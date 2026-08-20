# Project FORESIGHT

**AI-Powered Demand & Inventory Intelligence Platform**

Project FORESIGHT is an end-to-end retail analytics and machine-learning project, developed
as part of the Zidio Development Data Science & Analytics internship. It was built as a
client engagement for **NorthBay Living**, a mid-size direct-to-consumer home & lifestyle
brand, whose planning team currently manages inventory on spreadsheets with no forecasting
in place.

The project transforms raw sales and inventory data into validated analytical datasets,
forecasts weekly demand at SKU-store level, scores stockout and overstock risk, and delivers
the results through a planning dashboard and a deployed scoring service — so a non-technical
operations team can decide what to reorder, what to clear, and what to leave alone, without
needing a data scientist in the room.

---

## Live Deployments

| Deliverable | Link |
|---|---|
| Planning Dashboard (Streamlit) | https://project-foresight-bm7qjlc2xqqzf96oghyl6r.streamlit.app |
| Scoring Service (FastAPI) | https://project-foresight-api-flsj.onrender.com/docs |

> **Note:** the scoring service runs on Render's free tier, which sleeps after 15 minutes of
> inactivity. The first request after a period of inactivity may take 30–50 seconds to
> respond while the service wakes up — this is expected, not an error.

---

## The Business Problem

NorthBay Living loses money in two directions at once: best-selling products run out
(lost sales that can never be recovered), while slow movers pile up (cash locked in stock
that later gets marked down). Project FORESIGHT builds a demand forecast and an early-warning
system that flags, for every product, how much will likely sell over the next 8 weeks, which
products are at risk of stocking out, and which are overstocked.

## Data

Four datasets are used, adapted from the M5 Forecasting competition and mapped onto the
brief's schema (sales, calendar, SKU master, inventory snapshots). The full data dictionary
is in the engagement brief; the transformation logic is in Notebook 01.

A fixed, category-balanced **development scope of 300 SKU-store series** (30 products × 10
stores) is used throughout the pipeline, documented in `data/processed/development_sku_scope.csv`.

## Key Assumptions and Limitations

Full detail in [`docs/assumptions_limitations.md`](docs/assumptions_limitations.md). The
most important ones to know before reading any result in this project:

- **Inventory position (`inventory_snapshots_final.csv`) is simulated**, derived from
  historical demand patterns — not real client inventory data. In this run, the simulation
  did not produce any stockout scenarios across the 300 series (0 flagged "Reorder Now").
- **Unit cost and list price are estimated**, not observed client figures. Every rupee value
  in this project's dashboards, risk scores, and executive readout is therefore an
  **estimate for illustration of methodology**, not a fact.
- Every decision made in this project — including the M5 substitution and the development
  scope — is logged with rationale in [`docs/decision_log.md`](docs/decision_log.md).

## Forecasting Result (Backtest vs Baseline)

Following the engagement's non-negotiable rule — *"beat the baseline, honestly, or ship the
baseline and say why"* — both a statistical baseline and a machine-learning model were
developed under identical rolling-origin validation, then compared once on an untouched
final-test period.

| Model | Validation WAPE | Final-Test WAPE | Final-Test Bias |
|---|---|---|---|
| Baseline — damped-trend exponential smoothing (Notebook 04) | 50.02% | **53.17%** | +10.94% |
| ML — LightGBM (Notebook 05) | 50.67% | 59.34% | +11.03% |

**Outcome: the baseline was retained as the production forecaster.** The ML model was fairly
developed and validated under the same rules as the baseline, but did not clear the
pre-declared improvement threshold on the untouched final test (Notebook 06). This is reported
as-is, per the engagement's honesty requirement — a retained baseline is a valid, documented
outcome, not a failure.

## Risk Scoring Result

Of the 300 SKU-store series scored (Notebook 07): **281 Healthy, 19 Markdown/Clear, 0 Reorder
Now, 0 Watch/Volatile.** The Markdown/Clear group is concentrated in a single product
(`FOODS_1_004`) overstocked across nearly every store — a systemic pattern worth a manual
pricing/promotion review, not a random spread across the catalogue.

---

## Repository Structure

```
Project FORESIGHT/
├── notebooks/              00-07: the full pipeline, in run order
├── data/
│   ├── raw/                 source extracts (not in version control - see below)
│   ├── processed/           cleaned datasets + model/production/inventory outputs
│   └── modeling/            feature-engineered weekly dataset (not in version control)
├── reports/
│   ├── figures/              all analysis and diagnostic charts, prefixed by notebook
│   ├── tables/                all reporting tables, prefixed by notebook
│   ├── notebook_exports/      PDF exports of key notebooks
│   └── executive_report/      EDA Insight Memo
├── docs/                     decision log, assumptions/limitations, project roadmap
├── streamlit_app/app.py      planning dashboard
├── api/main.py                scoring service (FastAPI)
├── presentation/               executive readout deck
├── run_data_pipeline.py
└── requirements.txt
```

> **Note on data files:** `data/raw/`, `data/interim/`, `data/modeling/`, and the largest
> processed files (`sales_daily_final.csv`, `inventory_snapshots_final.csv`) are excluded
> from version control (see `.gitignore`) since they are large and fully regenerable from
> Notebook 01 onward. Everything the dashboard and API need to run is included.

## Setup and Run Instructions

**1. Clone and install dependencies**

```bash
git clone https://github.com/mohitkumar29239/project-foresight.git
cd project-foresight
pip install -r requirements.txt
```

**2. Re-run the full pipeline (optional — outputs are already committed)**

Run the notebooks in `notebooks/` in numeric order, 00 through 07, top to bottom. Each
notebook validates its own inputs and outputs before proceeding, so an out-of-order or
partial run will fail loudly rather than silently produce bad results.

**3. Run the planning dashboard locally**

```bash
streamlit run streamlit_app/app.py
```

**4. Run the scoring service locally**

```bash
uvicorn api.main:app --reload
```
Visit `http://127.0.0.1:8000/docs` for interactive API documentation.

---

## Project Status

- [x] Notebook 00 — Phase 0 Setup
- [x] Notebook 01 — Data Engineering & Validation
- [x] Notebook 02 — Exploratory Data Analysis
- [x] Notebook 03 — Feature Engineering
- [x] Notebook 04 — Baseline Forecasting
- [x] Notebook 05 — Machine-Learning Forecasting
- [x] Notebook 06 — Model Evaluation & Selection
- [x] Notebook 07 — Inventory Intelligence & Risk Scoring
- [x] Streamlit Planning Dashboard — deployed
- [x] FastAPI Scoring Service — deployed
- [x] Executive Readout Deck
- [x] Power BI Report — descoped (time constraint; dashboard + API cover the same delivery goal)
- [ ] Demo Video

---

*Mohit Kumar · Zidio Development Data Science & Analytics Internship · Project FORESIGHT ·
Client: NorthBay Living*