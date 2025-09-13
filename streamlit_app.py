# app.py

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.title("Earnings Calendar")

# Load CSV
df = pd.read_csv("TVcal.csv")

# Parse DATE column (dd/mm/yyyy)
df["DATE"] = pd.to_datetime(df["DATE"], format="%d/%m/%Y", errors="coerce")

# Get start of this week (Monday) and next week
today = datetime.today()
start_of_week = today - timedelta(days=today.weekday())  # Monday this week
end_of_week = start_of_week + timedelta(days=6)          # Sunday this week

start_next_week = start_of_week + timedelta(days=7)
end_next_week = start_next_week + timedelta(days=6)

# Filter DataFrames
this_week_df = df[(df["DATE"] >= start_of_week) & (df["DATE"] <= end_of_week)]
next_week_df = df[(df["DATE"] >= start_next_week) & (df["DATE"] <= end_next_week)]

# Create Tabs
tab1, tab2 = st.tabs(["📅 This Week", "📅 Next Week"])

with tab1:
    st.subheader("This Week's Earnings")
    if this_week_df.empty:
        st.info("No earnings events this week.")
    else:
        st.dataframe(this_week_df)

with tab2:
    st.subheader("Next Week's Earnings")
    if next_week_df.empty:
        st.info("No earnings events next week.")
    else:
        st.dataframe(next_week_df)