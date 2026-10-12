from pathlib import Path
import pandas as pd
import os
# print(os.getcwd())

project_root = Path(__file__).resolve().parent.parent
file_path = project_root / "data" / "raw" / "FOIA_504_FY2010_Present_asof_260630.csv"

df = pd.read_csv(file_path)

# print(df.head())
# print(df.dtypes)

# print(df.shape)
# print(df.columns)

# df.info()

# Sort fields by missing-value count to inspect incomplete or conditionally blank data
# print(df.isna().sum().sort_values(ascending=False))

# Import the SBA dictionary to confirm field definition
dictionary_df = pd.read_excel(
    "data/raw/7a_504_foia_data_dictionary.xlsx"
)

# Show full text in long DataFrame columns
pd.set_option("display.max_colwidth", None)

# print(dictionary_df.shape)
# print(dictionary_df.columns)
# print(dictionary_df.head(10))

# cdc_definitions = dictionary_df[
#     dictionary_df["Field Name"].str.contains("CDC", case=False, na=False)
# ]
#
# print(cdc_definitions)

# excel_file = pd.ExcelFile(
#     "data/raw/7a_504_foia_data_dictionary.xlsx"
# )
#
# print(excel_file.sheet_names)

dictionary_df = pd.read_excel(
    "data/raw/7a_504_foia_data_dictionary.xlsx",
    sheet_name="504 Data Dictionary"
)

# cdc_definitions = dictionary_df[
#     dictionary_df["Field Name"].str.contains("CDC", case=False, na=False)
# ]
#
# print(cdc_definitions)

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

working_df = df[selected_columns].copy()

print(working_df.shape)
print(working_df.columns)



# print(df[selected_columns].head(10))
