import pandas as pd
import os
from app.config import DATA_PATH

def load_dataframe():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(project_root, DATA_PATH)

    df = pd.read_excel(data_path)
    df["date"] = pd.to_datetime(df["date"])
    return df