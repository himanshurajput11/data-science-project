import pandas as pd
import pytest

from data_science_project.validation import validate_required_columns

def test_validate_required_columns_accepts_complete_schema():
    validate_required_columns(pd.DataFrame({"feature": [1], "target": [0]}), ["feature", "target"])

def test_validate_required_columns_reports_missing_names():
    with pytest.raises(ValueError, match="[Mm]issing.*target"):
        validate_required_columns(pd.DataFrame({"feature": [1]}), ["feature", "target"])
import pandas as pd
import pytest

from data_science_project.validation import validate_required_columns

def test_validate_required_columns_accepts_complete_schema():
    validate_required_columns(pd.DataFrame({"feature": [1], "target": [0]}), ["feature", "target"])

def test_validate_required_columns_reports_missing_names():
    with pytest.raises(ValueError, match="missing.*target"):
        validate_required_columns(pd.DataFrame({"feature": [1]}), ["feature", "target"])
