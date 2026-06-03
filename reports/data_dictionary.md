# Mutual Fund Analytics Platform - Data Dictionary

## Project Overview

This document describes all datasets used in the Mutual Fund Analytics Platform project, including column definitions, data types, business meanings, and source references.

---

# Dataset: 01_fund_master.csv

**Purpose:** Master reference table containing details of all mutual fund schemes.

| Column Name        | Data Type | Business Definition                 |
| ------------------ | --------- | ----------------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme identifier       |
| fund_house         | String    | Asset Management Company (AMC) name |
| scheme_name        | String    | Mutual fund scheme name             |
| category           | String    | Broad fund category                 |
| sub_category       | String    | Detailed scheme category            |
| plan               | String    | Direct or Regular plan              |
| launch_date        | Date      | Fund launch date                    |
| benchmark          | String    | Benchmark index                     |
| expense_ratio_pct  | Float     | Annual expense ratio (%)            |
| exit_load_pct      | Float     | Exit load percentage                |
| min_sip_amount     | Float     | Minimum SIP investment amount       |
| min_lumpsum_amount | Float     | Minimum lump-sum investment amount  |
| fund_manager       | String    | Fund manager name                   |
| risk_category      | String    | Risk classification                 |
| sebi_category_code | String    | SEBI category code                  |

**Source:** AMFI Scheme Master Dataset

---

# Dataset: 02_nav_history.csv

**Purpose:** Historical NAV values for mutual fund schemes.

| Column Name | Data Type | Business Definition    |
| ----------- | --------- | ---------------------- |
| amfi_code   | Integer   | AMFI scheme identifier |
| date        | Date      | NAV reporting date     |
| nav         | Float     | Net Asset Value        |

**Source:** Historical NAV Records

---

# Dataset: 03_aum_by_fund_house.csv

**Purpose:** Assets Under Management by fund house.

| Column Name | Data Type | Business Definition      |
| ----------- | --------- | ------------------------ |
| fund_house  | String    | Asset Management Company |
| report_date | Date      | Reporting date           |
| aum         | Float     | Assets Under Management  |

**Source:** AMFI AUM Reports

---

# Dataset: 04_monthly_sip_inflows.csv

**Purpose:** Monthly SIP investment inflows.

| Column Name    | Data Type | Business Definition                  |
| -------------- | --------- | ------------------------------------ |
| month          | Date      | Reporting month                      |
| sip_amount     | Float     | Total SIP inflow                     |
| yoy_growth_pct | Float     | Year-over-Year SIP growth percentage |

**Source:** AMFI SIP Statistics

---

# Dataset: 05_category_inflows.csv

**Purpose:** Category-wise investment inflows.

| Column Name   | Data Type | Business Definition  |
| ------------- | --------- | -------------------- |
| category      | String    | Mutual fund category |
| inflow_amount | Float     | Net inflow amount    |
| report_date   | Date      | Reporting date       |

**Source:** AMFI Category Flow Reports

---

# Dataset: 06_industry_folio_count.csv

**Purpose:** Industry-wide folio statistics.

| Column Name | Data Type | Business Definition     |
| ----------- | --------- | ----------------------- |
| month       | Date      | Reporting month         |
| folio_count | Integer   | Total investor folios   |
| growth_pct  | Float     | Folio growth percentage |

**Source:** AMFI Industry Statistics

---

# Dataset: 07_scheme_performance.csv

**Purpose:** Fund performance metrics.

| Column Name      | Data Type | Business Definition         |
| ---------------- | --------- | --------------------------- |
| amfi_code        | Integer   | AMFI scheme identifier      |
| return_1y        | Float     | One-year return (%)         |
| return_3y        | Float     | Three-year CAGR (%)         |
| return_5y        | Float     | Five-year CAGR (%)          |
| expense_ratio    | Float     | Annual expense ratio (%)    |
| max_drawdown_pct | Float     | Maximum drawdown percentage |

**Source:** Scheme Performance Dataset

---

# Dataset: 08_investor_transactions.csv

**Purpose:** Investor-level mutual fund transactions.

| Column Name      | Data Type | Business Definition        |
| ---------------- | --------- | -------------------------- |
| investor_id      | Integer   | Unique investor identifier |
| amfi_code        | Integer   | Mutual fund scheme code    |
| transaction_date | Date      | Transaction date           |
| transaction_type | String    | SIP, Lumpsum, Redemption   |
| amount           | Float     | Transaction amount         |
| state            | String    | Investor state             |
| kyc_status       | String    | KYC verification status    |

**Source:** Investor Transaction Records

---

# Dataset: 09_portfolio_holdings.csv

**Purpose:** Scheme portfolio composition.

| Column Name  | Data Type | Business Definition             |
| ------------ | --------- | ------------------------------- |
| amfi_code    | Integer   | AMFI scheme identifier          |
| holding_name | String    | Security name                   |
| sector       | String    | Industry sector                 |
| holding_pct  | Float     | Portfolio allocation percentage |

**Source:** Portfolio Holdings Data

---

# Dataset: 10_benchmark_indices.csv

**Purpose:** Benchmark index performance tracking.

| Column Name | Data Type | Business Definition  |
| ----------- | --------- | -------------------- |
| index_name  | String    | Benchmark index name |
| date        | Date      | Observation date     |
| index_value | Float     | Index closing value  |
| return_pct  | Float     | Percentage return    |

**Source:** Benchmark Index Dataset

---

# Data Quality & Cleaning Summary

## Cleaning Activities Performed

### nav_history.csv

* Converted date column to datetime format
* Sorted by AMFI code and date
* Removed duplicate rows
* Forward-filled missing NAV values
* Validated NAV > 0

### investor_transactions.csv

* Standardized transaction types
* Validated positive transaction amounts
* Fixed date formats
* Checked KYC status values
* Removed duplicates

### scheme_performance.csv

* Converted returns to numeric
* Validated expense ratio range (0.1%–2.5%)
* Flagged extreme return anomalies
* Removed duplicates

### Remaining Datasets

* Standardized column names
* Removed duplicate rows
* Performed basic data validation checks

---

# Database Design

## Database

SQLite Database: `bluestock_mf.db`

## Star Schema

### Dimension Tables

* dim_fund
* dim_date

### Fact Tables

* fact_nav
* fact_transactions
* fact_performance
* fact_aum

---

# Key Business Identifier

**AMFI Code**

AMFI Code serves as the primary business key linking:

* Fund Master
* NAV History
* Scheme Performance
* Investor Transactions
* AUM Data

This ensures consistency across all analytical and reporting datasets.
