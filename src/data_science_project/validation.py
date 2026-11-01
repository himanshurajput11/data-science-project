from collections.abc import Sequence

import pandas as pd

def validate_no_missing_values(
    data: pd.DataFrame, columns: Sequence[str] | None = None
) -> None:
    """Raise ValueError when selected columns contain missing values."""
    selected = data if columns is None else data.loc[:, columns]
    missing = selected.columns[selected.isna().any()].tolist()
    if missing:
        raise ValueError(f"Missing values in columns: {missing}")
