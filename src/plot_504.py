from pathlib import Path

import matplotlib.pyplot as plt

from analyze_504 import get_georgia_data, analyze_years

def plot_yearly_approvals(yearly_summary):
    # FY2026 is partial through June 30, so it's excluded
    # from the completed-year comparison.
    completed_years = yearly_summary[
        yearly_summary["ApprovalFY"] < 2026
    ].copy()

    plt.figure(figsize=(10, 6))

    plt.plot(
        completed_years["ApprovalFY"],
        completed_years["TotalApprovalMillions"],
        marker="o"
    )

    plt.title("Georgia SBA 504 Total Approvals by Fiscal Year")
    plt.xlabel("Fiscal Year")
    plt.ylabel("Total Approval ($ Millions)")

    plt.tight_layout()

    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "outputs"

    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / "georgia_504_approvals_by_year.png"

    plt.savefig(output_path, dpi=300)
    plt.show()

    return output_path

if __name__ == "__main__":
    georgia_df = get_georgia_data()
    yearly_summary = analyze_years(georgia_df)

    chart_path = plot_yearly_approvals(yearly_summary)

    print(f"Chart saved to: {chart_path}")
