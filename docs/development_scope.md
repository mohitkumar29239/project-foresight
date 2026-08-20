# Project FORESIGHT — Development Scope

Project FORESIGHT uses a representative development population of 300 SKU-store series.

The development population contains:

- 30 products selected across three product categories;
- all 10 available retail stores;
- all 1,913 historical sales dates.

The complete `sku_master_final.csv` contains 30,490 SKU-store reference records. However, all sales analysis, forecasting, simulated inventory analysis, risk scoring, and dashboard KPIs will use only the 300 SKU-store series available in `sales_daily_final.csv`.

This reduced scope supports reproducible execution within the available local memory, storage, and processing capacity.

All simulated inventory fields, estimated financial attributes, and assumption-based replenishment parameters will be clearly identified throughout the project.

## Scope Authority

`data/processed/development_sku_scope.csv` is the authoritative definition of the modelling and decision-support population.

The following project components must use this scope:

- EDA KPI calculations;
- weekly feature generation;
- baseline forecasting;
- machine-learning forecasting;
- model evaluation;
- final forecast outputs;
- inventory-risk scoring;
- Streamlit dashboard KPIs;
- FastAPI scoring outputs.

The complete `sku_master_final.csv` must not be used as the denominator for development-scope KPIs.

Any output that uses a different population must explicitly identify that population.