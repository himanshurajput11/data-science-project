import pandas as pd
import pytest

from data_science_project import validate_no_missing_values
from data_science_project.validation import validate_no_missing_values as validate_no_missing_values_module


def test_validate_no_missing_values_accepts_complete_data():
    validate_no_missing_values(pd.DataFrame({"feature": [1, 2]}))


def test_validate_no_missing_values_accepts_single_column_name():
    validate_no_missing_values(pd.DataFrame({"feature": [1, 2]}), "feature")
    assert validate_no_missing_values is validate_no_missing_values_module


def test_validate_no_missing_values_reports_affected_columns():
    with pytest.raises(ValueError, match="feature"):
        validate_no_missing_values(pd.DataFrame({"feature": [1, None]}))
