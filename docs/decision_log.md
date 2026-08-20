# Project FORESIGHT — Decision Log

## Document Control

| Item | Details |
|---|---|
| **Project** | Project FORESIGHT |
| **Author** | Mohit Kumar |
| **Internship** | Zidio Development |
| **Document Version** | 1.1 |
| **Status** | Active |
| **Created** | 2 August 2026 |
| **Last Updated** | 21 August 2026 |

---

## 1. Purpose

This decision log records important technical, analytical, modelling, product, deployment, and governance decisions made throughout Project FORESIGHT.

It provides a clear explanation of:

- what decision was made;
- why the decision was required;
- which alternatives were considered;
- how the decision affects the project;
- who is responsible for the decision.

The log supports project reproducibility, transparency, and controlled roadmap updates.

---

## 2. Decision Status Values

| Status | Meaning |
|---|---|
| **Proposed** | The decision is still being considered |
| **Approved** | The decision has been accepted for implementation |
| **Implemented** | The approved decision has been applied |
| **Revised** | The original decision has been changed or superseded |
| **Retired** | The decision is no longer applicable |

---

## 3. Decision Entry Structure

Every major decision should include:

- decision identifier;
- date;
- project stage;
- decision status;
- decision made;
- reason;
- alternatives considered;
- expected project impact;
- person responsible;
- related files or outputs.

---

## 4. Project Decisions

### DEC-001 — Adapt the Zidio Brief Using M5 Data

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Data Foundation |
| **Status** | Implemented |
| **Decision** | Use the public M5 dataset as the primary source for Project FORESIGHT while preserving the business objectives of the Zidio engagement brief. |
| **Reason** | The required business problem involves retail demand forecasting and inventory intelligence. The M5 data provides detailed historical sales, calendar, event, SNAP, and pricing information suitable for this purpose. |
| **Alternatives Considered** | Generate a completely synthetic dataset; locate another retail dataset; reduce the project to sales analysis only. |
| **Expected Impact** | The project gains realistic retail sales history and hierarchy while requiring clear disclosure that it is an adaptation rather than observed NorthBay Living data. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `docs/project_roadmap.md`, `notebooks/01_Data_Engineering_Validation.ipynb` |

---

### DEC-002 — Simulate Inventory Snapshot Data

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Data Foundation |
| **Status** | Implemented |
| **Decision** | Create a simulated Inventory Snapshot dataset because the M5 source files do not contain stock balances, purchase orders, receipts, lead times, or observed stockout records. |
| **Reason** | Inventory-risk scoring requires an inventory position that can be combined with future demand forecasts. |
| **Alternatives Considered** | Exclude inventory intelligence; use sales quantities as inventory; search for an unrelated external inventory dataset. |
| **Expected Impact** | Stockout, overstock, reorder, and financial-exposure results will be analytical estimates and must not be presented as observed retailer outcomes. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `data/processed/inventory_snapshots_final.csv`, `docs/assumptions_limitations.md` |

---

### DEC-003 — Restrict Development to 300 SKU-Store Series

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Data Foundation |
| **Status** | Implemented |
| **Decision** | Use 300 SKU-store series, representing 30 products across 10 stores, for the analytical, modelling, risk-scoring, and dashboard development workflow. |
| **Reason** | The complete M5 population is computationally large for an internship-scale end-to-end project. A controlled representative scope supports detailed analysis, repeatable modelling, and practical application development. |
| **Alternatives Considered** | Use all 30,490 SKU-store records; analyse only one store; select a very small demonstration sample. |
| **Expected Impact** | Development becomes computationally manageable while KPI calculations must consistently use `development_sku_scope.csv`. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `data/processed/development_sku_scope.csv`, `docs/development_scope.md` |

---

### DEC-004 — Use a Seven-Notebook Analytical Architecture

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Roadmap and Governance |
| **Status** | Implemented |
| **Decision** | Organise the main analytical workflow into seven sequential notebooks covering data engineering, EDA, feature engineering, baseline forecasting, machine-learning forecasting, model evaluation, and inventory-risk scoring. |
| **Reason** | Separating responsibilities makes the project easier to understand, validate, reproduce, review, and explain during interviews. |
| **Alternatives Considered** | Use one large notebook; use only three broad notebooks; place all logic directly inside Python scripts. |
| **Expected Impact** | Each notebook has a clear responsibility and uses validated outputs from the preceding stage. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `docs/project_roadmap.md`, `notebooks/` |

---

### DEC-005 — Forecast at Weekly SKU-Store Level

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Forecasting Design |
| **Status** | Implemented |
| **Decision** | Produce demand forecasts at the weekly SKU-store level. |
| **Reason** | Daily SKU demand can be sparse and volatile. Weekly aggregation provides a more stable planning grain while preserving product and store-level detail for inventory decisions. |
| **Alternatives Considered** | Daily SKU-store forecasts; monthly forecasts; category-level forecasts; national product-level forecasts. |
| **Expected Impact** | Daily sales data is aggregated into weekly observations during the feature-engineering workflow. Forecasts and evaluation results remain specific to each SKU-store series. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/03_Feature_Engineering.ipynb`, `data/modeling/weekly_features_final.csv` |

---

### DEC-006 — Use an Eight-Week Forecast Horizon

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Forecasting Design |
| **Status** | Implemented |
| **Decision** | Use an eight-week demand forecast horizon for the initial project implementation. |
| **Reason** | An eight-week horizon is suitable for medium-term inventory planning and falls within the six-to-eight-week range described in the engagement scope. |
| **Alternatives Considered** | Four-week horizon; six-week horizon; twelve-week horizon; multiple independent forecast horizons. |
| **Expected Impact** | Baselines, machine-learning models, rolling-origin validation, final forecasts, and inventory-risk calculations use the same eight-week horizon. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/04_Baseline_Forecasting.ipynb`, `notebooks/05_Machine_Learning_Forecasting.ipynb`, `data/processed/production_outputs/06_production_forecast_config.json` |

---

### DEC-007 — Use WAPE as the Primary Forecast Metric

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Forecast Evaluation |
| **Status** | Implemented |
| **Decision** | Use Weighted Absolute Percentage Error, or WAPE, as the primary model-evaluation metric. |
| **Reason** | WAPE evaluates total absolute forecast error relative to total actual demand and is suitable for comparing performance across series with different sales volumes. |
| **Alternatives Considered** | MAPE; sMAPE; MAE; RMSE; MASE. |
| **Expected Impact** | Major models report WAPE using the same evaluation periods and calculation method. Forecast Bias is used as a secondary metric, with MAE and RMSE as supporting metrics. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/04_Baseline_Forecasting.ipynb`, `notebooks/06_Model_Evaluation.ipynb`, `reports/tables/06_model_comparison_scorecard.csv` |

---

### DEC-008 — Use Rolling-Origin Cross-Validation

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Forecast Evaluation |
| **Status** | Implemented |
| **Decision** | Evaluate forecasting models using rolling-origin cross-validation while preserving chronological order. |
| **Reason** | Forecasting models must be evaluated on future periods using only information that would have been available at each forecast origin. Random splitting would break time order and could produce misleading results. |
| **Alternatives Considered** | Random train-test split; one fixed historical split; evaluation on the training period. |
| **Expected Impact** | Baseline and machine-learning models use comparable chronological validation procedures. Future information must never enter training features. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/04_Baseline_Forecasting.ipynb`, `notebooks/05_Machine_Learning_Forecasting.ipynb`, `notebooks/06_Model_Evaluation.ipynb` |

---

### DEC-009 — Protect the Latest Eight Weeks as the Final Holdout

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Forecast Evaluation |
| **Status** | Implemented |
| **Decision** | Reserve the latest eight-week period as an untouched final holdout dataset. |
| **Reason** | The final holdout provides an unbiased estimate of how the selected forecasting approach performs on data not used for feature design, model tuning, or champion selection. |
| **Alternatives Considered** | Use all available dates during model development; use a random holdout; repeatedly evaluate against the final period during tuning. |
| **Expected Impact** | The final holdout remains unused until model development and selection decisions are complete. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/03_Feature_Engineering.ipynb`, `notebooks/06_Model_Evaluation.ipynb`, `data/processed/production_outputs/06_production_forecast_config.json` |

---

### DEC-010 — Require a Seasonal-Naive Baseline

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Baseline Forecasting |
| **Status** | Revised |
| **Decision** | Require a simple, transparent statistical baseline as the mandatory benchmark against which more advanced forecasting models are evaluated. The final production baseline is the damped-trend exponential-smoothing model selected through the completed baseline workflow. |
| **Reason** | Retail demand commonly contains recurring patterns and trends. A transparent baseline provides a meaningful benchmark for determining whether a more complex model adds genuine value. |
| **Alternatives Considered** | Use only a simple naive forecast; compare models without a formal baseline; use average demand as the only benchmark. |
| **Expected Impact** | Advanced models must demonstrate measurable value against a validated baseline before being considered for production. The final locked baseline is documented in `04_champion_baseline_config.json`. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/04_Baseline_Forecasting.ipynb`, `data/processed/baseline_outputs/04_champion_baseline_config.json` |

---

### DEC-011 — Use LightGBM and XGBoost as the Main Machine-Learning Models

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Machine-Learning Forecasting |
| **Status** | Implemented |
| **Decision** | Use LightGBM as the primary machine-learning forecasting model and evaluate it against the established baseline under the same forecasting and validation framework. XGBoost was considered as a secondary machine-learning approach during the modelling design. |
| **Reason** | Gradient-boosting models can handle nonlinear relationships, lag variables, rolling statistics, pricing information, calendar effects, promotions, categorical features, and multiple SKU-store series within a global forecasting framework. |
| **Alternatives Considered** | Train separate ARIMA or Prophet models for every series; use deep learning; use only Random Forest; use a single machine-learning model without comparison. |
| **Expected Impact** | Notebook 05 provides the machine-learning forecasting workflow and produces the ML outputs used during model evaluation. The ML model is not automatically promoted to production and must satisfy the final selection rules. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/05_Machine_Learning_Forecasting.ipynb`, `data/processed/ml_outputs/05_champion_ml_config.json`, `data/processed/ml_outputs/05_ml_forecasts.csv` |

---

### DEC-012 — Permit a Baseline or Hybrid Champion

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Model Evaluation and Selection |
| **Status** | Revised |
| **Decision** | Allow the final forecasting solution to use the validated baseline or a machine-learning approach depending on objective final-test performance and predefined selection guardrails. |
| **Reason** | One model should not be promoted simply because it is more complex. Honest model selection requires the production choice to be supported by final-test evidence and business-relevant guardrails. |
| **Alternatives Considered** | Always select LightGBM; always use one global machine-learning champion; hide SKU segments where machine learning performs poorly. |
| **Expected Impact** | The final production forecaster is selected through an explicit and reproducible decision rule. The current locked outcome retains the baseline because the ML model did not meet the required improvement and guardrail conditions. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/06_Model_Evaluation.ipynb`, `data/processed/production_outputs/06_production_forecast_config.json`, `reports/tables/06_model_comparison_scorecard.csv` |

---

### DEC-013 — Use Transparent Rule-Based Inventory Risk Scoring

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Inventory Intelligence |
| **Status** | Implemented |
| **Decision** | Calculate stockout and overstock risks using transparent business rules that combine forecasts, inventory position, demand coverage, and related planning indicators. |
| **Reason** | Operations users must understand why a SKU receives a risk classification and recommended action. Explainable rules are more suitable than an unexplained black-box classification model for the initial implementation. |
| **Alternatives Considered** | Train a black-box risk classifier; show forecasts without recommendations; assign risk labels manually. |
| **Expected Impact** | Every risk score, classification, and recommended action is traceable to documented scoring logic and assumptions. Because inventory and cost inputs are simulated or estimated, resulting financial exposure values are treated as illustrative. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/07_Inventory_Intelligence.ipynb`, `data/processed/inventory_outputs/07_risk_scores.csv`, `data/processed/inventory_outputs/07_risk_scoring_config.json`, `docs/assumptions_limitations.md` |

---

### DEC-014 — Use Streamlit as the Mandatory Planning Application

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Productization |
| **Status** | Revised |
| **Decision** | Build Streamlit as the primary stakeholder-facing planning dashboard for Project FORESIGHT. |
| **Reason** | Streamlit supports rapid development of interactive analytical applications using Python and is suitable for presenting forecasts, risks, filters, recommendations, and downloadable outputs. |
| **Alternatives Considered** | Use only Power BI; provide notebook outputs without an application; build a custom web interface. |
| **Expected Impact** | Streamlit remains the mandatory stakeholder-facing application. The final implementation uses five navigation areas: Home, Forecast, Inventory & Risk, Product Details, and Executive Summary. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `streamlit_app/app.py`, `docs/project_roadmap.md` |

---

### DEC-015 — Use FastAPI for the Scoring Service

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Productization |
| **Status** | Implemented |
| **Decision** | Build a lightweight FastAPI service that exposes the project's scoring and analytical outputs through documented API endpoints. |
| **Reason** | FastAPI provides input validation, structured response schemas, automatic API documentation, and a professional method for serving analytical results. |
| **Alternatives Considered** | Expose results only through Streamlit; use Flask; omit the scoring service. |
| **Expected Impact** | The project includes a separately deployable API service with documented endpoints and structured responses. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `api/main.py`, `README.md` |

---

### DEC-016 — De-scope Power BI from the Mandatory Submission

| Field | Details |
|---|---|
| **Date** | 21 August 2026 |
| **Stage** | Business Intelligence |
| **Status** | Revised |
| **Decision** | Power BI is removed from the mandatory Project FORESIGHT submission scope and retained only as an optional future portfolio enhancement. |
| **Reason** | The mandatory analytical, forecasting, inventory-intelligence, dashboard, API, deployment, documentation, and executive communication requirements are already substantially complete. Continuing Power BI development at this stage could delay final submission without materially improving the core deliverables. |
| **Alternatives Considered** | Complete Power BI before submission; replace Streamlit with Power BI; maintain Power BI as a mandatory deliverable; postpone Power BI until after submission. |
| **Expected Impact** | Streamlit remains the primary stakeholder-facing planning application. Power BI will not block project completion and may be developed later as a separate portfolio enhancement. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `docs/project_roadmap.md`, `docs/decision_log.md`, `README.md` |

---

### DEC-017 — Use a One-Command Reproducible Pipeline

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Data Foundation |
| **Status** | Implemented |
| **Decision** | Use `run_data_pipeline.py` as the primary command for reproducing the data-engineering workflow and validating its generated outputs. |
| **Reason** | A professional project should not depend entirely on manually opening notebooks and executing individual cells to recreate essential datasets. |
| **Alternatives Considered** | Run Notebook 01 manually; execute separate scripts for each dataset; provide only previously exported files. |
| **Expected Impact** | A reviewer can use the project pipeline to reproduce the core data-engineering workflow from the project root, subject to the availability of the source data and required dependencies. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `run_data_pipeline.py`, `notebooks/01_Data_Engineering_Validation.ipynb` |

---

### DEC-018 — Maintain a Controlled Living Roadmap

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Roadmap and Governance |
| **Status** | Implemented |
| **Decision** | Maintain `project_roadmap.md` as a controlled living document whose architecture remains locked while validated progress, results, outputs, and limitations may be updated. |
| **Reason** | The project requires a stable development sequence while still allowing factual updates as work is completed. |
| **Alternatives Considered** | Never update the roadmap; rewrite the roadmap freely during development; track progress only through conversation history. |
| **Expected Impact** | Major architectural changes require a documented decision, while minor factual updates may increase the roadmap version from 3.0 to 3.1, 3.2, and so on. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `docs/project_roadmap.md`, `docs/decision_log.md` |

---

### DEC-019 — Protect Mandatory Deliverables from Optional Work

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Project Governance |
| **Status** | Implemented |
| **Decision** | Complete forecasting, risk scoring, Streamlit, FastAPI, deployment, documentation, executive communication, and final submission before optional enhancements receive priority. |
| **Reason** | Additional models, advanced dashboards, Power BI, explainability, Docker, and other enhancements can consume time without satisfying missing core deliverables. |
| **Alternatives Considered** | Develop optional features alongside unfinished mandatory work; prioritise visual polish before modelling; attempt every possible technology. |
| **Expected Impact** | Optional work may be postponed or removed whenever it threatens the quality or completion of the required Zidio deliverables. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `docs/project_roadmap.md` |

---

### DEC-020 — Retire Unused Dashboard-Ready Dataset Directory

| Field | Details |
|---|---|
| **Date** | 21 August 2026 |
| **Stage** | Dashboard Data Preparation |
| **Status** | Retired |
| **Decision** | Retire the planned `data/dashboard/` dataset layer because the directory was empty and was not required by the final Streamlit or FastAPI implementation. |
| **Reason** | The final applications do not depend on a dedicated `data/dashboard/` directory. Maintaining an unused directory and documenting it as an active project dependency would create unnecessary repository complexity and could cause confusion during review. |
| **Alternatives Considered** | Keep the empty directory; populate it with duplicate dashboard datasets; continue using the planned dashboard-data architecture. |
| **Expected Impact** | `data/dashboard/` is not part of the final mandatory project architecture. Streamlit and FastAPI continue to use their actual validated project outputs and data sources. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `docs/project_roadmap.md`, `docs/decision_log.md`, `streamlit_app/app.py`, `api/main.py` |

---

### DEC-021 — Use Streamlit Community Cloud and Render as Initial Deployment Targets

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Deployment |
| **Status** | Implemented |
| **Decision** | Use Streamlit Community Cloud as the initial deployment target for the planning application and Render as the initial deployment target for the FastAPI service. |
| **Reason** | These platforms support public portfolio deployment and are appropriate for the project's Python-based application architecture. |
| **Alternatives Considered** | Deploy both components through one platform; use Hugging Face Spaces; keep applications local only. |
| **Expected Impact** | Deployment files, dependencies, paths, startup commands, and documentation are prepared for these platforms. Another platform may be used later if a documented technical limitation occurs. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `streamlit_app/app.py`, `api/main.py`, `README.md` |

---

### DEC-022 — Lock Master Roadmap Version 3.1

| Field | Details |
|---|---|
| **Date** | 21 August 2026 |
| **Stage** | Roadmap and Governance |
| **Status** | Revised |
| **Decision** | Update the locked Master Roadmap from version 3.0 to version 3.1 to reflect the completed analytical, productization, deployment, and submission state of the project. |
| **Reason** | The project has progressed beyond the original roadmap state. The current roadmap must accurately distinguish completed mandatory deliverables from optional future enhancements. |
| **Alternatives Considered** | Keep version 3.0 unchanged; create a completely new roadmap; continue modifying the roadmap without version control. |
| **Expected Impact** | Roadmap version 3.1 becomes the authoritative current project roadmap. Future major architectural changes require a new decision-log entry. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `docs/project_roadmap.md`, `docs/decision_log.md` |

---

### DEC-023 — Freeze Core Technical Scope for Final Submission

| Field | Details |
|---|---|
| **Date** | 21 August 2026 |
| **Stage** | Final Submission |
| **Status** | Implemented |
| **Decision** | Freeze the core technical scope and prioritise validation, documentation, demonstration, and final submission over additional modelling or application features. |
| **Reason** | The required forecasting, evaluation, inventory intelligence, dashboard, API, deployment, and executive communication components are complete. Additional feature development introduces scope risk without being necessary for the core submission. |
| **Alternatives Considered** | Add additional forecasting models; build Power BI; add advanced explainability; redesign the dashboard; expand the modelling population. |
| **Expected Impact** | Remaining project effort will focus on repository audit, documentation consistency, deployment verification, demo preparation, and final submission. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `docs/project_roadmap.md`, `docs/development_scope.md`, `docs/assumptions_limitations.md` |

---

### DEC-024 — Retain the Baseline as the Production Forecaster

| Field | Details |
|---|---|
| **Date** | 21 August 2026 |
| **Stage** | Model Evaluation and Final Submission |
| **Status** | Implemented |
| **Decision** | Retain the damped-trend exponential-smoothing baseline as the locked production forecaster rather than promoting the machine-learning model. |
| **Reason** | On the untouched eight-week final-test period, the baseline achieved a WAPE of **53.17%**, while the LightGBM machine-learning model achieved **59.34%**. The ML model therefore did not provide the required improvement over the baseline. The baseline also achieved lower WAPE across the evaluated forecast horizons. |
| **Alternatives Considered** | Promote LightGBM as the production model; create a hybrid production model; continue tuning the ML model after observing the final-test results; retain the baseline. |
| **Expected Impact** | The baseline remains the authoritative production forecasting method for the current submission. The ML model remains documented as a fairly evaluated challenger that did not meet the production selection criteria. The final production configuration is locked and should not be changed without a new documented decision. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `data/processed/production_outputs/06_production_forecast_config.json`, `data/processed/production_outputs/06_production_forecast.csv`, `data/processed/baseline_outputs/04_champion_baseline_config.json`, `data/processed/ml_outputs/05_champion_ml_config.json`, `reports/tables/06_model_comparison_scorecard.csv` |

---

## 5. Future Decisions

New decisions will be added to this section only if a new material technical, analytical, product, deployment, or governance decision is required during the final submission phase.

At the current project stage, the core technical scope is frozen.

Remaining decisions may relate to:

- final documentation corrections;
- deployment configuration changes, if technically required;
- final submission requirements;
- demonstration or presentation changes;
- post-submission portfolio enhancements.

Optional enhancements such as Power BI, additional forecasting models, expanded modelling scope, advanced explainability, or additional application features are not part of the mandatory final submission scope.

No future decision should be entered unless it represents a genuine project decision and is supported by the relevant implementation, analysis, or validation.

---

## 6. Current Decision Summary

The current Project FORESIGHT decision state is:

| Area | Current Decision |
|---|---|
| **Data Source** | M5 dataset adapted to the Zidio / NorthBay Living business brief |
| **Development Population** | 300 SKU-store series |
| **Forecast Grain** | Weekly SKU-store |
| **Forecast Horizon** | 8 weeks |
| **Primary Forecast Metric** | WAPE |
| **Validation Method** | Rolling-origin chronological validation |
| **Final Holdout** | Untouched latest 8 weeks |
| **Production Forecaster** | Damped-trend exponential smoothing |
| **Baseline Final-Test WAPE** | 53.17% |
| **ML Final-Test WAPE** | 59.34% |
| **ML Production Selection** | No |
| **Inventory Risk Method** | Transparent rule-based scoring |
| **Inventory Inputs** | Simulated / estimated where observed client data was unavailable |
| **Planning Dashboard** | Streamlit |
| **Scoring Service** | FastAPI |
| **Dashboard Deployment** | Streamlit Community Cloud |
| **API Deployment** | Render |
| **Power BI** | De-scoped from mandatory submission |
| **Core Technical Scope** | Frozen for final submission |
| **Current Roadmap** | Version 3.1 |
| **Final Production Configuration** | Locked |

---

## 7. Governance Rule

Project FORESIGHT follows the principle:

> **Beat the baseline honestly, or ship the baseline and explain why.**

A more complex model is not considered superior merely because it uses machine learning.

Any future change to the locked production forecasting method, development population, forecasting horizon, core application architecture, or mandatory submission scope must be supported by:

1. a genuine project requirement;
2. relevant implementation or validation evidence;
3. an updated decision-log entry;
4. corresponding updates to affected documentation and outputs.

This ensures that the final repository remains reproducible, auditable, and consistent with the actual implemented project.

---

*Mohit Kumar · Zidio Development Data Science & Analytics Internship · Project FORESIGHT · Client: NorthBay Living*