# 📊 Bluestock Mutual Fund Analytics Platform

<div align="center">

# 🚀 End-to-End Mutual Fund Analytics & Risk Intelligence Platform

### Built with Python • SQL • Power BI • Financial Analytics • Monte Carlo Simulation

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge\&logo=python)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow?style=for-the-badge\&logo=powerbi)
![SQL](https://img.shields.io/badge/SQLite-Database-green?style=for-the-badge)
![Finance](https://img.shields.io/badge/Domain-Finance-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

### 📈 Transforming Raw Mutual Fund Data into Actionable Investment Intelligence

</div>

---

# 🌟 Project Highlights

This capstone project simulates a complete Mutual Fund Analytics Platform used by asset management companies, analysts, and investors.

The platform performs:

* ✅ Automated ETL Pipelines
* ✅ Data Cleaning & Validation
* ✅ Exploratory Data Analysis
* ✅ Performance Analytics
* ✅ Risk Analytics
* ✅ Investor Analytics
* ✅ Portfolio Analytics
* ✅ Power BI Dashboarding
* ✅ Monte Carlo Forecasting
* ✅ Automated HTML Reporting
* ✅ Fund Recommendation Engine

---

# 🎯 Business Problem

The Indian Mutual Fund industry has experienced massive growth in:

* Assets Under Management (AUM)
* SIP Contributions
* Investor Participation
* Fund Categories
* Portfolio Diversification

However, investors often struggle to:

* Compare funds objectively
* Measure risk accurately
* Track portfolio concentration
* Understand benchmark performance
* Generate actionable insights

This project solves these challenges through a complete analytics ecosystem.

---

# 🏗️ Project Architecture

```text
Raw Data
    ↓
ETL Pipeline
    ↓
Data Cleaning
    ↓
SQLite Storage
    ↓
EDA & Analytics
    ↓
Performance Metrics
    ↓
Risk Analytics
    ↓
Power BI Dashboard
    ↓
Investor Insights
    ↓
Automated Reports
```

---

# 🛠 Tech Stack

| Category        | Tools                       |
| --------------- | --------------------------- |
| Programming     | Python                      |
| Database        | SQLite                      |
| Data Processing | Pandas, NumPy               |
| Statistics      | SciPy                       |
| Visualization   | Matplotlib, Seaborn, Plotly |
| Dashboard       | Power BI                    |
| Version Control | Git & GitHub                |
| Reporting       | HTML, PDF                   |

---

# 📂 Repository Structure

```text
Bluestock_MF_Capstone
│
├── B5_automation
│   ├── email_report.py
│   ├── email_template.html
│   └── weekly_report.html
│
├── dashboard
│   ├── bluestock_mf_dashboard.pbix
│   └── Dashboard.pdf
│
├── data
│   ├── db
│   ├── processed
│   └── raw
│
├── notebooks
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   ├── 05_advanced_analytics.ipynb
│   └── B3_Monte_Carlo_Simulation.ipynb
│
├── reports
│   ├── charts
│   ├── Dashboard Screenshots
│   ├── Output_CSVs
│   ├── Final_Report.pdf
│   └── Presentation.pptx
│
├── scripts
│   ├── compute_metrics.py
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   └── recommender.py
│
├── sql
│   ├── schema.sql
│   └── queries.sql
│
├── README.md
├── requirements.txt
├── .gitignore
└── .gitattributes
```

---

# 📊 Analytics Performed

## 📈 Performance Analytics

* CAGR
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Tracking Error

## ⚠ Risk Analytics

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling Sharpe Ratio
* Sector HHI Concentration

## 👥 Investor Analytics

* Cohort Analysis
* SIP Continuity Analysis
* Geographic Analysis
* Age Group Analysis
* Transaction Trend Analysis

## 🏦 Fund Analytics

* Fund Ranking
* Benchmark Comparison
* Fund Scorecard
* Risk vs Return Analysis
* Portfolio Concentration Analysis

---

# 🎲 Monte Carlo Simulation

A 5-Year Monte Carlo Simulation was developed to forecast future NAV growth under multiple market scenarios.

### Outputs

* Expected NAV
* Optimistic Scenario
* Pessimistic Scenario
* Confidence Intervals
* Future Growth Distribution

---

# 🤖 Fund Recommendation Engine

Users can select:

* Low Risk
* Moderate Risk
* High Risk

The recommendation engine returns top-performing mutual funds based on:

* Sharpe Ratio
* Risk Grade
* Historical Returns

---

# 📧 Automated Reporting

The project includes an automated HTML reporting system capable of generating:

* Weekly Performance Reports
* Fund Rankings
* Risk Highlights
* HTML Reports Ready for Email Delivery

---

# 📊 Dashboard Pages

## 🏦 Industry Overview

* Total AUM
* SIP Inflows
* Total Folios
* Industry Trends

## 📈 Fund Performance

* Risk vs Return Analysis
* Fund Scorecards
* Benchmark Comparison

## 👥 Investor Analytics

* Investor Demographics
* Transaction Insights
* Geographic Analysis

## 📉 SIP & Market Trends

* SIP Growth
* Market Performance
* Category Inflows

---

# 🏆 Key Findings

### 🥇 Top Ranked Fund

SBI Small Cap Fund emerged as the highest-ranked fund based on composite scoring.

### 📈 Best Long-Term Return

ABSL Small Cap Fund delivered the strongest 5-Year returns.

### 💰 Industry Growth

SIP inflows crossed ₹31,000 Crore indicating strong retail participation.

### ⚠ Risk Observation

Higher returns generally corresponded with higher volatility and downside risk.

### 📊 Benchmark Observation

Several actively managed funds consistently outperformed benchmark indices.

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/kjuhi-18/bluestock_mf_capstone
cd Bluestock_MF_Capstone
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

## Run Recommendation Engine

```bash
python scripts/recommender.py
```

## Generate Weekly Report

```bash
python B5_automation/email_report.py
```

## Open Dashboard

Open:

```text
dashboard/bluestock_mf_dashboard.pbix
```

using Power BI Desktop.

---

# 📸 Dashboard Gallery

## Industry Overview

![Industry Overview](reports/Dashboard%20Screenshots/page1_industry_overview.png)

## Fund Performance

![Fund Performance](reports/Dashboard%20Screenshots/page2_fund_performance.png)


## Investor Analytics

![Investor Analytics](reports/Dashboard%20Screenshots/page3_investor_analytics.png)

## SIP & Market Trends

![SIP & Market Trends](reports/Dashboard%20Screenshots/page4_sip_market_trends.png)



---



# 👨‍💻 Author

## Kunal Jhindal

**B.Tech Artificial Intelligence & Machine Learning**

Passionate about:

* 📊 Data Analytics
* 🤖 Machine Learning
* 💹 Financial Analytics
* 📈 Quantitative Finance
* 🔍 Data Science

---

<div align="center">

### ⭐ If you found this project interesting, consider giving it a star!

### 🚀 Built with Python, Analytics & Curiosity

</div>
