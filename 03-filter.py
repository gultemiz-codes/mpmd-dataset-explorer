"""Checkpoint 3 of 4: add an interactive region filter.

It builds on checkpoint 02's preview and inspection sections. The selected
regions produce a filtered dataframe; checkpoint 04 adds metrics and charts
for that subset, including a useful empty-selection state.
"""

from pathlib import Path
import pandas as pd
import streamlit as st

st.title("MPMD2.2 Dataset Explorer")
st.caption("Synthetic data for learning")
data_path = Path(__file__).with_name("customers.csv")
if not data_path.exists():
    data_path = Path(__file__).parent.parent / "customers.csv"
df = pd.read_csv(data_path)
st.subheader("Data preview")
st.dataframe(df)
st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])
st.subheader("Storage types")
st.dataframe(df.dtypes.astype(str))
st.subheader("Missing values")
st.dataframe(df.isna().sum().rename("missing"))
st.subheader("Numerical summary")
st.dataframe(df.describe())
st.write("Mean charge:", df["monthly_charge"].mean())
st.write("Median charge:", df["monthly_charge"].median())

# Drop missing region labels and sort options for a predictable control.
regions = sorted(df["region"].dropna().unique())
selected = st.multiselect(
    "Regions", options=regions, default=regions
)

# isin() keeps rows whose region is among the selected options.
filtered = df[df["region"].isin(selected)]
st.subheader("Selected customers")
st.write("Selected rows:", len(filtered))
st.dataframe(filtered)
