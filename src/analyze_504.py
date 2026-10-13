from clean_504 import clean_504_data

def get_georgia_data():
    df = clean_504_data()

    georgia_df = df[df["ProjectState"] == "GA"].copy()

    return georgia_df

def analyze_counties(georgia_df):

    # group and aggregate

    county_summary = (
        georgia_df
        .groupby("ProjectCounty")
        .agg(
            LoanCount=("ProjectCounty", "size"),
            TotalApproval=("GrossApproval", "sum"),
            JobsSupported=("JobsSupported", "sum")
        )
        .reset_index()
    )

    # calculate jobs associated with each $1M approved

    county_summary["JobsPerMillion"] = (
            county_summary["JobsSupported"]
            / (county_summary["TotalApproval"] / 1_000_000)
    ).round(2)

    # rank by total approval dollars

    county_summary = county_summary.sort_values(
        "TotalApproval",
        ascending=False
    )

    return county_summary

def analyze_industries(georgia_df):
    # Industry analysis requires both a NAICS code and description
    industry_df = georgia_df.dropna(
        subset=["NaicsCode", "NaicsDescription"]
    ).copy()

    industry_summary = (
        industry_df
        .groupby("NaicsCode")
        .agg(
            NaicsDescription=("NaicsDescription", "first"),
            LoanCount=("NaicsCode", "size"),
            TotalApproval=("GrossApproval", "sum"),
            JobsSupported=("JobsSupported", "sum")
        )
        .reset_index()
    )

    # Calculate jobs associated with each $1M approved
    industry_summary["JobsPerMillion"] = (
        industry_summary["JobsSupported"]
        / (industry_summary["TotalApproval"] / 1_000_000)
    ).round(2)

    # Rank industries by total approval dollars
    industry_summary = industry_summary.sort_values(
        "TotalApproval",
        ascending=False
    )

    return industry_summary

def analyze_years(georgia_df):
    yearly_summary = (
        georgia_df
        .groupby("ApprovalFY")
        .agg(
            LoanCount=("ApprovalFY", "size"),
            TotalApproval=("GrossApproval", "sum"),
            JobsSupported=("JobsSupported", "sum"),
            AverageLoanSize=("GrossApproval", "mean")
        )
        .reset_index()
        .sort_values("ApprovalFY")
    )

    yearly_summary["TotalApprovalMillions"] = (
            yearly_summary["TotalApproval"] / 1_000_000
    ).round(2)

    yearly_summary["AverageLoanSize"] = (
        yearly_summary["AverageLoanSize"]
        .round(0)
    )

    # Express total approvals in millions for easier reading
    yearly_summary["TotalApprovalMillions"] = (
            yearly_summary["TotalApproval"] / 1_000_000
    ).round(2)

    # Round average loan size to the nearest dollar
    yearly_summary["AverageLoanSize"] = (
        yearly_summary["AverageLoanSize"]
        .round(0)
    )

    # Calculate year-over-year percentage change
    yearly_summary["LoanCountYoYPercent"] = (
        yearly_summary["LoanCount"]
        .pct_change()
        .mul(100)
        .round(2)
    )

    yearly_summary["ApprovalYoYPercent"] = (
        yearly_summary["TotalApproval"]
        .pct_change()
        .mul(100)
        .round(2)
    )

    return yearly_summary


if __name__ == "__main__":
    georgia_df = get_georgia_data()

    # county_summary = analyze_counties(georgia_df)
    # industry_summary = analyze_industries(georgia_df)

    # print("\nTop 10 Georgia counties by SBA 504 approval:")
    # print(county_summary.head(10).to_string(index=False))

    # print("\nTop 10 Georgia industries by SBA 504 approval:")
    # print(industry_summary.head(10).to_string(index=False))

    #

    yearly_summary = analyze_years(georgia_df)

    print("\nGeorgia SBA 504 activity by fiscal year:")
    print(yearly_summary.to_string(index=False))
