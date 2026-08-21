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

| Deliverable                    | Link                                                           |
| ------------------------------ | -------------------------------------------------------------- |
| Planning Dashboard (Streamlit) | https://project-foresight-bm7qjlc2xqqzf96oghyl6r.streamlit.app |
| Scoring Service (FastAPI)      | https://project-foresight-api-flsj.onrender.com                |
| API documentation              | https://project-foresight-api-flsj.onrender.com/docs           |

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

The project uses four core project datasets, adapted from the M5 Forecasting competition
and mapped onto the brief's schema: sales, calendar, SKU master, and inventory snapshots.
The inventory snapshot dataset is simulated because the M5 source does not contain observed
inventory balances, replenishment orders, receipts, lead times, or stockout records.

The primary M5 source files are:

* `sales_train_validation.csv.gz`
* `calendar.csv`
* `sell_prices.csv.gz`

The transformation and validation logic is implemented in Notebook 01.

A fixed, category-balanced **development scope of 300 SKU-store series** (30 products × 10
stores) is used throughout the forecasting and inventory-intelligence workflow, documented
in `data/processed/development_sku_scope.csv`.

## Key Assumptions and Limitations

Full detail in [`docs/assumptions_limitations.md`](docs/assumptions_limitations.md). The
most important ones to know before reading any result in this project:

* **Inventory position (`inventory_snapshots_final.csv`) is simulated**, derived from
  historical demand patterns — not real client inventory data. In this run, the simulation
  did not produce any stockout scenarios across the 300 series (0 flagged "Reorder Now").
* **Unit cost and list price are estimated**, not observed client figures. Every rupee value
  in this project's dashboards, risk scores, and executive readout is therefore an
  **estimate for illustration of methodology**, not a fact.
* Every decision made in this project — including the M5 substitution and the development
  scope — is logged with rationale in [`docs/decision_log.md`](docs/decision_log.md).

## Forecasting Result (Backtest vs Baseline)

Following the engagement's non-negotiable rule — *"beat the baseline, honestly, or ship the
baseline and say why"* — both a statistical baseline and a machine-learning model were
developed under identical rolling-origin validation, then compared once on an untouched
final-test period.

| Model                                         | Validation WAPE | Final-Test WAPE | Final-Test Bias |
| --------------------------------------------- | --------------: | --------------: | --------------: |
| Baseline — damped-trend exponential smoothing |          50.02% |      **53.17%** |         +10.94% |
| ML — LightGBM                                 |          50.67% |          59.34% |         +11.03% |

**Outcome: the baseline was retained as the production forecaster.** The ML model was fairly
developed and validated under the same rules as the baseline, but it did not outperform the
baseline on the untouched final-test period. The baseline also achieved lower WAPE at every
forecast horizon from 1 to 8 weeks. This is reported as-is, consistent with the engagement's
requirement to beat the baseline honestly or ship the baseline and document why.

## Risk Scoring Result

Of the 300 SKU-store series scored (Notebook 07): **281 Healthy, 19 Markdown/Clear, 0 Reorder
Now, 0 Watch/Volatile.** The Markdown/Clear group is concentrated in a single product
(`FOODS_1_004`) overstocked across nearly every store — a systemic pattern worth a manual
pricing/promotion review, not a random spread across the catalogue.

---

## Repository Structure

```text
Project FORESIGHT/
├── notebooks/
│   ├── 00_Phase_0_Setup.ipynb
│   ├── 01_Data_Engineering_Validation.ipynb
│   ├── 02_Exploratory_Data_Analysis.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Baseline_Forecasting.ipynb
│   ├── 05_Machine_Learning_Forecasting.ipynb
│   ├── 06_Model_Evaluation.ipynb
│   └── 07_Inventory_Intelligence.ipynb
│
├── data/
│   ├── raw/                     source extracts (local only; excluded from Git)
│   ├── interim/                 intermediate datasets (local only; excluded from Git)
│   ├── modeling/
│   │   ├── categorical_features.json
│   │   ├── feature_dictionary.csv
│   │   ├── model_feature_list.json
│   │   └── weekly_features_final.csv
│   │
│   └── processed/
│       ├── development_sku_scope.csv
│       ├── sku_master_final.csv
│       ├── baseline_outputs/
│       ├── ml_outputs/
│       ├── inventory_outputs/
│       └── production_outputs/
│
├── reports/
│   ├── figures/                 analysis and diagnostic charts
│   ├── tables/                  reporting and audit tables
│   ├── notebook_exports/        PDF exports of notebooks 00–07
│   └── executive_report/        EDA Insight Memo
│
├── docs/
│   ├── project_roadmap.md
│   ├── decision_log.md
│   ├── development_scope.md
│   └── assumptions_limitations.md
│
├── streamlit_app/
│   └── app.py
│
├── api/
│   └── main.py
│
├── presentation/
│   └── Executive_Readout.pptx
│
├── run_data_pipeline.py
├── requirements.txt
├── README.md
└── .gitignore
```

> **Note on data files:** `data/raw/` contains the original source extracts and is excluded
> from version control. `data/interim/` contains intermediate analytical datasets and is
> also excluded. Large generated datasets such as `sales_daily_final.csv`,
> `calendar_final.csv`, and `inventory_snapshots_final.csv` are excluded because they can
> be regenerated from the project pipeline. The smaller `development_sku_scope.csv` file
> is retained as the authoritative definition of the 300-series development population.
> `sku_master_final.csv` and the committed files under `data/processed/*_outputs/` are
> retained because they are required by the dashboard, API, evaluation, and final project
> outputs. The files under `data/modeling/` contain the feature-engineered modelling data
> and supporting feature metadata required to document the forecasting workflow.
> Jupyter checkpoint and temporary/cache files are excluded from version control.

## Setup and Run Instructions

**1. Clone and install dependencies**

```bash
git clone https://github.com/mohitkumar29239/project-foresight.git
cd project-foresight
pip install -r requirements.txt
```

**2. Prepare the source data**

The original M5 source extracts are excluded from version control because of their size.
Before reproducing the project pipeline, place these files in `data/raw/`:

```text
data/raw/calendar.csv
data/raw/sales_train_validation.csv.gz
data/raw/sell_prices.csv.gz
```

These are the public M5 source files used by Notebook 01.

**3. Re-run the analytical pipeline (optional)**

For a fresh reproduction, run the notebooks in the following dependency order:

1. `01_Data_Engineering_Validation.ipynb`
2. `00_Phase_0_Setup.ipynb`
3. `02_Exploratory_Data_Analysis.ipynb`
4. `03_Feature_Engineering.ipynb`
5. `04_Baseline_Forecasting.ipynb`
6. `05_Machine_Learning_Forecasting.ipynb`
7. `06_Model_Evaluation.ipynb`
8. `07_Inventory_Intelligence.ipynb`

Notebook 00 is numbered as the conceptual Phase 0 notebook, but some of its validation
cells depend on the processed output generated by Notebook 01. The numbered workflow
should therefore follow the dependency order above rather than simple numeric order.

The committed outputs are retained for review, so a full rerun is optional unless
reproducing the analytical workflow from source data.

**4. Run the planning dashboard locally**

```bash
streamlit run streamlit_app/app.py
```

**5. Run the scoring service locally**

```bash
uvicorn api.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for interactive API documentation.

---

## Project Status

* [x] Notebook 00 — Phase 0 Setup / Governance Audit
* [x] Notebook 01 — Data Engineering & Validation
* [x] Notebook 02 — Exploratory Data Analysis
* [x] Notebook 03 — Feature Engineering
* [x] Notebook 04 — Baseline Forecasting
* [x] Notebook 05 — Machine-Learning Forecasting
* [x] Notebook 06 — Model Evaluation
* [x] Notebook 07 — Inventory Intelligence
* [x] Streamlit Planning Dashboard — deployed
* [x] FastAPI Scoring Service — deployed
* [x] Executive Readout Deck
* [x] Power BI Report — descoped from mandatory submission
* [ ] Demo Video

---

*Mohit Kumar · Zidio Development Data Science & Analytics Internship · Project FORESIGHT ·
Client: NorthBay Living*
