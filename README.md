# Data Science Project

A Python starter repository for reproducible data analysis and machine-learning work.

## Getting started

Create and activate a virtual environment, then install the project and development
dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Run the test suite with:

```powershell
python -m pytest
```

## Project layout

- `src/data_science_project/` — reusable project code
- `tests/` — automated tests
- `data/raw/` and `data/processed/` — local data directories

Data files, model artifacts, virtual environments, and local secrets are excluded
from version control. Do not commit credentials or data you do not have permission
to publish. Document data sources, licenses, and reproducible preparation steps
before sharing results.
