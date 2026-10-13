from pathlib import Path
import pandas as pd
import streamlit as st

st.title("MPMD2.2 Dataset Explorer")
st.caption("Synthetic data for learning")
df = pd.read_csv(Path(__file__).with_name("customers.csv"))
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
regions = sorted(df["region"].dropna().unique())
selected = st.multiselect(
    "Regions", options=regions, default=regions
)
filtered = df[df["region"].isin(selected)]
st.subheader("Selected customers")
st.write("Selected rows:", len(filtered))
st.dataframe(filtered)
if filtered.empty:
    st.info("Choose at least one region to see customers.")
else:
    st.write("Observed charges:",
             filtered["monthly_charge"].count())
    st.write("Median selected charge:",
             filtered["monthly_charge"].median())
    st.subheader("Monthly charges")
    chart_data = filtered.set_index("customer_id")
    st.bar_chart(chart_data[["monthly_charge"]])
    st.caption("Missing selected charges: " +
               str(filtered["monthly_charge"].isna().sum()))
    st.subheader("Cancellation counts")
    counts = filtered["cancelled"].value_counts()
    counts = counts.reindex([0, 1], fill_value=0)
    counts.index = ["No", "Yes"]
    st.bar_chart(counts)
