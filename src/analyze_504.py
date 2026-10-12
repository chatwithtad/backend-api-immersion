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

if __name__ == "__main__":
    georgia_df = get_georgia_data()

    # print(georgia_df.shape)
    # print(georgia_df["ProjectState"].value_counts())
    county_summary = analyze_counties(georgia_df)

    print(county_summary.head(10).to_string(index=False))