from collections.abc import Sequence

import pandas as pd


def _normalize_columns(columns: Sequence[str] | str | None) -> list[str] | None:
    """Turn a scalar string or sequence into a list of column names."""
    if columns is None:
        return None
    if isinstance(columns, str):
        return [columns]
    return list(columns)


def validate_no_missing_values(
    data: pd.DataFrame, columns: Sequence[str] | str | None = None
) -> None:
    """Raise ValueError when selected columns contain missing values."""
    normalized = _normalize_columns(columns)
    selected = data if normalized is None else data.loc[:, normalized]
    missing = selected.columns[selected.isna().any()].tolist()
    if missing:
        raise ValueError(f"Missing values in columns: {missing}")


def validate_required_columns(
    data: pd.DataFrame, required_columns: Sequence[str] | str
) -> None:
    """Raise ValueError when any required columns are absent."""
    normalized = _normalize_columns(required_columns)
    missing = [column for column in normalized if column not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
