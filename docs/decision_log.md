# Project FORESIGHT — Decision Log

## Document Control

| Item | Details |
|---|---|
| **Project** | Project FORESIGHT |
| **Author** | Mohit Kumar |
| **Internship** | Zidio Development |
| **Document Version** | 1.0 |
| **Status** | Active |
| **Created** | 2 August 2026 |
| **Last Updated** | 2 August 2026 |

---

## 1. Purpose

This decision log records important technical, analytical, modelling, product, and deployment decisions made throughout Project FORESIGHT.

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
| **Revised** | The original decision has been changed |
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
| **Expected Impact** | The project gains realistic sales history and hierarchy while requiring clear disclosure that it is an adaptation rather than observed NorthBay Living data. |
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
| **Alternatives requires an inventory position that can be combined with future demand forecasts. |
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
| **Status** | Approved |
| **Decision** | Organise the main analytical workflow into seven sequential notebooks covering data engineering, EDA, feature engineering, baseline forecasting, machine-learning forecasting, model evaluation, and inventory-risk scoring. |
| **Reason** | Separating responsibilities makes the project easier to understand, validate, reproduce, review, and explain during interviews. |
| **Alternatives Considered** | Use one large notebook; use only three broad notebooks; place all logic directly inside Python scripts. |
| **Expected Impact** | Each notebook will have a clear responsibility and will use validated outputs from the preceding stage. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `docs/project_roadmap.md`, `notebooks/` |

---

### DEC-005 — Forecast at Weekly SKU-Store Level

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Forecasting Design |
| **Status** | Approved |
| **Decision** | Produce demand forecasts at the weekly SKU-store level. |
| **Reason** | Daily SKU demand can be sparse and volatile. Weekly aggregation provides a more stable planning grain while preserving product and store-level detail for inventory decisions. |
| **Alternatives Considered** | Daily SKU-store forecasts; monthly forecasts; category-level forecasts; national product-level forecasts. |
| **Expected Impact** | Daily sales data will be aggregated into weekly observations during Notebook 03. Forecasts and evaluation results will remain specific to each SKU-store series. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/03_Forecasting_Feature_Engineering.ipynb`, `data/interim/weekly_features_final.parquet` |

---

### DEC-006 — Use an Eight-Week Forecast Horizon

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Forecasting Design |
| **Status** | Approved |
| **Decision** | Use an eight-week demand forecast horizon for the initial project implementation. |
| **Reason** | An eight-week horizon is suitable for medium-term inventory planning and falls within the six-to-eight-week range described in the engagement scope. |
| **Alternatives Considered** | Four-week horizon; six-week horizon; twelve-week horizon; multiple independent forecast horizons. |
| **Expected Impact** | Baselines, machine-learning models, rolling-origin validation, final forecasts, and inventory-risk calculations must use the same eight-week horizon. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/04_Baseline_Forecasting.ipynb`, `notebooks/05_Machine_Learning_Forecasting.ipynb` |

---

### DEC-007 — Use WAPE as the Primary Forecast Metric

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Forecast Evaluation |
| **Status** | Approved |
| **Decision** | Use Weighted Absolute Percentage Error, or WAPE, as the primary model-evaluation metric. |
| **Reason** | WAPE evaluates total absolute forecast error relative to total actual demand and is suitable for comparing performance across series absolute forecast error relative to total actual demand and is suitable for comparing performance across series with different sales volumes. |
| **Alternatives Considered** | MAPE; sMAPE; MAE; RMSE; MASE. |
| **Expected Impact** | All major models will report WAPE using the same evaluation periods and calculation method. Forecast Bias will be used as the secondary metric, with MAE and RMSE as supporting metrics. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/04_Baseline_Forecasting.ipynb`, `notebooks/06_Model_Evaluation_Selection.ipynb` |

---

### DEC-008 — Use Rolling-Origin Cross-Validation

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Forecast Evaluation |
| **Status** | Approved |
| **Decision** | Evaluate forecasting models using rolling-origin cross-validation while preserving chronological order. |
| **Reason** | Forecasting models must be evaluated on future periods using only information that would have been available at each forecast origin. Random splitting would break time order and could produce misleading results. |
| **Alternatives Considered** | Random train-test split; one fixed historical split; evaluation on the training period. |
| **Expected Impact** | Baseline and machine-learning models must use identical rolling validation windows. Future information must never enter training features. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/04_Baseline_Forecasting.ipynb`, `notebooks/05_Machine_Learning_Forecasting.ipynb`, `notebooks/06_Model_Evaluation_Selection.ipynb` |

---

### DEC-009 — Protect the Latest Eight Weeks as the Final Holdout

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Forecast Evaluation |
| **Status** | Approved |
| **Decision** | Reserve the latest eight-week period as an untouched final holdout dataset. |
| **Reason** | The final holdout provides an unbiased estimate of how the selected forecasting approach performs on data not used for feature design, model tuning, or champion selection. |
| **Alternatives Considered** | Use all available dates during model development; use a random holdout; repeatedly evaluate against the final period during tuning. |
| **Expected Impact** | The final holdout must remain unused until model development and selection decisions are complete. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/03_Forecasting_Feature_Engineering.ipynb`, `notebooks/06_Model_Evaluation_Selection.ipynb` |


---

### DEC-010 — Require a Seasonal-Naive Baseline

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Baseline Forecasting |
| **Status** | Approved |
| **Decision** | Use the seasonal-naive forecast as the mandatory benchmark that advanced forecasting models must be compared against. |
| **Reason** | Retail demand commonly contains recurring seasonal patterns. A seasonal-naive forecast provides a simple, transparent, and meaningful benchmark for determining whether a more complex model adds genuine value. |
| **Alternatives Considered** | Use only a simple naive forecast; compare models without a formal baseline; use the average demand as the only benchmark. |
| **Expected Impact** | No machine-learning model will be declared successful unless it is evaluated fairly against the seasonal-naive baseline on identical validation periods. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/04_Baseline_Forecasting.ipynb`, `models/champion_baseline_config.json` |

---

### DEC-011 — Use LightGBM and XGBoost as the Main Machine-Learning Models

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Machine-Learning Forecasting |
| **Status** | Approved |
| **Decision** | Use LightGBM as the primary machine-learning forecasting model and XGBoost as the secondary comparison model. |
| **Reason** | Both models can handle nonlinear relationships, lag variables, rolling statistics, pricing information, calendar effects, promotions, categorical features, and multiple SKU-store series within a global forecasting framework. |
| **Alternatives Considered** | Train separate ARIMA or Prophet models for every series; use deep learning; use only Random Forest; use a single machine-learning model without comparison. |
| **Expected Impact** | Notebook 05 will train and evaluate LightGBM and XGBoost using the same features, forecast horizon, validation folds, and evaluation metrics. Random Forest may be included only as an optional benchmark. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/05_Machine_Learning_Forecasting.ipynb`, `models/lightgbm_model.pkl`, `models/xgboost_model.pkl` |

---

### DEC-012 — Permit a Baseline or Hybrid Champion

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Model Evaluation and Selection |
| **Status** | Approved |
| **Decision** | Allow the final forecasting solution to use the seasonal-naive baseline, a machine-learning model, or a hybrid model-selection rule depending on validated performance. |
| **Reason** | One model may not perform best for every SKU-store series. Honest model selection is more important than forcing an advanced model into production. |
| **Alternatives Considered** | Always select LightGBM; always use one global champion for every series; hide SKU segments where machine learning performs poorly. |
| **Expected Impact** | Notebook 06 may assign different forecasting approaches to different SKU-store segments when the rule is reproducible, transparent, and supported by validation results. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/06_Model_Evaluation_Selection.ipynb`, `models/champion_model_decision.json`, `docs/model_card.md` |

---

### DEC-013 — Use Transparent Rule-Based Inventory Risk Scoring

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Inventory Intelligence |
| **Status** | Approved |
| **Decision** | Calculate stockout and overstock risks using transparent business rules that combine forecasts, lead time, on-hand inventory, on-order inventory, safety stock, demand coverage, and forecast confidence. |
| **Reason** | Operations users must understand why a SKU receives a risk classification and recommended action. Explainable rules are more suitable than an unexplained black-box classification model for the initial implementation. |
| **Alternatives Considered** | Train a black-box risk classifier; show forecasts without recommendations; assign risk labels manually. |
| **Expected Impact** | Every risk score, classification, reorder recommendation, and markdown recommendation must be traceable to documented formulas, thresholds, and assumptions. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `notebooks/07_Inventory_Intelligence_Risk_Scoring.ipynb`, `docs/risk_scoring_methodology.md` |

---

### DEC-014 — Use Streamlit as the Mandatory Planning Application

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Productization |
| **Status** | Approved |
| **Decision** | Build a seven-page Streamlit application as the primary stakeholder-facing planning dashboard. |
| **Reason** | Streamlit supports rapid development of interactive analytical applications using Python and is suitable for presenting forecasts, risks, filters, recommendations, and downloadable outputs. |
| **Alternatives Considered** | Use only Power BI; provide notebook outputs without an application; build a custom web interface. |
| **Expected Impact** | Streamlit remains a mandatory project deliverable. Power BI may supplement it but cannot replace it. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `streamlit_app/`, `docs/dashboard_user_guide.md` |

---

### DEC-015 — Use FastAPI for the Scoring Service

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Productization |
| **Status** | Approved |
| **Decision** | Build a lightweight FastAPI service that exposes product lists, forecasts, risk results, recommendations, health checks, and prediction functionality. |
| **Reason** | FastAPI provides input validation, structured response schemas, automatic API documentation, and a professional method for serving analytical results. |
| **Alternatives Considered** | Expose results only through Streamlit; use Flask; omit the scoring service. |
| **Expected Impact** | The final project must contain documented endpoints, graceful error handling, tested responses, and a publicly reachable service where deployment is technically possible. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `api/`, `docs/api_documentation.md` |

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
| **Related Files** | `docs/project_roadmap.md`, `docs/decision_log.md` |

---

### DEC-017 — Use a One-Command Reproducible Pipeline

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Data Foundation |
| **Status** | Implemented |
| **Decision** | Use `run_data_pipeline.py` as the primary command for reproducing the data-engineering workflow and validating its generated outputs. |
| **Reason** | A professional project should not depend on manually opening notebooks and executing individual cells to recreate essential datasets. |
| **Alternatives Considered** | Run Notebook 01 manually; execute separate scripts for each dataset; provide only previously exported files. |
| **Expected Impact** | A reviewer can regenerate and validate the five processed project datasets from the project root using one command. |
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
| **Status** | Approved |
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
| **Expected Impact** | `data/dashboard/` is not part of the final mandatory project architecture. Streamlit and FastAPI will continue to use their actual validated project outputs and data sources. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `docs/project_roadmap.md`, `docs/decision_log.md`, `streamlit_app/`, `api/` |

---

### DEC-021 — Use Streamlit Community Cloud and Render as Initial Deployment Targets

| Field | Details |
|---|---|
| **Date** | 2 August 2026 |
| **Stage** | Deployment |
| **Status** | Implemented |
| **Decision** | Use Streamlit Community Cloud as the initial deployment target for the planning application and Render as the initial deployment target for the FastAPI service. |
| **Reason** | These platforms support public portfolio deployment and are appropriate for the project’s Python-based application architecture. |
| **Alternatives Considered** | Deploy both components through one platform; use Hugging Face Spaces; keep applications local only. |
| **Expected Impact** | Deployment files, dependencies, paths, startup commands, and documentation will be prepared for these platforms. Another platform may be used later if a documented technical limitation occurs. |
| **Responsible** | Mohit Kumar |
| **Related Files** | `streamlit_app/`, `api/`, `docs/deployment_guide.md` |

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

## 5. Future Decisions

New decisions will be added to this section only if a new material technical, analytical, product, deployment, or governance decision is required during the final submission phase.

At the current project stage, no major architectural or modelling decisions are planned.

Remaining decisions may relate to:

- final documentation corrections;
- deployment configuration changes, if required;
- final submission requirements;
- demonstration or presentation changes;
- post-submission portfolio enhancements.

Optional enhancements such as Power BI, additional forecasting models, expanded modelling scope, or advanced application features are not part of the mandatory final submission scope.

No future decision should be entered unless it represents a genuine project decision and is supported by the relevant implementation, analysis, or validation.
