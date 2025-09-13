# app.py

import streamlit as st
import requests

def fetch_page(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    return resp.text if resp.status_code == 200 else f"Error: {resp.status_code}"

def main():
    st.title("Raw HTML Viewer")

    url = st.text_input(
        "Enter URL", 
        "https://www.investingnote.com/stock_events/calendar?event_type=result_release&source=&country="
    )

    if st.button("Fetch Page"):
        with st.spinner("Fetching page..."):
            html = fetch_page(url)
        st.text_area("Raw HTML Content", html, height=600)

if __name__ == "__main__":
    main()