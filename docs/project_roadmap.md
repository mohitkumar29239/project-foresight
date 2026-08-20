# Project FORESIGHT — Master Roadmap

## Document Control

| Item | Details |
|---|---|
| **Project** | Project FORESIGHT |
| **Author** | Mohit Kumar |
| **Internship** | Zidio Development |
| **Roadmap Version** | 3.0 |
| **Status** | Locked |
| **Last Updated** | August 2026 |

---

## 1. Project Objective

Project FORESIGHT is an end-to-end demand forecasting and inventory intelligence project designed to transform retail data into actionable business decisions.

The project will:

- build a reproducible data pipeline;
- analyse sales, pricing, seasonality, events, and inventory patterns;
- forecast weekly demand at the SKU-store level;
- identify stockout and overstock risks;
- recommend replenishment and markdown actions;
- quantify revenue at risk and capital locked in inventory;
- deliver results through dashboards, a deployed scoring service, and an executive readout.

---

## 2. Current Project Status

### Completed

- Notebook 01 — Data Engineering and Validation
- Five validated processed datasets
- Development-scope documentation
- Professional project-folder structure
- Initial README, `requirements.txt`, and `.gitignore`
- One-command data-pipeline runner
- Final Phase 0 audit with 41 of 41 checks passed

### Current Stage

The project is currently in the roadmap and governance stage.

Notebook 02 has not yet started. The complete project architecture, deliverables, dependencies, outputs, and completion criteria will be documented and locked before exploratory analysis begins.

---

## 3. Official Client Deliverables

| ID | Deliverable | Project Output |
|---|---|---|
| **D1** | Reproducible data pipeline | Notebook 01 and `run_data_pipeline.py` |
| **D2** | Data-quality and EDA insight memo | Notebook 02 and EDA report |
| **D3** | Weekly demand forecast model | Notebooks 03–06 |
| **D4** | Stockout and overstock risk scoring | Notebook 07 |
| **D5** | Interactive planning dashboard | Streamlit application |
| **D6** | Deployed scoring service | FastAPI service |
| **D7** | Executive readout | Presentation and business recommendations |

All seven deliverables must be completed before optional project enhancements are considered finished.

---

## 4. Project Implementation Adaptation

The original Zidio engagement brief describes four simulated client extracts.

Project FORESIGHT adapts that business problem using three public M5 source files:

- `sales_train_validation.csv.gz`;
- `calendar.csv`;
- `sell_prices.csv.gz`.

These files are transformed into the following project datasets:

- `sales_daily_final.csv`;
- `calendar_final.csv`;
- `sku_master_final.csv`;
- `inventory_snapshots_final.csv`;
- `development_sku_scope.csv`.

The Inventory Snapshot dataset is simulated because the M5 source data does not contain observed stock balances, replenishment orders, receipts, lead times, or stockout records.

Estimated costs, margins, lead times, safety-stock rules, replenishment policies, and inventory values must always be described as analytical assumptions rather than observed retailer information.

---

## 5. Development Scope

The analytical and modelling workflow uses 300 SKU-store series containing:

- 30 representative products;
- all 10 available stores;
- all 1,913 historical sales dates.

The complete SKU Master contains 30,490 SKU-store reference records. However, sales analysis, forecasting, inventory intelligence, risk scoring, and dashboard KPIs must use only the 300 SKU-store series listed in:

`data/processed/development_sku_scope.csv`

This rule prevents inconsistent KPI calculations across datasets with different population sizes.

---

## 6. End-to-End Project Architecture

```text
Raw M5 Source Data
        │
        ▼
Notebook 01
Data Engineering and Validation
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
Model Evaluation and Selection
        │
        ▼
Notebook 07
Inventory Intelligence and Risk Scoring
        │
        ▼
Dashboard-Ready Data Layer
        │
        ├──────────────┬──────────────┬──────────────┐
        ▼              ▼              ▼              ▼
    Streamlit       FastAPI        Power BI      Documentation
        │              │              │              │
        └──────────────┴──────────────┴──────────────┘
                               │
                               ▼
                         Deployment
                               │
                               ▼
                    Executive Communication
                               │
                               ▼
                       Final Submission
                               │
                               ▼
                   Resume and Portfolio Use


---

## 7. Core Analytical Stage Sequence

### Stage 0 — Data Foundation

**Status:** Completed

**Purpose:**  
Build and validate the project’s source-data pipeline.

**Completed outputs:**

- Notebook 01;
- five processed datasets;
- one-command pipeline runner;
- project-folder structure;
- development-scope documentation;
- initial configuration files;
- successful Phase 0 audit.

---

### Stage 1 — Roadmap and Project Governance

**Status:** Completed

**Purpose:**  
Define and lock the complete project architecture, responsibilities, outputs, dependencies, and completion criteria before Notebook 02 begins.

**Planned outputs:**

- `docs/project_roadmap.md`;
- `docs/decision_log.md`;
- `docs/assumptions_limitations.md`;
- final roadmap audit.

---

### Stage 2 — Notebook 02: Exploratory Data Analysis

**Status:** Not Started

**Purpose:**  
Analyse demand, sales, pricing, seasonality, product performance, events, and simulated inventory behaviour.

**Major outputs:**

- integrated daily analytical dataset;
- executive KPI summaries;
- performance tables;
- labelled analytical charts;
- business insights;
- EDA insight memo.

**Depends on:**  
Stage 0 and Stage 1.

---

### Stage 3 — Notebook 03: Forecasting Feature Engineering

**Status:** Not Started

**Purpose:**  
Create a leakage-safe weekly modelling dataset containing demand, calendar, pricing, event, and product features.

**Major outputs:**

- weekly modelling dataset;
- feature dictionary;
- feature-validation summary;
- modelling feature lists;
- leakage-audit results.

**Depends on:**  
Notebook 02.

---

### Stage 4 — Notebook 04: Baseline Forecasting

**Status:** Not Started

**Purpose:**  
Create simple benchmark forecasts that every advanced model must be compared against.

**Planned baseline models:**

- naive forecast;
- seasonal-naive forecast;
- four-week moving-average forecast.

**Major outputs:**

- baseline forecasts;
- WAPE results;
- Bias results;
- MAE and RMSE results;
- champion baseline configuration.

**Depends on:**  
Notebook 03.

---

### Stage 5 — Notebook 05: Machine-Learning Forecasting

**Status:** Not Started

**Purpose:**  
Train machine-learning forecasting models using the validated weekly feature dataset.

**Planned models:**

- LightGBM;
- XGBoost;
- optional Random Forest benchmark.

**Major outputs:**

- machine-learning forecasts;
- trained model files;
- preprocessing pipeline;
- fold-level performance metrics;
- feature-importance results.

**Depends on:**  
Notebook 03 and Notebook 04.

---

### Stage 6 — Notebook 06: Model Evaluation and Selection

**Status:** Not Started

**Purpose:**  
Compare baseline and machine-learning forecasts and select the final forecasting approach honestly.

**Major outputs:**

- model-comparison table;
- SKU-level evaluation;
- segment-level evaluation;
- forecast-confidence levels;
- champion-model decision;
- final forecast dataset;
- model card.

**Depends on:**  
Notebook 04 and Notebook 05.

---

### Stage 7 — Notebook 07: Inventory Intelligence and Risk Scoring

**Status:** Not Started

**Purpose:**  
Convert final forecasts into transparent stockout, overstock, replenishment, and markdown decisions.

**Major outputs:**

- stockout-risk scores;
- overstock-risk scores;
- recommended reorder quantities;
- markdown recommendations;
- decisioning grid;
- rupee value at risk;
- dashboard-ready master dataset.

**Depends on:**  
Notebook 06 and the validated simulated Inventory Snapshot dataset.

---

## 8. Productization and Delivery Stage Sequence

### Stage 8 — Dashboard Data Preparation

**Status:** Not Started

**Purpose:**  
Create compact, validated datasets specifically designed for Streamlit and Power BI.

**Planned outputs:**

- `data/dashboard/kpi_summary.csv`;
- `data/dashboard/sales_trends.csv`;
- `data/dashboard/forecast_dashboard.csv`;
- `data/dashboard/inventory_dashboard.csv`;
- `data/dashboard/risk_dashboard.csv`;
- `data/dashboard/product_details.csv`;
- `data/dashboard/recommendations.csv`.

**Completion criteria:**

- dashboard files are smaller than modelling datasets;
- each table has a clearly defined grain;
- key fields are unique where required;
- KPI values reconcile with notebook outputs;
- all dashboard files can be regenerated through code.

**Depends on:**  
Notebook 07.

---

### Stage 9 — Streamlit Planning Application

**Status:** Not Started

**Purpose:**  
Provide an interactive planning tool for non-technical business users.

**Planned pages:**

1. Home
2. Sales Analytics
3. Forecast
4. Inventory Dashboard
5. Risk Dashboard
6. Product Details
7. Executive Summary

**Required functionality:**

- headline KPI cards;
- date filters;
- category and department filters;
- state and store filters;
- SKU filters;
- sales-trend charts;
- actual-versus-forecast charts;
- forecast-confidence indicators;
- inventory-health views;
- stockout and overstock flags;
- prioritised reorder recommendations;
- prioritised markdown recommendations;
- downloadable results;
- clear loading, empty, and error states.

**Completion criteria:**

A non-technical user must be able to answer:

- What is selling?
- Which SKUs may stock out?
- Which SKUs are overstocked?
- What should be reordered?
- What should be marked down?
- What is the estimated financial value at stake?

**Depends on:**  
Stage 8.

---

### Stage 10 — FastAPI Scoring Service

**Status:** Not Started

**Purpose:**  
Expose forecasts, risks, and recommendations through a lightweight service.

**Planned endpoints:**

- `GET /`;
- `GET /health`;
- `GET /products`;
- `GET /forecast/{sku_id}`;
- `GET /risk/{sku_id}`;
- `GET /recommendations`;
- `POST /predict`.

**Required functionality:**

- input validation;
- clear request and response schemas;
- model and preprocessing loading;
- graceful handling of invalid SKU identifiers;
- documented example requests;
- documented example responses;
- interactive API documentation;
- health checking.

**Completion criteria:**

- the service returns forecasts and risks for valid inputs;
- invalid inputs do not crash the application;
- endpoint responses are documented;
- the service is reachable through a public URL.

**Depends on:**  
Notebook 06, Notebook 07, and validated model files.

---

### Stage 11 — Power BI Business Intelligence Report

**Status:** Not Started

**Purpose:**  
Create a consulting-style management report for executive monitoring and business analysis.

**Planned pages:**

1. Executive Dashboard
2. Sales Analytics
3. Product Performance
4. Category Performance
5. Inventory
6. Stockout Risk
7. Overstock
8. Promotion
9. Seasonality
10. Forecast
11. Business Insights
12. Executive Recommendations

**Role of Power BI:**

- executive KPI reporting;
- drill-down analysis;
- management storytelling;
- interactive business monitoring;
- portfolio presentation.

**Priority rule:**

Power BI is a portfolio enhancement. It must not delay the mandatory Streamlit application, scoring service, forecasting, or risk-scoring deliverables.

**Depends on:**  
Stage 8 and completed analytical outputs.

---

### Stage 12 — Testing and Deployment

**Status:** Not Started

**Purpose:**  
Confirm that the project works outside the development notebook environment.

**Planned deployment targets:**

- Streamlit application: Streamlit Community Cloud;
- FastAPI service: Render;
- alternative deployment platform: Hugging Face Spaces, where appropriate.

**Testing requirements:**

- data-file existence checks;
- schema-validation tests;
- forecast-metric tests;
- risk-rule tests;
- API endpoint tests;
- dashboard smoke tests;
- missing-file tests;
- invalid-input tests;
- deployment startup tests.

**Deployment requirements:**

- relative project paths;
- documented environment dependencies;
- no hard-coded local paths;
- no committed secrets;
- no large raw-data uploads to GitHub;
- tested public URLs;
- clear startup and troubleshooting instructions.

**Completion criteria:**

- the Streamlit URL works publicly;
- the FastAPI URL works publicly;
- the project installs from `requirements.txt`;
- important outputs reproduce consistently;
- applications start without manual code changes.

**Depends on:**  
Stages 9 and 10.

---

### Stage 13 — Final Documentation

**Status:** In Progress

**Purpose:**  
Document the project so that another person can understand, reproduce, evaluate, and use it.

**Planned documentation:**

- `README.md`;
- `docs/project_roadmap.md`;
- `docs/development_scope.md`;
- `docs/decision_log.md`;
- `docs/assumptions_limitations.md`;
- `docs/data_dictionary.md`;
- `docs/feature_dictionary.md`;
- `docs/modelling_methodology.md`;
- `docs/evaluation_methodology.md`;
- `docs/risk_scoring_methodology.md`;
- `docs/model_card.md`;
- `docs/dashboard_user_guide.md`;
- `docs/api_documentation.md`;
- `docs/deployment_guide.md`;
- `docs/business_recommendations.md`.

**Documentation rule:**

Documentation will be updated gradually as each stage is completed. It must describe actual project results rather than planned or assumed results.

**Completion criteria:**

A reviewer must be able to understand:

- the business problem;
- the data sources;
- the project adaptation;
- the analytical scope;
- the modelling approach;
- the evaluation results;
- the risk logic;
- the assumptions and limitations;
- how to run and use the project.

---

### Stage 14 — Executive Communication

**Status:** Not Started

**Purpose:**  
Present the project in clear business language for Operations and Finance stakeholders.

**Planned outputs:**

- Data-Quality and EDA Insight Memo;
- 6–10 slide executive presentation;
- business recommendations;
- final rupee-impact summary;
- 3–5 minute demonstration video.

**Planned presentation structure:**

1. Project title and client context
2. Business problem and objectives
3. Data and solution architecture
4. Data engineering and assumptions
5. EDA insights
6. Forecasting methodology
7. Model performance
8. Risk scoring and recommended actions
9. Dashboard and deployment
10. Financial impact and final recommendations

**Communication standards:**

- lead with business impact and recommended actions;
- explain accuracy honestly;
- clearly disclose assumptions and limitations;
- avoid unexplained technical language;
- use charts readable by non-technical users.

**Depends on:**  
All analytical, modelling, risk, and deployment stages.

---

### Stage 15 — Final Submission

**Status:** Not Started

**Purpose:**  
Package and submit every required project deliverable.

**Required submission items:**

- Git repository;
- live Streamlit application URL;
- live scoring-service URL;
- complete README;
- Data-Quality and EDA Insight Memo;
- executive readout;
- 3–5 minute demo video;
- completed submission form containing all links.

**Final quality checks:**

- repository structure is clean;
- no unnecessary files are committed;
- no private information or secrets are exposed;
- notebooks run in the correct order;
- README commands are tested;
- public links are accessible;
- final metrics match notebook results;
- assumptions and limitations are visible;
- required deliverables are not missing.

**Depends on:**  
Stages 0–14.

---

### Stage 16 — Resume, LinkedIn, and Interview Preparation

**Status:** Not Started

**Purpose:**  
Convert the completed technical project into professional career materials.

**Planned outputs:**

- ATS-friendly resume project entry;
- LinkedIn project description;
- LinkedIn completion post;
- GitHub repository summary;
- portfolio screenshots;
- 30-second project pitch;
- two-minute project explanation;
- detailed interview walkthrough;
- technical interview questions and answers;
- business interview questions and answers.

**Priority rule:**

Career packaging begins only after the core Zidio submission is technically complete and verified.

**Depends on:**  
Stage 15.

---

## 9. Locked Forecasting Decisions

The following forecasting decisions are fixed for the initial Project FORESIGHT implementation.

| Decision | Locked Choice |
|---|---|
| **Forecast grain** | Weekly SKU-store level |
| **Development population** | 300 SKU-store series |
| **Forecast horizon** | Eight weeks |
| **Primary metric** | WAPE |
| **Secondary metric** | Forecast Bias |
| **Supporting metrics** | MAE and RMSE |
| **Required baseline** | Seasonal-naive forecast |
| **Additional baselines** | Naive and four-week moving average |
| **Validation method** | Rolling-origin cross-validation |
| **Final evaluation period** | Latest untouched eight-week period |
| **Leakage policy** | Features may use only information available before the forecast origin |
| **Primary machine-learning model** | LightGBM |
| **Secondary machine-learning model** | XGBoost |
| **Optional benchmark** | Random Forest |
| **Model-selection rule** | Advanced models must be compared fairly against seasonal-naive |

### 9.1 Forecasting Principles

The forecasting workflow must:

- preserve chronological order;
- avoid random train-test splitting;
- use identical validation windows for competing models;
- report WAPE and Bias for every major model;
- evaluate overall and SKU-level performance;
- retain the seasonal-naive forecast where advanced models do not improve performance;
- document poor performance rather than hiding it;
- save all final model decisions and evaluation outputs.

### 9.2 Forecasting Scope Protection

The following are not required for the initial core implementation:

- separate ARIMA models for every SKU-store series;
- separate Prophet models for every SKU-store series;
- deep-learning forecasting models;
- real-time forecasting;
- automatic model retraining;
- complex forecast reconciliation across multiple hierarchy levels.

These methods may be explored only after all mandatory deliverables are complete.

---

## 10. Locked Risk-Scoring Decisions

Risk scoring will combine final demand forecasts with the simulated inventory position.

### 10.1 Stockout Risk

Stockout risk will consider:

- forecast demand over the SKU lead-time period;
- available on-hand stock;
- on-order inventory;
- safety stock;
- projected ending inventory;
- forecast confidence;
- estimated lost-sales exposure.

### 10.2 Overstock Risk

Overstock risk will consider:

- current on-hand inventory;
- expected forward demand;
- days of supply;
- excess units;
- estimated inventory value;
- demand velocity;
- forecast confidence.

### 10.3 Final Business Classifications

| Classification | General Condition | Recommended Action |
|---|---|---|
| **Reorder Now** | High stockout risk and low overstock risk | Prioritise replenishment |
| **Healthy** | Low stockout risk and low overstock risk | No immediate action |
| **Overstock** | High overstock risk and low stockout risk | Reduce replenishment or consider markdown |
| **Watch** | High uncertainty, volatility, or conflicting risks | Review manually |

### 10.4 Required SKU-Level Outputs

Every development SKU must receive:

- final forecast;
- forecast-confidence level;
- stockout-risk score;
- overstock-risk score;
- business classification;
- recommended action;
- priority rank;
- estimated revenue at risk;
- estimated capital locked in excess inventory;
- recommended reorder quantity where applicable.

### 10.5 Transparency Rule

Risk scoring must remain explainable.

Every score and recommendation must be traceable to documented inputs, formulas, thresholds, and assumptions. Black-box classifications without visible business logic are not acceptable.

---

## 11. Locked Project Priority Order

### Tier 1 — Mandatory Core Work

1. Complete and audit the master roadmap.
2. Complete Notebook 02 and the EDA insight memo.
3. Complete Notebook 03 feature engineering.
4. Complete Notebook 04 baseline forecasting.
5. Complete Notebook 05 machine-learning forecasting.
6. Complete Notebook 06 model evaluation and selection.
7. Complete Notebook 07 inventory intelligence and risk scoring.
8. Prepare dashboard-ready datasets.
9. Build the Streamlit planning application.
10. Build the FastAPI scoring service.
11. Test and deploy the applications.
12. Complete the project documentation.
13. Prepare the executive readout.
14. Record the demonstration video.
15. Complete the final submission.

### Tier 2 — Portfolio Enhancements

The following begin only after the mandatory work is stable:

- Power BI report;
- SHAP or additional explainability;
- advanced dashboard controls;
- additional downloadable reports;
- extended automated testing;
- professional portfolio screenshots;
- resume, LinkedIn, and interview materials.

### Tier 3 — Optional Stretch Work

The following are optional:

- calibrated prediction intervals;
- lead-time what-if controls;
- model-monitoring plan;
- CI/CD;
- Docker;
- advanced forecast reconciliation;
- additional classical time-series demonstrations;
- automated retraining.

Optional work must never delay a mandatory Zidio deliverable.

---

## 12. Scope Protection Rules

To prevent unnecessary complexity, the project will follow these rules:

1. Complete mandatory work before optional enhancements.
2. Do not add a model only because it is popular.
3. Do not create a chart unless it answers a defined business question.
4. Do not create dashboard pages without a clear stakeholder purpose.
5. Do not use the complete 30,490-record SKU Master population for development-scope KPIs.
6. Do not describe simulated inventory values as observed retailer data.
7. Do not use future information in forecasting features.
8. Do not report an advanced model as successful unless it is evaluated fairly against the baseline.
9. Do not commit large raw datasets, secrets, or machine-specific paths to GitHub.
10. Do not begin career packaging before the technical submission is complete.

---

## 13. Change-Control Policy

This roadmap is a controlled living document.

### Locked Elements

The following should remain stable:

- official deliverables;
- development scope;
- seven-notebook architecture;
- weekly forecasting grain;
- eight-week forecast horizon;
- seasonal-naive baseline;
- WAPE as the primary metric;
- rolling-origin validation;
- leakage-prevention policy;
- transparent risk-scoring requirement;
- Streamlit and scoring-service deliverables.

### Updatable Elements

The following will be updated as evidence becomes available:

- stage status;
- completed checklists;
- actual output filenames;
- final feature list;
- selected forecasting model;
- model-performance results;
- forecast-confidence methodology;
- final risk thresholds;
- deployed URLs;
- business insights;
- financial-impact estimates;
- limitations discovered during development.

### Version Rule

- Minor factual or progress updates will increase the roadmap version from `3.0` to `3.1`, `3.2`, and so on.
- A major architecture change would require a new major version.
- Every important change must be recorded in `docs/decision_log.md`.

---

## 14. Stage-by-Stage Output Register

This register defines the main files expected from every project stage. Filenames may receive minor technical adjustments, but the purpose of each output must remain unchanged.

### 14.1 Stage 0 — Data Foundation

| Output | Location | Status |
|---|---|---|
| Data Engineering notebook | `notebooks/01_Data_Engineering_Validation.ipynb` | Completed |
| Notebook PDF | `reports/notebook_exports/01_Data_Engineering_Validation.pdf` | Completed |
| Final daily sales data | `data/processed/sales_daily_final.csv` | Completed |
| Final calendar data | `data/processed/calendar_final.csv` | Completed |
| Final SKU master | `data/processed/sku_master_final.csv` | Completed |
| Simulated inventory snapshots | `data/processed/inventory_snapshots_final.csv` | Completed |
| Development SKU scope | `data/processed/development_sku_scope.csv` | Completed |
| Pipeline runner | `run_data_pipeline.py` | Completed |
| Development-scope document | `docs/development_scope.md` | Completed |

---

### 14.2 Stage 1 — Roadmap and Governance

| Output | Location | Status |
|---|---|---|
| Master project roadmap | `docs/project_roadmap.md` | In Progress |
| Project decision log | `docs/decision_log.md` | Not Started |
| Assumptions and limitations | `docs/assumptions_limitations.md` | Not Started |
| Roadmap audit summary | `reports/tables/project_roadmap_audit.csv` | Not Started |

---

### 14.3 Stage 2 — Exploratory Data Analysis

| Output | Location | Status |
|---|---|---|
| EDA notebook | `notebooks/02_Exploratory_Data_Analysis.ipynb` | Not Started |
| Integrated daily analytical data | `data/interim/analytics_base_daily.parquet` | Not Started |
| Executive KPI summary | `reports/tables/eda_kpi_summary.csv` | Not Started |
| SKU performance summary | `reports/tables/sku_performance_summary.csv` | Not Started |
| Category performance summary | `reports/tables/category_performance_summary.csv` | Not Started |
| Store performance summary | `reports/tables/store_performance_summary.csv` | Not Started |
| Inventory EDA summary | `reports/tables/inventory_eda_summary.csv` | Not Started |
| EDA figures | `reports/figures/` | Not Started |
| EDA insight memo | `reports/executive_report/EDA_Insight_Memo.pdf` | Not Started |
| Notebook PDF | `reports/notebook_exports/02_Exploratory_Data_Analysis.pdf` | Not Started |

---

### 14.4 Stage 3 — Feature Engineering

| Output | Location | Status |
|---|---|---|
| Feature-engineering notebook | `notebooks/03_Forecasting_Feature_Engineering.ipynb` | Not Started |
| Weekly modelling dataset | `data/interim/weekly_features_final.parquet` | Not Started |
| Feature dictionary | `docs/feature_dictionary.md` | Not Started |
| Feature-validation summary | `reports/tables/feature_validation_summary.csv` | Not Started |
| Model feature list | `models/model_feature_list.json` | Not Started |
| Categorical feature list | `models/categorical_features.json` | Not Started |
| Notebook PDF | `reports/notebook_exports/03_Forecasting_Feature_Engineering.pdf` | Not Started |

---

### 14.5 Stage 4 — Baseline Forecasting

| Output | Location | Status |
|---|---|---|
| Baseline notebook | `notebooks/04_Baseline_Forecasting.ipynb` | Not Started |
| Baseline forecasts | `data/interim/baseline_forecasts.parquet` | Not Started |
| Overall baseline metrics | `reports/tables/baseline_model_metrics.csv` | Not Started |
| SKU-level baseline metrics | `reports/tables/baseline_sku_metrics.csv` | Not Started |
| Fold-level baseline metrics | `reports/tables/baseline_fold_metrics.csv` | Not Started |
| Champion baseline configuration | `models/champion_baseline_config.json` | Not Started |
| Notebook PDF | `reports/notebook_exports/04_Baseline_Forecasting.pdf` | Not Started |

---

### 14.6 Stage 5 — Machine-Learning Forecasting

| Output | Location | Status |
|---|---|---|
| Machine-learning notebook | `notebooks/05_Machine_Learning_Forecasting.ipynb` | Not Started |
| Machine-learning forecasts | `data/interim/ml_forecasts.parquet` | Not Started |
| Overall ML metrics | `reports/tables/ml_model_metrics.csv` | Not Started |
| SKU-level ML metrics | `reports/tables/ml_sku_metrics.csv` | Not Started |
| Fold-level ML metrics | `reports/tables/ml_fold_metrics.csv` | Not Started |
| Feature importance | `reports/tables/feature_importance.csv` | Not Started |
| LightGBM model | `models/lightgbm_model.pkl` | Not Started |
| XGBoost model | `models/xgboost_model.pkl` | Not Started |
| Preprocessing pipeline | `models/preprocessing_pipeline.pkl` | Not Started |
| Notebook PDF | `reports/notebook_exports/05_Machine_Learning_Forecasting.pdf` | Not Started |

---

### 14.7 Stage 6 — Model Evaluation and Selection

| Output | Location | Status |
|---|---|---|
| Model-evaluation notebook | `notebooks/06_Model_Evaluation_Selection.ipynb` | Not Started |
| Final forecasts | `data/processed/final_forecasts.csv` | Not Started |
| Model-comparison table | `reports/tables/model_comparison.csv` | Not Started |
| SKU forecast evaluation | `reports/tables/sku_forecast_evaluation.csv` | Not Started |
| Segment forecast evaluation | `reports/tables/segment_forecast_evaluation.csv` | Not Started |
| Forecast-confidence table | `reports/tables/forecast_confidence.csv` | Not Started |
| Champion-model decision | `models/champion_model_decision.json` | Not Started |
| Model card | `docs/model_card.md` | Not Started |
| Notebook PDF | `reports/notebook_exports/06_Model_Evaluation_Selection.pdf` | Not Started |

---

### 14.8 Stage 7 — Inventory Intelligence and Risk Scoring

| Output | Location | Status |
|---|---|---|
| Risk-scoring notebook | `notebooks/07_Inventory_Intelligence_Risk_Scoring.ipynb` | Not Started |
| Inventory risk scores | `data/processed/inventory_risk_scores.csv` | Not Started |
| Reorder recommendations | `data/processed/reorder_recommendations.csv` | Not Started |
| Markdown recommendations | `data/processed/markdown_recommendations.csv` | Not Started |
| Dashboard master dataset | `data/dashboard/dashboard_master_dataset.csv` | Not Started |
| Executive inventory KPIs | `data/dashboard/executive_inventory_kpis.csv` | Not Started |
| Decisioning grid | `reports/tables/decisioning_grid.csv` | Not Started |
| Risk-scoring methodology | `docs/risk_scoring_methodology.md` | Not Started |
| Notebook PDF | `reports/notebook_exports/07_Inventory_Intelligence_Risk_Scoring.pdf` | Not Started |

---

### 14.9 Productization and Final Delivery

| Output | Location | Status |
|---|---|---|
| Streamlit application | `streamlit_app/` | Not Started |
| FastAPI service | `api/` | Not Started |
| Power BI report | `dashboard/` | Not Started |
| Automated tests | `tests/` | Not Started |
| Executive presentation | `presentation/` | Not Started |
| Final executive report | `reports/executive_report/` | Not Started |
| Deployment guide | `docs/deployment_guide.md` | Not Started |
| Dashboard user guide | `docs/dashboard_user_guide.md` | Not Started |
| API documentation | `docs/api_documentation.md` | Not Started |
| Final business recommendations | `docs/business_recommendations.md` | Not Started |

---

## 15. Project Definition of Done

Project FORESIGHT will be considered technically complete only when all mandatory conditions below are satisfied.

### 15.1 Data Foundation

- [x] Raw source files are stored in the correct project folder.
- [x] Data cleaning and transformation are performed through code.
- [x] Processed datasets are validated.
- [x] The pipeline runs from one command.
- [x] Development scope is documented.
- [x] Simulated inventory data is clearly disclosed.
- [x] The Phase 0 audit passes without failure.

### 15.2 Exploratory Data Analysis

- [ ] Demand trend and seasonality are analysed.
- [ ] Category, department, store, state, product, and SKU performance are analysed.
- [ ] Top-moving products are identified.
- [ ] Slow-moving and dead-stock candidates are identified.
- [ ] Pricing and promotion relationships are examined.
- [ ] Event and SNAP effects are examined.
- [ ] Simulated inventory health is analysed.
- [ ] Charts are labelled and readable.
- [ ] Every major chart has a business interpretation.
- [ ] At least three decision-relevant insights are documented.
- [ ] The EDA insight memo is exported.

### 15.3 Feature Engineering

- [ ] Weekly modelling grain is validated.
- [ ] Lag features are created.
- [ ] Rolling features are created.
- [ ] Calendar and seasonal features are created.
- [ ] Pricing and promotion features are created.
- [ ] Event and SNAP features are created.
- [ ] Demand variability features are created.
- [ ] Feature availability is checked at every forecast origin.
- [ ] Leakage audit passes.
- [ ] Feature dictionary is completed.

### 15.4 Forecasting

- [ ] Forecast horizon is fixed at eight weeks.
- [ ] WAPE is used as the primary evaluation metric.
- [ ] Forecast Bias is reported.
- [ ] Seasonal-naive baseline is implemented.
- [ ] Rolling-origin validation is implemented.
- [ ] Machine-learning models use the same validation windows.
- [ ] Baseline and advanced models are compared fairly.
- [ ] Final untouched holdout performance is reported.
- [ ] Poor-performing SKU segments are disclosed.
- [ ] Champion-model decision is documented.
- [ ] Final forecast dataset is exported.

### 15.5 Inventory Intelligence

- [ ] Every development SKU receives a stockout-risk score.
- [ ] Every development SKU receives an overstock-risk score.
- [ ] Every development SKU receives a business classification.
- [ ] Every development SKU receives a recommended action.
- [ ] Reorder quantities are calculated where applicable.
- [ ] Markdown candidates are identified.
- [ ] Revenue at risk is estimated.
- [ ] Capital locked in excess inventory is estimated.
- [ ] Decisioning logic is transparent.
- [ ] Risk-scoring methodology is documented.

### 15.6 Dashboard and Service

- [ ] Dashboard-ready datasets are validated.
- [ ] Streamlit application loads successfully.
- [ ] Streamlit filters work correctly.
- [ ] Actual-versus-forecast charts are available.
- [ ] Risk flags and recommendations are visible.
- [ ] Invalid and empty states are handled.
- [ ] FastAPI endpoints return valid responses.
- [ ] Invalid API inputs are handled gracefully.
- [ ] Interactive API documentation is available.
- [ ] Public deployment links work.

### 15.7 Documentation and Submission

- [ ] README contains the business problem and project overview.
- [ ] README contains setup and reproduction instructions.
- [ ] README contains final WAPE versus baseline.
- [ ] Assumptions and limitations are clearly disclosed.
- [ ] Data and feature dictionaries are available.
- [ ] Model card is completed.
- [ ] Dashboard and API guides are completed.
- [ ] Executive readout is completed.
- [ ] EDA insight memo is completed.
- [ ] Demo video is recorded.
- [ ] Repository is clean and reproducible.
- [ ] Final submission form contains all required links.

---

## 16. Final Quality Standard

The project must demonstrate more than code execution.

A strong final submission must show:

- reproducible data engineering;
- business-focused exploratory analysis;
- leakage-safe forecasting;
- honest baseline comparison;
- transparent inventory-risk logic;
- actionable recommendations;
- financial impact estimates;
- usable stakeholder tools;
- clear documentation;
- professional communication.

Project FORESIGHT is not complete merely because the notebooks run. It is complete only when the outputs are trustworthy, reproducible, understandable, and useful for inventory decision-making.

---

## 17. Project Governance and Progress Tracking

### 17.1 Stage Status Values

Every project stage must use one of the following status values:

| Status | Meaning |
|---|---|
| **Not Started** | Work has not begun |
| **In Progress** | Work is actively being completed |
| **Blocked** | Work **In Progress** | Work is cannot continue because of a documented issue |
| **Under Review** | Work is complete but still being validated |
| **Completed** | All completion criteria have passed |
| **Locked** | The completed work has been formally accepted and should not change without approval |

A stage must not be marked **Completed** merely because its notebook runs. Its required outputs, validations, documentation, and business conclusions must also be finished.

---

### 17.2 Stage Completion Procedure

At the end of every major stage, the following procedure will be followed:

1. Save the notebook or project files.
2. Restart the notebook kernel where appropriate.
3. Run the stage from beginning to end.
4. Confirm that all required outputs were created.
5. Validate row counts, schemas, keys, and important calculations.
6. Review charts, tables, and business interpretations.
7. Export the final notebook PDF.
8. Update the relevant documentation.
9. Update the roadmap status and checklist.
10. Record important decisions in `docs/decision_log.md`.
11. Record newly discovered assumptions or limitations.
12. Mark the stage as completed only after all checks pass.

---

### 17.3 Notebook Completion Standard

Every final notebook should contain:

- a professional title page;
- project and notebook information;
- a clear business objective;
- concise section introductions;
- reproducible code;
- clear variable names;
- validated data inputs;
- labelled charts;
- observations;
- business insights;
- business recommendations where relevant;
- exported outputs;
- a final validation section;
- a notebook conclusion;
- a final PDF export.

Notebook markdown must remain concise, professional, business-oriented, and suitable for GitHub, recruiters, mentors, and interview discussion.

---

### 17.4 Validation Standard

Validation must be performed at four levels.

#### Data Validation

- expected files exist;
- required columns exist;
- data types are correct;
- key fields are non-null;
- key fields are unique where required;
- row counts are reasonable;
- date ranges are correct;
- development scope is preserved.

#### Analytical Validation

- KPI calculations reconcile;
- aggregation levels are correct;
- charts use the intended population;
- percentages use appropriate denominators;
- observations match displayed results;
- simulated and observed values are clearly separated.

#### Modelling Validation

- features do not contain future information;
- chronological order is preserved;
- validation folds are reproducible;
- all models use comparable test periods;
- metrics are calculated consistently;
- final holdout data remains untouched until model selection is complete.

#### Product Validation

- dashboard filters work;
- API inputs are validated;
- error and empty states are handled;
- displayed metrics match notebook outputs;
- applications start from a clean environment;
- public links remain reachable.

---

### 17.5 Decision Logging Rule

The following decisions must be recorded in `docs/decision_log.md`:

- changes to project scope;
- changes to notebook responsibilities;
- changes to forecast grain or horizon;
- changes to evaluation metrics;
- changes to development population;
- addition or removal of major models;
- champion-model selection;
- risk-threshold decisions;
- dashboard architecture decisions;
- deployment-platform decisions;
- changes caused by technical limitations.

Each decision entry must include:

- date;
- decision identifier;
- decision made;
- reason;
- alternatives considered;
- expected impact;
- person responsible.

---

### 17.6 Assumption and Limitation Logging Rule

The file `docs/assumptions_limitations.md` must be updated whenever the project:

- simulates unavailable information;
- estimates costs or margins;
- creates lead-time assumptions;
- defines inventory policies;
- excludes unavailable variables;
- restricts analysis to the development scope;
- discovers data-quality limitations;
- identifies forecasting weaknesses;
- encounters deployment constraints.

Assumptions must never be presented as observed facts.

---

### 17.7 Roadmap Review Points

The roadmap will be reviewed after:

- completion of Notebook 02;
- completion of Notebook 03;
- completion of the baseline forecast;
- final model selection;
- completion of risk scoring;
- dashboard completion;
- deployment;
- final submission.

At each review, only factual progress, validated outputs, results, limitations, and approved technical changes should be updated.

The overall architecture must remain stable unless a documented technical reason requires modification.

---

## 18. Roadmap Acceptance Checklist

The master roadmap can be formally locked only when all statements below are true.

- [x] The project objective is documented.
- [x] The official client deliverables are documented.
- [x] The M5 adaptation is clearly disclosed.
- [x] The 300 SKU-store development scope is documented.
- [x] The complete end-to-end architecture is documented.
- [x] All seven notebook responsibilities are defined.
- [x] Productization stages are defined.
- [x] Deployment requirements are defined.
- [x] Documentation and submission stages are defined.
- [x] Forecast grain and horizon are fixed.
- [x] Evaluation metrics are fixed.
- [x] Baseline requirements are fixed.
- [x] Validation methodology is fixed.
- [x] Risk-scoring principles are documented.
- [x] Mandatory and optional work are separated.
- [x] Expected project outputs are registered.
- [x] The complete definition of done is documented.
- [x] Change-control rules are documented.
- [x] Decision-logging rules are documented.
- [x] Assumption-logging rules are documented.
- [x] Roadmap file has passed the final structural audit.
- [x] Document status has been changed from `In Progress` to `Locked`.

---

## 19. Roadmap Lock Declaration

After the final structural audit passes, this roadmap will become:

```text
Project FORESIGHT — Master Roadmap
Version: 3.0
Status: Locked