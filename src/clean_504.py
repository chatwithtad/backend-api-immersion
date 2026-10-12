from load_504 import load_504_data

selected_columns = [
    "AsOfDate",
    "Program",
    "LocationID",
    "BorrName",
    "BorrCity",
    "BorrState",
    "BorrZip",
    "CDC_Name",
    "ThirdPartyLender_Name",
    "ThirdPartyLender_State",
    "ThirdPartyDollars",
    "GrossApproval",
    "ApprovalDate",
    "ApprovalFY",
    "FirstDisbursementDate",
    "ProcessingMethod",
    "TermInMonths",
    "NaicsCode",
    "NaicsDescription",
    "FranchiseCode",
    "FranchiseName",
    "ProjectCounty",
    "ProjectState",
    "BusinessType",
    "BusinessAge",
    "LoanStatus",
    "PaidInFullDate",
    "ChargeOffDate",
    "GrossChargeOffAmount",
    "JobsSupported",
    "CollateralInd"
]

def clean_504_data():
    df = load_504_data()

    working_df = df[selected_columns].copy()

    # Standardize location fields so grouping is not split by
    # inconsistent capitalization or stray spaces

    working_df["ProjectState"] = (
        working_df["ProjectState"]
        .str.strip()
        .str.upper()
    )

    working_df["ProjectCounty"] = (
        working_df["ProjectCounty"]
        .str.strip()
        .str.upper()
    )

    # NAICS codes are identifiers, not quantities.
    # Convert float-like values such as 623312.0 to string labels like "623312"
    # while preserving missing values.

    working_df["NaicsCode"] = (
        working_df["NaicsCode"]
        .astype("Int64")
        .astype("string")
    )

    # Standardize industry descriptions so hidden whitespace
    # does not split identical industries into separate groups
    working_df["NaicsDescription"] = (
        working_df["NaicsDescription"]
        .str.strip()
    )

    return working_df


if __name__ == "__main__":
    working_df = clean_504_data()

    analysis_columns = [
        "ProjectState",
        "ProjectCounty",
        "NaicsCode",
        "NaicsDescription",
        "GrossApproval",
        "JobsSupported"
    ]

    print(working_df[analysis_columns].dtypes)

    print("\nMissing values:")
    print(working_df[analysis_columns].isna().sum())

    print("\nSample rows:")
    print(working_df[analysis_columns].head(10).to_string(index=False))
