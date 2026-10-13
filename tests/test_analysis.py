import pandas as pd

from analyze_504 import analyze_counties, analyze_industries


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

def test_analyze_industries_groups_by_naics_code():
    test_data = pd.DataFrame({
        "NaicsCode": ["624410", "624410", "722511"],
        "NaicsDescription": [
            "Child Day Care Services",
            "Child Care Services",
            "Full-Service Restaurants"
        ],
        "GrossApproval": [1_000_000, 2_000_000, 1_000_000],
        "JobsSupported": [10, 20, 5]
    })

    result = analyze_industries(test_data)

    childcare = result[result["NaicsCode"] == "624410"].iloc[0]

    assert childcare["LoanCount"] == 2
    assert childcare["TotalApproval"] == 3_000_000
    assert childcare["JobsSupported"] == 30
    assert childcare["JobsPerMillion"] == 10.0