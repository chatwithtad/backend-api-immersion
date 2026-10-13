import pandas as pd

from analyze_504 import analyze_counties


def test_analyze_counties():
    test_data = pd.DataFrame({
        "ProjectCounty": ["FULTON", "FULTON", "COBB"],
        "GrossApproval": [1_000_000, 2_000_000, 1_000_000],
        "JobsSupported": [10, 20, 5]
    })

    result = analyze_counties(test_data)

    fulton = result[result["ProjectCounty"] == "FULTON"].iloc[0]

    assert fulton["LoanCount"] == 2
    assert fulton["TotalApproval"] == 3_000_000
    assert fulton["JobsSupported"] == 30
    assert fulton["JobsPerMillion"] == 10.0
