"""
Project FORESIGHT — Planning Dashboard
Zidio Development Internship | NorthBay Living Demand & Inventory Intelligence

Run with:  streamlit run streamlit_app/app.py
(run from the project root, or adjust PROJECT_ROOT below)
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Project FORESIGHT — NorthBay Living",
    page_icon="📊",
    layout="wide",
)

# ============================================================
# Paths (same convention as the notebooks)
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
PRODUCTION_DIR = PROCESSED_DIR / "production_outputs"
INVENTORY_DIR = PROCESSED_DIR / "inventory_outputs"
BASELINE_DIR = PROCESSED_DIR / "baseline_outputs"
REPORTS_TABLES = PROJECT_ROOT / "reports" / "tables"


# ============================================================
# Cached Data Loaders
# ============================================================

@st.cache_data
def load_data():
    """Load every dataset the dashboard needs. Returns None for any file not yet present,
    so pages can show a clear empty state instead of crashing."""
    data = {}

   
    def try_read_csv(path, **kwargs):
        return pd.read_csv(path, **kwargs) if path.exists() else None

    def try_read_json(path):
        if path.exists():
            with open(path) as f:
                return json.load(f)
        return None

    data["sku_master"] = try_read_csv(PROCESSED_DIR / "sku_master_final.csv")
    data["production_forecast"] = try_read_csv(
        PRODUCTION_DIR / "06_production_forecast.csv", parse_dates=["week_start_date"]
    )
    data["production_config"] = try_read_json(PRODUCTION_DIR / "06_production_forecast_config.json")
    data["risk_scores"] = try_read_csv(INVENTORY_DIR / "07_risk_scores.csv")
    data["action_list"] = try_read_csv(INVENTORY_DIR / "07_prioritized_action_list.csv")
    data["risk_config"] = try_read_json(INVENTORY_DIR / "07_risk_scoring_config.json")
    data["baseline_metrics"] = try_read_csv(BASELINE_DIR / "04_baseline_model_metrics.csv")
    data["comparison_scorecard"] = try_read_csv(REPORTS_TABLES / "06_model_comparison_scorecard.csv")

    return data


def missing_data_notice(name, path_hint):
    st.warning(
        f"**{name} not found yet.** Expected at `{path_hint}`. "
        f"Run the corresponding notebook first, then reload this page."
    )


# ============================================================
# Load Everything Once
# ============================================================

data = load_data()

# ============================================================
# Sidebar Navigation
# ============================================================

st.sidebar.title("📊 Project FORESIGHT")
st.sidebar.caption("Demand & Inventory Intelligence — NorthBay Living")

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Forecast", "Inventory & Risk", "Product Details", "Executive Summary"],
)

if data["sku_master"] is not None:
    categories = ["All"] + sorted(data["sku_master"]["category"].dropna().unique().tolist())
    selected_category = st.sidebar.selectbox("Category filter", categories)
else:
    selected_category = "All"


def filter_by_category(df, sku_col="sku_id"):
    """Apply the sidebar category filter to any dataframe with a sku_id column."""
    if selected_category == "All" or data["sku_master"] is None or df is None:
        return df
    allowed_skus = set(
        data["sku_master"].loc[data["sku_master"]["category"] == selected_category, "sku_id"]
    )
    return df[df[sku_col].isin(allowed_skus)]


# ============================================================
# PAGE: HOME
# ============================================================

if page == "Home":
    st.title("Project FORESIGHT")
    st.subheader("Demand & Inventory Intelligence for NorthBay Living")

    col1, col2, col3, col4 = st.columns(4)

    if data["production_config"]:
        col1.metric("Production Forecaster", data["production_config"].get("production_model", "—"))
        col2.metric(
            "Final-Test WAPE",
            f"{data['production_config'].get('ml_final_test_wape' if data['production_config'].get('ml_selected') else 'baseline_final_test_wape', '—')}%",
        )
    else:
        col1.metric("Production Forecaster", "—")
        col2.metric("Final-Test WAPE", "—")

    if data["action_list"] is not None:
        col3.metric("Series Requiring Action", len(data["action_list"]))
    else:
        col3.metric("Series Requiring Action", "—")

    if data["risk_scores"] is not None:
        col4.metric("Series Monitored", data["risk_scores"]["sku_id"].nunique())
    else:
        col4.metric("Series Monitored", "—")

    st.divider()
    st.markdown(
        """
        Use the sidebar to navigate:
        - **Forecast** — demand forecast vs actuals, by series
        - **Inventory & Risk** — the stockout/overstock decisioning grid and prioritized action list
        - **Product Details** — drill into any single SKU-store series
        - **Executive Summary** — headline numbers for a non-technical stakeholder
        """
    )

    if data["production_forecast"] is None:
        missing_data_notice("Production forecast", "data/processed/production_outputs/06_production_forecast.csv")
    if data["risk_scores"] is None:
        missing_data_notice("Risk scores", "data/processed/inventory_outputs/07_risk_scores.csv")


# ============================================================
# PAGE: FORECAST
# ============================================================

elif page == "Forecast":
    st.title("Demand Forecast")

    if data["production_forecast"] is None:
        missing_data_notice("Production forecast", "data/processed/production_outputs/06_production_forecast.csv")
    else:
        forecast_df = filter_by_category(data["production_forecast"])
        series_options = sorted(forecast_df["sku_id"].unique())
        selected_series = st.selectbox("Choose a SKU-store series", series_options)

        series_df = forecast_df[forecast_df["sku_id"] == selected_series].sort_values("week_start_date")

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=series_df["week_start_date"], y=series_df["actual_demand"],
            mode="lines+markers", name="Actual Demand", line=dict(color="#1E2761"),
        ))
        fig.add_trace(go.Scatter(
            x=series_df["week_start_date"], y=series_df["forecast_demand"],
            mode="lines+markers", name="Forecast", line=dict(color="#C0392B", dash="dash"),
        ))
        fig.update_layout(title=f"Actual vs Forecast — {selected_series}", height=450)
        st.plotly_chart(fig, use_container_width=True)

        if not series_df.empty:
            wape = (
                np.sum(np.abs(series_df["forecast_demand"] - series_df["actual_demand"]))
                / np.sum(series_df["actual_demand"]) * 100
            )
            st.metric("Series WAPE (final test)", f"{wape:.1f}%")

    st.divider()
    st.subheader("Model Comparison")
    if data["comparison_scorecard"] is not None:
        st.dataframe(data["comparison_scorecard"], use_container_width=True)
    else:
        missing_data_notice("Model comparison scorecard", "reports/tables/06_model_comparison_scorecard.csv")


# ============================================================
# PAGE: INVENTORY & RISK
# ============================================================

elif page == "Inventory & Risk":
    st.title("Inventory & Stock Risk")

    if data["risk_scores"] is None:
        missing_data_notice("Risk scores", "data/processed/inventory_outputs/07_risk_scores.csv")
    else:
        risk_df = filter_by_category(data["risk_scores"])

        quadrant_colors = {
            "Reorder Now": "#C0392B",
            "Markdown / Clear": "#8E44AD",
            "Watch / Volatile": "#D68910",
            "Healthy": "#27AE60",
        }

        fig = px.scatter(
            risk_df, x="overstock_risk_score", y="stockout_risk_score",
            color="quadrant", size="estimated_value_at_stake",
            color_discrete_map=quadrant_colors,
            hover_data=["sku_id", "recommended_action"],
            title="Decisioning Grid — Estimated value at stake sizes each bubble",
        )
        fig.add_hline(y=0.5, line_dash="dash", line_color="grey")
        fig.add_vline(x=0.5, line_dash="dash", line_color="grey")
        fig.update_layout(height=550)
        st.plotly_chart(fig, use_container_width=True)

        st.caption(
            "⚠️ Estimated value figures use simulated inventory and estimated unit-cost data "
            "(see docs/assumptions_limitations.md) — treat as illustrative, not exact."
        )

    st.divider()
    st.subheader("Prioritized Action List")

    if data["action_list"] is None:
        missing_data_notice("Prioritized action list", "data/processed/inventory_outputs/07_prioritized_action_list.csv")
    else:
        action_df = filter_by_category(data["action_list"])
        quadrant_filter = st.multiselect(
            "Filter by decision",
            options=action_df["quadrant"].unique().tolist(),
            default=action_df["quadrant"].unique().tolist(),
        )
        filtered_actions = action_df[action_df["quadrant"].isin(quadrant_filter)]
        st.dataframe(
            filtered_actions.sort_values("estimated_value_at_stake", ascending=False),
            use_container_width=True,
        )
        st.download_button(
            "Download this list as CSV",
            filtered_actions.to_csv(index=False),
            file_name="prioritized_action_list.csv",
        )


# ============================================================
# PAGE: PRODUCT DETAILS
# ============================================================

elif page == "Product Details":
    st.title("Product Details")

    if data["sku_master"] is None:
        missing_data_notice("SKU master", "data/processed/sku_master_final.csv")
    else:
        sku_df = filter_by_category(data["sku_master"])
        selected_sku = st.selectbox("Choose a series", sorted(sku_df["sku_id"].unique()))

        sku_row = sku_df[sku_df["sku_id"] == selected_sku]
        st.dataframe(sku_row, use_container_width=True)

        if data["risk_scores"] is not None:
            risk_row = data["risk_scores"][data["risk_scores"]["sku_id"] == selected_sku]
            if not risk_row.empty:
                r = risk_row.iloc[0]
                col1, col2, col3 = st.columns(3)
                col1.metric("Stockout Risk", f"{r['stockout_risk_score']:.2f}")
                col2.metric("Overstock Risk", f"{r['overstock_risk_score']:.2f}")
                col3.metric("Decision", r["quadrant"])
                st.info(f"**Recommended action:** {r['recommended_action']}")


# ============================================================
# PAGE: EXECUTIVE SUMMARY
# ============================================================

elif page == "Executive Summary":
    st.title("Executive Summary")
    st.caption("Headline numbers for the Head of Operations and Finance")

    if data["production_config"] and data["risk_config"]:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Forecast")
            st.metric("Production Model", data["production_config"].get("production_model", "—"))
            st.metric("Baseline Final-Test WAPE", f"{data['production_config'].get('baseline_final_test_wape', '—')}%")
            st.metric("WAPE Improvement", f"{data['production_config'].get('wape_improvement_pp', '—')} pp")

        with col2:
            st.markdown("### Inventory Risk")
            st.metric("Series Scored", data["risk_config"].get("series_scored", "—"))
            st.metric("Series Flagged for Action", data["risk_config"].get("series_flagged", "—"))

        if data["action_list"] is not None:
            st.divider()
            st.markdown("### Top Priorities")
            st.dataframe(
                data["action_list"].sort_values("estimated_value_at_stake", ascending=False).head(10),
                use_container_width=True,
            )
    else:
        st.warning("Run Notebooks 06 and 07 to populate the executive summary.")

    st.divider()
    st.caption(
        "Limitations: inventory position and unit-cost figures are simulated for this engagement "
        "(see docs/assumptions_limitations.md). Forecast accuracy is reported honestly, including "
        "any degradation from validation to the untouched final test."
    )
