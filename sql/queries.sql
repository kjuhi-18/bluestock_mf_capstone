-- 1. Top 5 Funds by AUM

SELECT *
FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

--------------------------------------------------

-- 2. Average NAV Per Month

SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

--------------------------------------------------

-- 3. SIP YoY Growth

SELECT
    year,
    AVG(yoy_growth_pct) AS avg_yoy_growth
FROM monthly_sip_inflows
GROUP BY year
ORDER BY year;

--------------------------------------------------

-- 4. Transactions by State

SELECT
    state,
    SUM(amount) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

--------------------------------------------------

-- 5. Funds with Expense Ratio < 1%

SELECT
    amfi_code,
    expense_ratio
FROM fact_performance
WHERE expense_ratio < 1;

--------------------------------------------------

-- 6. Top Fund Houses by AUM

SELECT
    fund_house,
    SUM(aum) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC;

--------------------------------------------------

-- 7. Highest 5-Year Return Funds

SELECT
    amfi_code,
    return_5y
FROM fact_performance
ORDER BY return_5y DESC
LIMIT 10;

--------------------------------------------------

-- 8. Average Transaction Amount by Type

SELECT
    transaction_type,
    AVG(amount) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;

--------------------------------------------------

-- 9. Risk Category Distribution

SELECT
    risk_category,
    COUNT(*) AS total_funds
FROM dim_fund
GROUP BY risk_category;

--------------------------------------------------

-- 10. Monthly NAV Trend

SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;