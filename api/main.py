"""
Project FORESIGHT — Scoring Service
Zidio Development Internship | NorthBay Living Demand & Inventory Intelligence

Returns forecast + risk for a SKU-store series, or a batch of them.

Run locally with:  uvicorn api.main:app --reload
(run from the project root, or adjust PROJECT_ROOT below)

Docs (auto-generated): http://127.0.0.1:8000/docs
"""

from pathlib import Path
from typing import List, Optional

import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# ============================================================
# Paths (same convention as the notebooks and the dashboard)
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
PRODUCTION_DIR = PROCESSED_DIR / "production_outputs"
INVENTORY_DIR = PROCESSED_DIR / "inventory_outputs"

PRODUCTION_FORECAST_FILE = PRODUCTION_DIR / "06_production_forecast.csv"
RISK_SCORES_FILE = INVENTORY_DIR / "07_risk_scores.csv"

app = FastAPI(
    title="Project FORESIGHT Scoring Service",
    description="Returns demand forecast and stockout/overstock risk for NorthBay Living SKU-store series.",
    version="1.0.0",
)

# ============================================================
# Load Data Once at Startup
# ============================================================

_forecast_df: Optional[pd.DataFrame] = None
_risk_df: Optional[pd.DataFrame] = None


@app.on_event("startup")
def load_data():
    global _forecast_df, _risk_df

    if PRODUCTION_FORECAST_FILE.exists():
        _forecast_df = pd.read_csv(PRODUCTION_FORECAST_FILE, parse_dates=["week_start_date"])
    else:
        _forecast_df = None
        print(f"⚠️  Production forecast not found at {PRODUCTION_FORECAST_FILE} — "
              f"run Notebook 06 before using /forecast endpoints.")

    if RISK_SCORES_FILE.exists():
        _risk_df = pd.read_csv(RISK_SCORES_FILE)
    else:
        _risk_df = None
        print(f"⚠️  Risk scores not found at {RISK_SCORES_FILE} — "
              f"run Notebook 07 before using /risk endpoints.")


# ============================================================
# Response Models
# ============================================================

class ForecastPoint(BaseModel):
    week_start_date: str
    horizon: int
    actual_demand: Optional[float] = None
    forecast_demand: float


class ForecastResponse(BaseModel):
    sku_id: str
    source_model: Optional[str] = None
    forecast: List[ForecastPoint]


class RiskResponse(BaseModel):
    sku_id: str
    stockout_risk_score: float
    overstock_risk_score: float
    quadrant: str
    recommended_action: str
    estimated_value_at_stake: float


class CombinedResponse(BaseModel):
    forecast: ForecastResponse
    risk: Optional[RiskResponse] = None


class BatchRequest(BaseModel):
    sku_ids: List[str]


# ============================================================
# Helpers
# ============================================================

def _get_forecast_for_sku(sku_id: str) -> ForecastResponse:
    if _forecast_df is None:
        raise HTTPException(status_code=503, detail="Production forecast not available. Run Notebook 06 first.")

    series = _forecast_df[_forecast_df["sku_id"] == sku_id]
    if series.empty:
        raise HTTPException(status_code=404, detail=f"No forecast found for sku_id='{sku_id}'.")

    points = [
        ForecastPoint(
            week_start_date=str(row["week_start_date"].date()) if hasattr(row["week_start_date"], "date") else str(row["week_start_date"]),
            horizon=int(row["horizon"]),
            actual_demand=float(row["actual_demand"]) if pd.notna(row.get("actual_demand")) else None,
            forecast_demand=float(row["forecast_demand"]),
        )
        for _, row in series.sort_values("horizon").iterrows()
    ]
    source_model = series["source_model"].iloc[0] if "source_model" in series.columns else None
    return ForecastResponse(sku_id=sku_id, source_model=source_model, forecast=points)


def _get_risk_for_sku(sku_id: str) -> Optional[RiskResponse]:
    if _risk_df is None:
        return None

    row = _risk_df[_risk_df["sku_id"] == sku_id]
    if row.empty:
        return None

    r = row.iloc[0]
    return RiskResponse(
        sku_id=sku_id,
        stockout_risk_score=float(r["stockout_risk_score"]),
        overstock_risk_score=float(r["overstock_risk_score"]),
        quadrant=str(r["quadrant"]),
        recommended_action=str(r["recommended_action"]),
        estimated_value_at_stake=float(r["estimated_value_at_stake"]),
    )


# ============================================================
# Endpoints
# ============================================================

@app.get("/", tags=["health"])
def root():
    return {
        "service": "Project FORESIGHT Scoring Service",
        "status": "ok",
        "forecast_data_loaded": _forecast_df is not None,
        "risk_data_loaded": _risk_df is not None,
    }


@app.get("/forecast/{sku_id}", response_model=ForecastResponse, tags=["forecast"])
def get_forecast(sku_id: str):
    """Return the production forecast for a single SKU-store series."""
    return _get_forecast_for_sku(sku_id)


@app.get("/risk/{sku_id}", response_model=RiskResponse, tags=["risk"])
def get_risk(sku_id: str):
    """Return the stockout/overstock risk assessment for a single SKU-store series."""
    result = _get_risk_for_sku(sku_id)
    if result is None:
        raise HTTPException(status_code=404, detail=f"No risk score found for sku_id='{sku_id}'.")
    return result


@app.get("/score/{sku_id}", response_model=CombinedResponse, tags=["combined"])
def get_combined_score(sku_id: str):
    """Return forecast + risk together for a single SKU-store series — the main endpoint
    the dashboard and downstream tools should use."""
    forecast = _get_forecast_for_sku(sku_id)
    risk = _get_risk_for_sku(sku_id)
    return CombinedResponse(forecast=forecast, risk=risk)


@app.post("/score/batch", response_model=List[CombinedResponse], tags=["combined"])
def get_batch_score(request: BatchRequest):
    """Return forecast + risk for a batch of SKU-store series. Series that fail individually
    are skipped (not raised) so one bad ID doesn't fail the whole batch."""
    if not request.sku_ids:
        raise HTTPException(status_code=400, detail="sku_ids must not be empty.")
    if len(request.sku_ids) > 500:
        raise HTTPException(status_code=400, detail="Batch size limited to 500 SKU-store series per request.")

    results = []
    for sku_id in request.sku_ids:
        try:
            forecast = _get_forecast_for_sku(sku_id)
            risk = _get_risk_for_sku(sku_id)
            results.append(CombinedResponse(forecast=forecast, risk=risk))
        except HTTPException:
            continue  # gracefully skip unknown SKUs rather than failing the whole batch

    return results
