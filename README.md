# MPMD2.2 Dataset Explorer

Reference implementation for the kickoff workshop. Students normally build this app from an empty repository, step by step. Use the completed reference for catch-up and comparison.

## Data

12 synthetic customers. One customer per row. Customer ID and region are nominal labels. Tenure is recorded in whole months. Monthly charge is in EUR. Satisfaction has ordered labels low, medium, high without established equal distances. Cancelled is a historical binary outcome (0 = no, 1 = yes). C06 intentionally has a missing charge and C08 intentionally has a charge of 999. Preserve these while learning inspection. This dataset is too small and synthetic for reliable operational modeling.

## Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

## macOS / Linux

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python -m streamlit run app.py
```

## Codespaces

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Open port 8501 through the Codespaces Ports view. Locally, use http://localhost:8501. If `python` is unavailable in Codespaces, use `python3` consistently. Keep the server terminal running. Stop it with Ctrl+C. Select the `.venv` interpreter in desktop VS Code.

## Known outputs

All data: 12 rows, 6 columns, 1 missing charge, observed mean 138.45454..., median 55. All cancellations: 8 no and 4 yes.
North only: C01, C05, C09, median charge 35.
South only: 3 customers, 2 observed charges, median 64, 1 missing charge.
Empty selection: 0 customers and an informative message.

## Dependencies and reproducibility

The compatibility ranges in requirements.txt support the APIs used in the example. They are not an exact environment lock. After testing a project, record exact tested versions or follow the course's locking approach. Do not commit a virtual environment.

## Version history

Save, test, commit, and push. In a second clean working copy, pull before rerunning. Inspect conflicts and preserve work rather than discarding changes.
