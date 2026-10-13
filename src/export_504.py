from pathlib import Path

# importing four functions from previous modules

from analyze_504 import (
    get_georgia_data,
    analyze_counties,
    analyze_industries,
    analyze_years,
)

def export_summaries():
    georgia_df = get_georgia_data()

# three finished DataFrames

    county_summary = analyze_counties(georgia_df)
    industry_summary = analyze_industries(georgia_df)
    yearly_summary = analyze_years(georgia_df)

    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "outputs"

    output_dir.mkdir(exist_ok=True)

# where the DataFrames will be saved

    county_summary.to_csv(
        output_dir / "georgia_county_summary.csv",
        index=False
    )

    industry_summary.to_csv(
        output_dir / "georgia_industry_summary.csv",
        index=False
    )

    yearly_summary.to_csv(
        output_dir / "georgia_yearly_summary.csv",
        index=False
    )

    return output_dir

if __name__ == "__main__":
    output_dir = export_summaries()

    print(f"Summary files saved to: {output_dir}")
