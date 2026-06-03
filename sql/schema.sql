-- Active: 1752167017627@@127.0.0.1@3306@bluestock_mf
CREATE TABLE dim_fund(
    fund_key INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER UNIQUE,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    risk_category TEXT
);

CREATE TABLE dim_date(
    date_key INTEGER PRIMARY KEY AUTOINCREMENT,
    full_date DATE,
    day INTEGER,
    month INTEGER,
    quarter INTEGER,
    year INTEGER
);

CREATE TABLE fact_nav(
    nav_key INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    date_key INTEGER,
    nav REAL,
    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code),
    FOREIGN KEY(date_key)
        REFERENCES dim_date(date_key)
);

CREATE TABLE fact_transactions(
    transaction_key INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    date_key INTEGER,
    amount REAL,
    transaction_type TEXT,
    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code),
    FOREIGN KEY(date_key)
        REFERENCES dim_date(date_key)
);

CREATE TABLE fact_performance(
    performance_key INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    expense_ratio REAL,
    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum(
    aum_key INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    date_key INTEGER,
    aum REAL,
    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code),
    FOREIGN KEY(date_key)
        REFERENCES dim_date(date_key)
);