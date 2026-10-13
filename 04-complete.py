"""Checkpoint 4 of 4: complete the dataset explorer.

This final stage retains checkpoint 03's filter and adds subset statistics and
charts. The empty-selection branch avoids presenting misleading summaries.
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

# Build the same sorted region control introduced in checkpoint 03.
regions = sorted(df["region"].dropna().unique())
selected = st.multiselect(
    "Regions", options=regions, default=regions
)
filtered = df[df["region"].isin(selected)]
st.subheader("Selected customers")
st.write("Selected rows:", len(filtered))
st.dataframe(filtered)

# Empty selections have no meaningful metrics or charts to display.
if filtered.empty:
    st.info("Choose at least one region to see customers.")
else:
    # count() excludes missing charges, unlike len(filtered).
    st.write("Observed charges:",
             filtered["monthly_charge"].count())
    st.write("Median selected charge:",
             filtered["monthly_charge"].median())
    st.subheader("Monthly charges")
    # Use customer IDs as chart labels instead of the default row index.
    chart_data = filtered.set_index("customer_id")
    st.bar_chart(chart_data[["monthly_charge"]])
    st.caption("Missing selected charges: " +
               str(filtered["monthly_charge"].isna().sum()))
    st.subheader("Cancellation counts")
    # Reindex keeps both outcomes visible even if one has no selected rows.
    counts = filtered["cancelled"].value_counts()
    counts = counts.reindex([0, 1], fill_value=0)
    counts.index = ["No", "Yes"]
    st.bar_chart(counts)
