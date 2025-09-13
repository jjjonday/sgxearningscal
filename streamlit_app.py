# app.py

import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_result_releases(url: str):
    """
    Scrape the InvestingNote page for Result Release events.
    Returns a DataFrame with the relevant info.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        st.error(f"Error fetching page: {resp.status_code}")
        return pd.DataFrame()  # empty

    soup = BeautifulSoup(resp.text, "html.parser")

    # This part depends on how the events are structured in HTML. You need to inspect the page.
    # Hypothetical selectors:
    # Let's say each event is in a <div class="event-item">, inside which
    # there's a date, company name, maybe a link, etc.
    events = []
    for item in soup.find_all("div", class_="event-item"):
        # adjust these according to actual structure
        date_el = item.find("span", class_="event-date")
        company_el = item.find("a", class_="company-name")
        detail_el = item.find("span", class_="event-detail")

        date = date_el.get_text(strip=True) if date_el else None
        company = company_el.get_text(strip=True) if company_el else None
        detail = detail_el.get_text(strip=True) if detail_el else None

        events.append({
            "Date": date,
            "Company": company,
            "Detail": detail
        })

    df = pd.DataFrame(events)
    return df

def main():
    st.title("InvestingNote Result Release Events")

    url = st.text_input(
        "Enter URL", 
        "https://www.investingnote.com/stock_events/calendar?event_type=result_release&source=&country="
    )

    if st.button("Fetch Events"):
        with st.spinner("Scraping data..."):
            df = scrape_result_releases(url)
        if df.empty:
            st.write("No events found. Possibly structure has changed or content needs login / JS rendering.")
        else:
            st.dataframe(df)

if __name__ == "__main__":
    main()
#1. Scrape TradingView for This week + next week data. 
#2. show it in the dashboard. Maybe create a selector to select companies and show a more granular dashboard
#3. email capability? 
