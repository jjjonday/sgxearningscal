import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Wide mode
st.set_page_config(layout="wide")

# Load CSV
df = pd.read_csv("TVcal.csv", dayfirst=True)

# Convert DATE column to datetime
df["DATE"] = pd.to_datetime(df["DATE"], format="%d/%m/%Y")

today = datetime.today().date()
start_week = today - timedelta(days=today.weekday())  # Monday
end_week = start_week + timedelta(days=6)
next_week_start = end_week + timedelta(days=1)
next_week_end = next_week_start + timedelta(days=6)

this_week = df[(df["DATE"].dt.date >= start_week) & (df["DATE"].dt.date <= end_week)]
next_week = df[(df["DATE"].dt.date >= next_week_start) & (df["DATE"].dt.date <= next_week_end)]

tab1, tab2 = st.tabs(["This Week", "Next Week"])

with tab1:
    st.subheader("This Week’s Earnings")
    st.dataframe(this_week, use_container_width=True)

with tab2:
    st.subheader("Next Week’s Earnings")
    st.dataframe(next_week, use_container_width=True)