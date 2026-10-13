"""Checkpoint 1 of 4: load the customer data and preview its shape.

This is the starting point. Checkpoint 02 keeps this preview and adds
inspection of column types, missing values, and numeric summaries.
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

# Start with the raw rows, then show the dataset dimensions.
st.subheader("Data preview")
st.dataframe(df)
st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])
