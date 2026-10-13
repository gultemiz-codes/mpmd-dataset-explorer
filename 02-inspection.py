"""Checkpoint 2 of 4: add basic data inspection to the preview.

It retains checkpoint 01's table and dimensions, then examines storage types,
missing values, and numeric distributions. Checkpoint 03 adds region filtering.
"""

from pathlib import Path
import pandas as pd
import streamlit as st

st.title("MPMD2.2 Dataset Explorer")
st.caption("Synthetic data for learning")
# Checkpoints can run here or from the project root after copying into app.py.
data_path = Path(__file__).with_name("customers.csv")
if not data_path.exists():
	data_path = Path(__file__).parent.parent / "customers.csv"
df = pd.read_csv(data_path)
st.subheader("Data preview")
st.dataframe(df)
st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])

# Inspect types and missingness before interpreting the numeric summaries.
st.subheader("Storage types")
st.dataframe(df.dtypes.astype(str))
st.subheader("Missing values")
st.dataframe(df.isna().sum().rename("missing"))

# describe() summarizes numeric columns; mean and median focus on monthly charge.
st.subheader("Numerical summary")
st.dataframe(df.describe())
st.write("Mean charge:", df["monthly_charge"].mean())
st.write("Median charge:", df["monthly_charge"].median())
