# Project FORESIGHT — Assumptions and Limitations

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

This document records the assumptions, limitations, exclusions, and interpretation rules used throughout Project FORESIGHT.

Its purpose is to ensure that:

- simulated values are not presented as observed business facts;
- analytical results are interpreted within the available data;
- modelling limitations remain visible;
- business recommendations are supported by transparent assumptions;
- future changes can be documented in a controlled manner.

This document will be updated whenever new assumptions or limitations are identified.

---

## 2. Project Adaptation

Project FORESIGHT adapts the Zidio demand and inventory intelligence engagement using public M5 retail data.

The project uses three source files:

- `sales_train_validation.csv.gz`;
- `calendar.csv`;
- `sell_prices.csv.gz`.

These files provide historical unit sales, calendar information, events, SNAP indicators, product hierarchy, store hierarchy, and weekly selling prices.

The source data does not represent actual NorthBay Living operations. Therefore:

- NorthBay Living is treated as the business case context;
- M5 data is used as the analytical foundation;
- results must not be described as actual NorthBay Living performance;
- financial and inventory conclusions must be presented as analytical estimates.

---

## 3. Data Assumptions

### 3.1 Sales Quantity

The `sales` or `units_sold` field is treated as historical customer demand.

A zero value may represent:

- no customer demand;
- unavailable stock;
- discontinued activity;
- temporary selling restrictions;
- genuine slow-moving behaviour.

The source data does not provide enough information to distinguish these causes perfectly.

### 3.2 Sales Availability

The historical sales records are assumed to be sufficiently complete for exploratory analysis and forecasting.

However, observed sales may underestimate true demand when stock was unavailable.

### 3.3 Calendar Alignment

Calendar dates, week identifiers, events, and SNAP indicators are assumed to be correctly aligned with historical sales records after Notebook 01 validation.

### 3.4 Selling Price

The weekly selling price is assumed to represent the active selling price for the relevant product-store-week combination.

Missing prices may indicate that:

- the product was not actively sold;
- the price was not recorded;
- the product had not yet launched;
- the product had temporarily disappeared from the assortment.

Missing price values must not automatically be interpreted as free products or zero-value sales.

### 3.5 Promotion Information

The M5 source files do not include a complete promotion-history table.

Price reductions, event periods, and selected calendar indicators may be used as indirect promotion signals. These signals do not prove that a formal marketing promotion occurred.

---

## 4. Simulated Inventory Assumptions

The Inventory Snapshot dataset is simulated because the M5 source data does not contain:

- on-hand inventory;
- on-order quantities;
- purchase orders;
- supplier receipts;
- replenishment dates;
- safety-stock policies;
- reorder points;
- observed stockout events;
- supplier service levels.

The simulated dataset is created only to support inventory-risk and decisioning demonstrations.

### 4.1 On-Hand Inventory

Simulated on-hand quantities represent estimated stock positions derived from historical demand behaviour and controlled analytical rules.

They are not observed physical stock counts.

### 4.2 On-Order Inventory

Simulated on-order quantities represent estimated replenishment quantities.

They are not actual confirmed supplier orders.

### 4.3 Lead Time

Lead times are simulated or estimated because supplier-level lead-time records are unavailable.

The selected lead-time values must be documented before final risk scoring.

### 4.4 Reorder Point and Safety Stock

Reorder points and safety-stock quantities will be calculated using documented business rules.

These rules may use:

- expected demand;
- demand variability;
- lead time;
- service-level assumptions;
- forecast confidence.

They do not represent an existing retailer replenishment policy.

### 4.5 Stockout and Overstock Labels

Stockout and overstock classifications will be analytical risk indicators.

They must not be described as confirmed historical stockout or overstock events.

---

## 5. Development-Scope Assumptions

The project uses 300 SKU-store series selected from the wider M5 population.

The scope contains:

- 30 representative products;
- 10 stores;
- 300 unique SKU-store combinations;
- the complete available historical date range for those combinations.

The development scope is used to:

- reduce computational requirements;
- support detailed analysis;
- enable repeatable forecasting experiments;
- make dashboard and deployment development practical.

Results from the 300-series scope should not automatically be treated as representative of every product in the complete M5 population.

All development-scope KPIs must use:

`data/processed/development_sku_scope.csv`

The complete 30,490-record SKU Master must not be used as the denominator for development-scope KPIs.

---

## 6. Financial Assumptions

The project may estimate:

- revenue;
- unit cost;
- gross margin;
- revenue at risk;
- lost-sales exposure;
- inventory value;
- capital locked in excess inventory;
- markdown value.

### 6.1 Currency Interpretation

The M5 dataset does not establish Indian rupees as its original transaction currency.

Where the project presents rupee-style business impact, the values must be described as scenario-based analytical estimates rather than converted audited financial results.

### 6.2 Unit Cost

Unit cost is not directly provided by the M5 source data.

Any unit-cost value used in the project will be estimated using a documented assumption or cost-to-price relationship.

### 6.3 Margin

Gross-margin estimates will depend on simulated or estimated unit costs.

They must not be described as audited profitability.

### 6.4 Revenue at Risk

Revenue at risk will estimate potential sales exposure based on forecast demand, inventory availability, and selling price.

It will not represent guaranteed lost revenue.

### 6.5 Capital Locked

Capital locked in excess inventory will estimate the value of inventory above the expected demand requirement.

It will depend on simulated inventory balances, estimated unit cost, and chosen overstock thresholds.

---

## 7. Exploratory Analysis Limitations

Exploratory relationships do not automatically establish causation.

For example:

- higher sales during an event period do not prove the event caused the increase;
- lower prices associated with higher demand do not independently prove price elasticity;
- SNAP-day differences may also reflect calendar, store, product, or seasonal effects;
- zero sales do not always prove dead stock;
- high inventory does not automatically prove inefficient replenishment.

Business interpretations must remain consistent with the available evidence.

---

## 8. Forecasting Assumptions and Limitations

### 8.1 Forecast Grain

Forecasting models will be evaluated using rolling-origin cross-validation so that chronological order is preserved and future information does not enter the training process.

Forecasts will be produced at the weekly SKU-store level.

Daily operational variation may therefore be smoothed during weekly aggregation.

### 8.2 Forecast Horizon

The initial forecast horizon is fixed at eight weeks.

Forecast reliability may decline for longer horizons.

### 8.3 Historical Patterns

Forecasting models assume that historical demand patterns contain useful information about future demand.

Unexpected structural changes may reduce forecast accuracy.

Examples include:

- major economic shocks;
- new competitors;
- product discontinuation;
- supply disruption;
- unusual promotions;
- assortment changes;
- changes in customer behaviour.

### 8.4 Feature Availability

Only information available before each forecast origin may be used.

Future sales, future rolling statistics, and unavailable future prices or events must not enter model features.

### 8.5 Intermittent Demand

Some SKU-store series may contain many zero-demand periods.

These series may be more difficult to forecast accurately than high-volume, stable series.

### 8.6 Model Generalisation

A model performing well overall may still perform poorly for certain:

- products;
- categories;
- stores;
- low-volume series;
- volatile series;
- intermittent series.

Overall WAPE must therefore be supported by segment-level and SKU-level evaluation.

### 8.7 Baseline Comparison

Machine-learning models are not assumed to be better automatically.

The seasonal-naive baseline may remain the preferred method when advanced models do not produce a reliable improvement.

### 8.8 Forecast Uncertainty

Point forecasts are estimates, not guarantees.

Forecast confidence or uncertainty must be considered when creating inventory recommendations.

---

## 9. Risk-Scoring Limitations

Inventory-risk scores will depend on:

- forecast quality;
- simulated inventory;
- estimated lead times;
- safety-stock rules;
- reorder assumptions;
- selected risk thresholds;
- estimated financial values.

A risk score should support human decision-making rather than automatically place purchase orders or apply markdowns.

The project will not implement:

- automated purchase-order placement;
- supplier optimisation;
- price optimisation;
- real-time replenishment;
- complete inventory optimisation;
- guaranteed service-level optimisation.

---

## 10. Dashboard and API Limitations

The Streamlit application and FastAPI service will use prepared analytical outputs.

They are demonstration and decision-support tools rather than live integrations with retailer systems.

Possible limitations include:

- deployment memory limits;
- application startup delay;
- static or periodically refreshed datasets;
- no real-time transaction processing;
- no live supplier integration;
- no authentication in the initial portfolio version;
- public hosting restrictions;
- model or data-file size constraints.

Public deployment availability may depend on third-party hosting platforms.

---

## 11. Interpretation Rules

Throughout the project:

1. Simulated values must be labelled as simulated or estimated.
2. Forecasts must be labelled as predictions.
3. Risk flags must be labelled as decision-support indicators.
4. Financial impact must be labelled as estimated exposure.
5. Correlation must not be described as causation.
6. Development-scope results must not be presented as full-population results.
7. Machine-learning performance must be compared with the seasonal-naive baseline.
8. Weak or negative results must be reported honestly.
9. Recommendations must include relevant assumptions.
10. Automated business action is outside the project scope.

---

## 12. Update Policy

This is an active document.

It must be updated when the project defines or discovers:

- final feature availability assumptions;
- exact validation folds;
- model-performance limitations;
- forecast-confidence rules;
- final lead-time values;
- safety-stock methodology;
- reorder thresholds;
- stockout thresholds;
- overstock thresholds;
- final financial assumptions;
- deployment constraints;
- new data-quality concerns.

Important changes must also be recorded in:

`docs/decision_log.md`