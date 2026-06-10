import pandas as pd

perf = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

risk_map = {

    'Low':['Low'],

    'Moderate':['Moderate'],

    'High':['High']

}

recommended = perf[
    perf['risk_grade']
    .isin(
        risk_map[risk]
    )
]

recommended = (

    recommended

    .sort_values(
        'sharpe_ratio',
        ascending=False
    )

    .head(3)

)

print(

    recommended[
        [
            'scheme_name',
            'sharpe_ratio',
            'risk_grade'
        ]
    ]

)