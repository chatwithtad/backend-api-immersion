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

if __name__ == "__main__":
    georgia_df = get_georgia_data()

    for code in ["721110", "722511"]:
        print(f"\nDescriptions for NAICS {code}:")

        descriptions = (
            georgia_df.loc[
                georgia_df["NaicsCode"] == code,
                "NaicsDescription"
            ]
            .value_counts()
        )

        for description, count in descriptions.items():
            print(repr(description), count)

    # print(georgia_df.shape)
    # print(georgia_df["ProjectState"].value_counts())
    county_summary = analyze_counties(georgia_df)
    industry_summary = analyze_industries(georgia_df)

    print("\nTop 10 Georgia counties by SBA 504 approval:")
    print(county_summary.head(10).to_string(index=False))

    print("\nTop 10 Georgia industries by SBA 504 approval:")
    print(industry_summary.head(10).to_string(index=False))
