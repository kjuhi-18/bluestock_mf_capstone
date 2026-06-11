"""
Automated Weekly Mutual Fund Performance Report

Reads:
- fund_scorecard.csv
- var_cvar_report.csv

Generates:
- weekly_report.html

Optionally emails the report using Gmail SMTP.
"""

import pandas as pd
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# ==========================
# LOAD DATA
# ==========================

scorecard = pd.read_csv(
    "../reports/fund_scorecard.csv"
)

var = pd.read_csv(
    "../reports/var_cvar_report.csv"
)


# ==========================
# TOP FUND
# ==========================

top_fund = (
    scorecard
    .sort_values(
        "fund_score",
        ascending=False
    )
    .iloc[0]
)


# ==========================
# HIGHEST RISK FUND
# ==========================

risk_fund = (
    var
    .sort_values(
        "VaR_95"
    )
    .iloc[0]
)


# ==========================
# LOAD HTML TEMPLATE
# ==========================

with open(
    "weekly_report.html",
    "r",
    encoding="utf-8"
) as file:

    html_template = file.read()


# ==========================
# REPLACE PLACEHOLDERS
# ==========================

html_content = html_template.format(

    top_fund=top_fund["scheme_name"],

    top_score=round(
        top_fund["fund_score"],
        2
    ),

    best_return=round(
        top_fund["return_5yr_pct"],
        2
    ),

    risk_fund=risk_fund["scheme_name"]

)


# ==========================
# SAVE GENERATED REPORT
# ==========================

with open(
    "generated_weekly_report.html",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        html_content
    )

print(
    "Weekly report generated successfully."
)


# ==========================
# OPTIONAL EMAIL SECTION
# ==========================

SEND_EMAIL = False

if SEND_EMAIL:

    sender_email = "YOUR_EMAIL@gmail.com"

    receiver_email = "YOUR_EMAIL@gmail.com"

    app_password = "YOUR_APP_PASSWORD"

    msg = MIMEMultipart()

    msg["Subject"] = (
        "Weekly Mutual Fund Performance Report"
    )

    msg["From"] = sender_email

    msg["To"] = receiver_email

    msg.attach(
        MIMEText(
            html_content,
            "html"
        )
    )

    server = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )

    server.starttls()

    server.login(
        sender_email,
        app_password
    )

    server.sendmail(
        sender_email,
        receiver_email,
        msg.as_string()
    )

    server.quit()

    print(
        "Email sent successfully."
    )