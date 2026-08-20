# Project FORESIGHT — Master Roadmap

## Document Control

| Item | Details |
|---|---|
| **Project** | Project FORESIGHT |
| **Author** | Mohit Kumar |
| **Internship** | Zidio Development |
| **Client** | NorthBay Living |
| **Roadmap Version** | 3.1 |
| **Status** | Locked |
| **Last Updated** | 21 August 2026 |

---

# 1. Project Objective

Project FORESIGHT is an end-to-end demand forecasting and inventory intelligence project designed to transform retail data into actionable business decisions.

The project transforms raw retail sales and reference data into:

- validated analytical datasets;
- weekly SKU-store demand forecasts;
- forecast-performance evaluations;
- stockout and overstock risk scores;
- replenishment and markdown recommendations;
- inventory intelligence outputs;
- an interactive planning dashboard;
- a deployed scoring service;
- executive-level business recommendations.

The project was developed as part of the Zidio Development Data Science & Analytics internship and adapted to a simulated client engagement for **NorthBay Living**, a mid-size direct-to-consumer home and lifestyle brand.

The intended business users are non-technical Operations and Finance stakeholders who need to answer:

- What is selling?
- Which products may stock out?
- Which products are overstocked?
- What should be reordered?
- What should be marked down?
- Where is inventory capital potentially locked?
- What does the forecast suggest for the next eight weeks?

---

# 2. Current Project Status

Project FORESIGHT has completed its core data engineering, analytical, forecasting, evaluation, inventory-intelligence, productization, deployment, and executive communication stages.

The **core technical scope is now frozen for final submission**.

## Completed Core Work

- Notebook 01 — Data Engineering and Validation
- Notebook 02 — Exploratory Data Analysis
- Notebook 03 — Forecasting Feature Engineering
- Notebook 04 — Baseline Forecasting
- Notebook 05 — Machine-Learning Forecasting
- Notebook 06 — Model Evaluation and Selection
- Notebook 07 — Inventory Intelligence and Risk Scoring
- Streamlit Planning Dashboard
- FastAPI Scoring Service
- Executive Readout
- Final forecasting evaluation
- Final inventory-risk scoring
- Notebook PDF exports for key modelling stages
- README documentation
- Streamlit deployment
- FastAPI deployment
- Final production forecasting configuration
- Final model comparison and selection evidence
- Decision-log governance updates

## Current Remaining Work

The remaining project work is primarily final submission and communication:

- final documentation cleanup;
- final repository audit;
- deployment verification;
- demo video;
- final submission form;
- final presentation or demonstration preparation.

Optional career and portfolio packaging may be completed after the technical submission.

## Portfolio Enhancement

Power BI was originally planned as an additional reporting layer but has been **de-scoped from the mandatory final submission**.

The Streamlit dashboard and FastAPI scoring service already provide the primary interactive planning and scoring capabilities required by the project.

Power BI may be developed later as an optional portfolio enhancement and does not block project completion.

---

# 3. Official Client Deliverables

| ID | Deliverable | Final Status | Project Output |
|---|---|---|---|
| **D1** | Reproducible data pipeline | **Completed** | Notebook 01 + `run_data_pipeline.py` |
| **D2** | Data-quality and EDA insight work | **Completed** | Notebook 02 + EDA outputs |
| **D3** | Weekly demand forecast model | **Completed** | Notebooks 03–06 |
| **D4** | Stockout and overstock risk scoring | **Completed** | Notebook 07 |
| **D5** | Interactive planning dashboard | **Completed / Deployed** | Streamlit application |
| **D6** | Deployed scoring service | **Completed / Deployed** | FastAPI service |
| **D7** | Executive readout | **Completed** | `presentation/Executive_Readout.pptx` |

All mandatory analytical and productization deliverables have been completed.

The remaining work is final submission packaging, demonstration, and documentation verification.

---

# 4. Live Deployments

| Deliverable | URL |
|---|---|
| **Planning Dashboard** | https://project-foresight-bm7qjlc2xqqzf96oghyl6r.streamlit.app |
| **Scoring Service** | https://project-foresight-api-flsj.onrender.com |
| **API Documentation** | https://project-foresight-api-flsj.onrender.com/docs |

The FastAPI scoring service is deployed on Render's free tier.

The service may sleep after inactivity. The first request after a period of inactivity may therefore take approximately 30–50 seconds while the service wakes up.

This behaviour is a deployment-platform characteristic and does not indicate an application failure.

---

# 5. Data and Project Adaptation

The original Zidio engagement brief describes four simulated client extracts covering sales, calendar, SKU information, and inventory snapshots.

Project FORESIGHT adapts that business problem using public M5 Forecasting source data.

The primary source files are:

- `sales_train_validation.csv.gz`
- `calendar.csv`
- `sell_prices.csv.gz`

These are transformed into the project datasets:

- `sales_daily_final.csv`
- `calendar_final.csv`
- `sku_master_final.csv`
- `inventory_snapshots_final.csv`
- `development_sku_scope.csv`

The inventory snapshot dataset is simulated because the M5 source data does not contain observed:

- stock balances;
- replenishment orders;
- receipts;
- lead times;
- stockout records.

Therefore, inventory-based financial values, risk scores, and recommendations are analytical estimates rather than observed NorthBay Living business figures.

The project must consistently disclose that the M5 dataset is a **public-data adaptation of the business problem**, not a direct extraction from an actual NorthBay Living operational system.

---

# 6. Development Scope

The project uses a fixed development scope of **300 SKU-store series** throughout the forecasting and inventory-intelligence workflow.

The scope represents:

- 30 representative products;
- 10 stores;
- historical sales observations covering the available development period.

The complete SKU master contains substantially more reference records, but the modelling and decision-support workflow is intentionally restricted to the defined development population.

The authoritative scope file is:

`data/processed/development_sku_scope.csv`

This scope protection prevents KPI and model comparisons from being calculated over inconsistent populations.

No expansion of the modelling population is planned for the mandatory final submission.

---

# 7. Forecasting Design and Model Selection

## 7.1 Forecast Grain

Forecasts are produced at the **weekly SKU-store level**.

Weekly aggregation provides a more stable planning grain than daily SKU demand while preserving product and store-level detail required for inventory decisions.

---

## 7.2 Forecast Horizon

The project uses an **eight-week forecast horizon**.

The same horizon is used across:

- baseline forecasting;
- machine-learning forecasting;
- model evaluation;
- final production forecasting;
- inventory-risk calculations.

The eight-week horizon is therefore part of the locked production configuration.

---

## 7.3 Primary Forecast Metric

The primary forecasting evaluation metric is **Weighted Absolute Percentage Error (WAPE)**.

Forecast Bias is used as a secondary metric, with MAE and RMSE serving as supporting metrics where applicable.

WAPE is used because it evaluates aggregate absolute forecast error relative to aggregate actual demand and is suitable for comparing performance across series with different sales volumes.

---

## 7.4 Validation Method

Forecasting models are evaluated using **chronological rolling-origin validation**.

Random train-test splitting is not used for the principal forecasting evaluation because it can introduce future information into model development and produce misleading estimates of forecasting performance.

The final evaluation workflow preserves chronological order.

---

## 7.5 Final Holdout

The latest **eight weeks** of available demand data are protected as an untouched final-test period.

This final holdout is not used for:

- feature design;
- model tuning;
- model selection;
- production configuration decisions.

The final-test period is used to provide the final evidence for production model selection.

---

## 7.6 Baseline

A transparent statistical baseline is mandatory for model comparison.

The final production baseline is a **damped-trend exponential-smoothing model** selected through the completed baseline workflow.

The baseline is documented in:

`data/processed/baseline_outputs/04_champion_baseline_config.json`

The baseline remains the authoritative production forecasting method for the current submission.

---

## 7.7 Machine-Learning Forecasting

LightGBM is used as the primary machine-learning forecasting approach.

XGBoost was considered as a secondary machine-learning approach during modelling design.

The machine-learning workflow uses forecasting features such as:

- lag variables;
- rolling statistics;
- calendar information;
- pricing information;
- promotional/event information;
- categorical SKU and store information.

The machine-learning model is evaluated against the established baseline under the same forecasting and evaluation framework.

The ML model is not automatically promoted to production.

---

## 7.8 Final Model Selection

The final production model is selected using objective evaluation evidence and predefined selection guardrails.

On the untouched eight-week final-test period:

| Model | Final-Test WAPE |
|---|---:|
| **Damped-Trend Exponential Smoothing Baseline** | **53.17%** |
| **LightGBM** | **59.34%** |

The machine-learning model therefore did **not** outperform the production baseline.

The baseline achieved lower WAPE and remained the selected production forecasting approach.

This result is intentionally retained as part of the project evidence rather than being hidden or replaced with an unsupported model-selection claim.

The final production forecasting configuration is locked in:

`data/processed/production_outputs/06_production_forecast_config.json`

---

# 8. Inventory Intelligence and Risk Scoring

Inventory risk is calculated using transparent business rules rather than an unexplained black-box classification model.

The scoring framework combines forecast and inventory-planning indicators such as:

- forecast demand;
- inventory position;
- demand coverage;
- lead-time-related planning information;
- safety-stock-related planning information;
- forecast confidence and related indicators.

The methodology is designed so that each risk classification and recommended action can be traced to documented logic and assumptions.

The inventory outputs include:

- stockout-risk assessment;
- overstock-risk assessment;
- replenishment recommendations;
- markdown recommendations;
- inventory exposure indicators.

Because inventory and financial inputs are simulated or estimated where observed client data was unavailable, the resulting risk scores and financial exposure values are **illustrative analytical estimates** rather than observed NorthBay Living outcomes.

---

# 9. Inventory Snapshot Results

The current simulated inventory-risk workflow produced:

- **0 Reorder Now cases**
- **19 Markdown/Clear cases**
- **281 Healthy cases**
- **0 Watch/Volatile cases**

These results demonstrate the scoring framework but must not be interpreted as evidence that an actual NorthBay Living inventory system contains no stockout risk.

The authoritative inventory outputs are generated within the project's processed inventory outputs.

---

# 10. End-to-End Project Architecture

```text
Public M5 Source Data
        │
        ▼
Notebook 01
Data Engineering & Validation
        │
        ├── sales_daily_final.csv
        ├── calendar_final.csv
        ├── sku_master_final.csv
        ├── inventory_snapshots_final.csv
        └── development_sku_scope.csv
        │
        ▼
Notebook 02
Exploratory Data Analysis
        │
        ▼
Notebook 03
Forecasting Feature Engineering
        │
        ▼
Notebook 04
Baseline Forecasting
        │
        ▼
Notebook 05
Machine-Learning Forecasting
        │
        ▼
Notebook 06
Model Evaluation & Selection
        │
        ├── Baseline vs ML evaluation
        ├── Final-test evidence
        └── Production forecast configuration
        │
        ▼
Notebook 07
Inventory Intelligence & Risk Scoring
        │
        ├──────────────────────┐
        ▼                      ▼
Streamlit Dashboard       FastAPI Service
        │                      │
        └──────────┬───────────┘
                   ▼
            Executive Readout
                   │
                   ▼
             Final Submission