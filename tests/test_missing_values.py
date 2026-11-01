import pandas as pd
import pytest

from data_science_project.validation import validate_no_missing_values

def test_validate_no_missing_values_accepts_complete_data():
    validate_no_missing_values(pd.DataFrame({"feature": [1, 2]}))

def test_validate_no_missing_values_reports_affected_columns():
    with pytest.raises(ValueError, match="feature"):
        validate_no_missing_values(pd.DataFrame({"feature": [1, None]}))
