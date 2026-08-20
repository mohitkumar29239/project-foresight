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
| **Last Updated** | August 2026 |

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

Project FORESIGHT has completed its core analytical, modelling, risk-scoring, productization, and deployment stages.

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
- Deployment of the Streamlit application
- Deployment of the FastAPI scoring service

## Current Remaining Work

The remaining project work is primarily final submission and communication:

- final documentation cleanup;
- final repository audit;
- demo video;
- final submission form;
- optional career/portfolio packaging after the technical submission is complete.

## Portfolio Enhancement

Power BI was originally planned as an additional reporting layer but has been **descoped due to time constraints**.

The Streamlit dashboard and FastAPI scoring service already cover the primary interactive delivery and scoring-service requirements.

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

The remaining work is final submission packaging and demonstration.

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

---

# 7. Key Assumptions and Limitations

The project contains several important methodological limitations.

## 7.1 Simulated Inventory

`inventory_snapshots_final.csv` contains simulated inventory positions rather than observed client inventory.

The simulation produced:

- **0 Reorder Now cases**
- **19 Markdown/Clear cases**
- **281 Healthy cases**
- **0 Watch/Volatile cases**

Therefore, the absence of stockout recommendations should not be interpreted as proof that NorthBay Living has no stockout problem.

---

## 7.2 Estimated Financial Values

Unit cost, list price, inventory value, revenue exposure, and related financial calculations are estimated analytical values.

They are included to demonstrate the methodology and decision framework.

They must not be presented as observed NorthBay Living financial figures.

---

## 7.3 M5 Adaptation

The project uses public M5 data adapted to the engagement brief.

The resulting datasets and business terminology are therefore a project-specific analytical adaptation rather than a direct extraction from an actual NorthBay Living operational system.

---

## 7.4 Development Scope

The modelling workflow is intentionally restricted to the defined 300-series development scope.

Results should therefore be interpreted as evidence from the project development population rather than a claim about an entire unseen retailer catalogue.

---

## 7.5 Forecasting Performance

The machine-learning model did not outperform the selected baseline on the untouched final-test period.

This result is intentionally reported rather than hidden.

The baseline was retained as the production forecasting approach.

---

# 8. End-to-End Project Architecture

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