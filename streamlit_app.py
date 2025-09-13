import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Static Page Cloner")

url = st.text_input("Enter a URL:", "https://example.com")

if st.button("Clone Page"):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")

        # Optional: strip scripts for safety
        for tag in soup(["script", "style"]):
            tag.decompose()

        # Render
        st.components.v1.html(str(soup), height=800, scrolling=True)
    else:
        st.error(f"Failed: {r.status_code}")