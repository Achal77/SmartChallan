import os

import pandas as pd

from config import LOG_COLUMNS, LOG_FILE, ensure_runtime_directories


def load_log() -> pd.DataFrame:
    ensure_runtime_directories()
    if LOG_FILE.exists():
        return pd.read_csv(LOG_FILE)
    return pd.DataFrame(columns=LOG_COLUMNS)


def append_log(entry: dict) -> None:
    ensure_runtime_directories()
    dataframe = load_log()
    dataframe = pd.concat([dataframe, pd.DataFrame([entry])], ignore_index=True)
    dataframe.to_csv(LOG_FILE, index=False)
