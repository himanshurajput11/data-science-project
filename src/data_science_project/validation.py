from collections.abc import Sequence

import pandas as pd

def validate_required_columns(
    data: pd.DataFrame, required_columns: Sequence[str]
) -> None:
    """Raise ValueError when any required columns are absent."""
    missing = [column for column in required_columns if column not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
