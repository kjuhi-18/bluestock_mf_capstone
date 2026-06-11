"""
compute_metrics.py

Calculates:

1. CAGR
2. Sharpe Ratio
3. Sortino Ratio
4. Alpha
5. Beta
6. Maximum Drawdown

Author: Kunal Jhindal
Project: Bluestock Mutual Fund Analytics Capstone
"""

import pandas as pd
import numpy as np

from scipy.stats import linregress


# ====================================
# CAGR
# ====================================

def calculate_cagr(
    start_nav,
    end_nav,
    years
):

    return (

        (end_nav / start_nav)

        **

        (1 / years)

        - 1

    )


# ====================================
# SHARPE RATIO
# ====================================

def calculate_sharpe_ratio(
    returns,
    risk_free_rate=0.065
):

    excess_return = (

        returns.mean() * 252

        -

        risk_free_rate

    )

    volatility = (

        returns.std()

        *

        np.sqrt(252)

    )

    return excess_return / volatility


# ====================================
# SORTINO RATIO
# ====================================

def calculate_sortino_ratio(
    returns,
    risk_free_rate=0.065
):

    downside = returns[
        returns < 0
    ]

    downside_std = (

        downside.std()

        *

        np.sqrt(252)

    )

    excess_return = (

        returns.mean() * 252

        -

        risk_free_rate

    )

    return excess_return / downside_std


# ====================================
# ALPHA & BETA
# ====================================

def calculate_alpha_beta(
    fund_returns,
    benchmark_returns
):

    slope, intercept, _, _, _ = linregress(

        benchmark_returns,

        fund_returns

    )

    alpha = intercept * 252

    beta = slope

    return alpha, beta


# ====================================
# MAX DRAWDOWN
# ====================================

def calculate_max_drawdown(
    nav_series
):

    running_max = (
        nav_series.cummax()
    )

    drawdown = (

        nav_series

        /

        running_max

        - 1

    )

    return drawdown.min()


# ====================================
# EXAMPLE USAGE
# ====================================

if __name__ == "__main__":

    print(
        "compute_metrics.py loaded successfully."
    )