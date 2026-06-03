from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

# =========================
# Paths
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_PATH = BASE_DIR / "data" / "raw"
PROCESSED_PATH = BASE_DIR / "data" / "processed"
DB_PATH = BASE_DIR / "data" / "db" / "bluestock_mf.db"

# =========================
# SQLite Connection
# =========================

engine = create_engine(
    f"sqlite:///{DB_PATH}"
)

print("SQLite Database Connected")
print(DB_PATH)

# =========================
# Load Datasets
# =========================

fund_master = pd.read_csv(
    RAW_PATH / "01_fund_master.csv"
)

nav_history = pd.read_csv(
    PROCESSED_PATH / "nav_history_clean.csv"
)

investor_transactions = pd.read_csv(
    PROCESSED_PATH / "investor_transactions_clean.csv"
)

scheme_performance = pd.read_csv(
    PROCESSED_PATH / "scheme_performance_clean.csv"
)

aum = pd.read_csv(
    RAW_PATH / "03_aum_by_fund_house.csv"
)

print("\nDatasets Loaded Successfully")

# =========================
# Create dim_fund
# =========================

dim_fund = fund_master.copy()

# =========================
# Create dim_date
# =========================

nav_history["date"] = pd.to_datetime(
    nav_history["date"]
)

dim_date = pd.DataFrame()

dim_date["full_date"] = (
    nav_history["date"]
    .drop_duplicates()
    .sort_values()
)

dim_date["day"] = dim_date["full_date"].dt.day
dim_date["month"] = dim_date["full_date"].dt.month
dim_date["quarter"] = dim_date["full_date"].dt.quarter
dim_date["year"] = dim_date["full_date"].dt.year

print("Date Dimension Created")

# =========================
# Load Dimension Tables
# =========================

dim_fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

dim_date.to_sql(
    "dim_date",
    engine,
    if_exists="replace",
    index=False
)

print("Dimension Tables Loaded")

# =========================
# Load Fact Tables
# =========================

nav_history.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

investor_transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

scheme_performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("Fact Tables Loaded")

# =========================
# Row Count Verification
# =========================

tables = {
    "dim_fund": dim_fund,
    "dim_date": dim_date,
    "fact_nav": nav_history,
    "fact_transactions": investor_transactions,
    "fact_performance": scheme_performance,
    "fact_aum": aum
}

print("\n" + "="*50)
print("ROW COUNT VALIDATION")
print("="*50)

for table_name, df in tables.items():

    db_count = pd.read_sql(
        f"SELECT COUNT(*) AS cnt FROM {table_name}",
        engine
    )

    csv_rows = len(df)
    db_rows = db_count["cnt"][0]

    print(f"\n{table_name}")
    print(f"Source Rows : {csv_rows}")
    print(f"DB Rows     : {db_rows}")

    if csv_rows == db_rows:
        print("Status      : MATCH")
    else:
        print("Status      : MISMATCH")

print("\nETL Pipeline Completed Successfully")