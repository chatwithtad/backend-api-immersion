from pathlib import Path
import pandas as pd


def load_504_data():
    project_root = Path(__file__).resolve().parent.parent
    file_path = (
        project_root
        / "data"
        / "raw"
        / "FOIA_504_FY2010_Present_asof_260630.csv"
    )

    df = pd.read_csv(file_path)

    return df


if __name__ == "__main__":
    df = load_504_data()
    print(df.shape)
