"""
Purpose:
Fetching Live NAVs

Author: Kunal Jhindal
Project: Bluestock Mutual Fund Analytics Capstone
"""
import requests
import pandas as pd
from pathlib import Path

# Scheme Codes
SCHEMES = {
    "HDFC_Top_100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

# Output folder
RAW_PATH = Path("../data/raw")
RAW_PATH.mkdir(parents=True, exist_ok=True)


def fetch_nav(scheme_name, scheme_code):
    """Fetch NAV history from MFAPI and save as CSV"""

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        output_file = RAW_PATH / f"{scheme_name}_nav.csv"

        nav_df.to_csv(output_file, index=False)

        print(f"✓ Saved: {output_file}")

    except Exception as e:
        print(f"✗ Error fetching {scheme_name}: {e}")


def main():
    print("Fetching live NAV data...\n")

    for name, code in SCHEMES.items():
        fetch_nav(name, code)

    print("\nDone!")


if __name__ == "__main__":
    main()