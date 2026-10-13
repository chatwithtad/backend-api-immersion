import pandas as pd

# from analyze_504 import analyze_counties, analyze_industries

from analyze_504 import (
    analyze_counties,
    analyze_industries,
    analyze_years,
)

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

def test_analyze_years():
        test_data = pd.DataFrame({
            "ApprovalFY": [2024, 2024, 2025],
            "GrossApproval": [1_000_000, 3_000_000, 5_000_000],
            "JobsSupported": [10, 20, 40]
        })

        result = analyze_years(test_data)

        year_2024 = result[result["ApprovalFY"] == 2024].iloc[0]
        year_2025 = result[result["ApprovalFY"] == 2025].iloc[0]

        assert year_2024["LoanCount"] == 2
        assert year_2024["TotalApproval"] == 4_000_000
        assert year_2024["JobsSupported"] == 30
        assert year_2024["AverageLoanSize"] == 2_000_000

        assert year_2025["LoanCountYoYPercent"] == -50.0
        assert year_2025["ApprovalYoYPercent"] == 25.0


def test_analyze_industries_excludes_missing_naics_data():
    test_data = pd.DataFrame({
        "NaicsCode": ["624410", "624410", None],
        "NaicsDescription": [
            "Child Day Care Services",
            None,
            "Unknown Industry"
        ],
        "GrossApproval": [
            1_000_000,
            2_000_000,
            3_000_000
        ],
        "JobsSupported": [10, 20, 30]
    })

    result = analyze_industries(test_data)

    assert len(result) == 1

    childcare = result.iloc[0]

    assert childcare["NaicsCode"] == "624410"
    assert childcare["LoanCount"] == 1
    assert childcare["TotalApproval"] == 1_000_000
    assert childcare["JobsSupported"] == 10

