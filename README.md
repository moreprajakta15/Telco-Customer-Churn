# Telco Customer Churn — Analysis & Prediction Dashboard

## Project Overview

This project analyzes customer churn for a telecom company using a dataset of 7,043 customer records. It covers the full workflow — data cleaning, exploratory data analysis (EDA), and an interactive Excel dashboard — to identify which customers are most likely to churn and why.

**Churn** refers to customers who stop using the company's services. Identifying churn drivers helps the business take proactive steps (offers, retention campaigns) to keep at-risk customers.

## Dataset

- **Source**: Telco Customer Churn dataset (`WA_Fn-UseC_-Telco-Customer-Churn.csv`)
- **Records**: 7,043 customers
- **Columns**: 20 fields, including demographics, subscribed services, contract details, billing information, and churn status

## Project Workflow

1. **Data Cleaning** (`data.py`)
   - Converted `TotalCharges` to numeric (handled blank values for new customers with 0 tenure)
   - Removed the non-predictive `customerID` column
   - Checked for missing values and duplicates
   - Exported the cleaned dataset as `telco_churn_cleaned.csv`

2. **Exploratory Data Analysis** (`code.py`)
   - Analyzed churn distribution, and churn by contract type, tenure, monthly charges, internet service, and payment method
   - Generated 6 visualizations (count plots, pie charts, histograms, KDE plots, bar charts) using Matplotlib and Seaborn

3. **Interactive Dashboard** (`telco_churn_dashboard.xlsx`)
   - Built in Excel with live formulas (`COUNTIFS`, `AVERAGEIFS`) so the dashboard recalculates automatically if the underlying data changes
   - Includes 5 KPI cards and 8 charts covering churn distribution, contract type, internet service, tenure trends, payment method, and billing patterns
   - Colorful, single-page layout designed for easy sharing (portfolio/resume-ready)

## Files in This Repo

| File | Purpose |
|---|---|
| `WA_Fn-UseC_-Telco-Customer-Churn.csv` | Raw dataset |
| `data.py` | Data cleaning script |
| `telco_churn_cleaned.csv` | Cleaned dataset (output of `data.py`) |
| `code.py` | EDA script with visualizations |
| `1_churn_distribution.png` – `6_churn_by_payment.png` | EDA chart outputs |
| `telco_churn_dashboard.xlsx` | Interactive Excel dashboard |
| `.gitignore` | Files/folders excluded from version control |

## Key Insights

- **Overall churn rate: 26.5%** (1,869 of 7,043 customers churned)
- **Contract type is the strongest churn driver**: Month-to-month customers churn at ~43%, compared to ~11% for one-year and ~3% for two-year contracts
- **New customers churn the most**: Average tenure of churned customers is ~18 months vs. ~38 months for retained customers
- **Fiber optic users churn more than DSL users**: ~42% vs. ~19%
- **Payment method matters**: Electronic check users churn at ~45%, while automatic payment methods (bank transfer/credit card) churn at ~17–18%
- **Price sensitivity plays a role**: Churned customers pay ~£74/month on average vs. ~£61/month for retained customers

## Recommendations

- Offer incentives to move month-to-month customers onto longer-term contracts
- Focus retention efforts on customers in their first 12 months
- Encourage automatic payment methods over electronic check
- Investigate service quality for fiber optic customers

## Tools & Technologies

- Python (Pandas, NumPy, Matplotlib, Seaborn) — data cleaning and EDA
- Excel (openpyxl-generated, formula-driven) — interactive dashboard

