from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


service = Service(executable_path="/workspaces/sgxearningscal/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.investingnote.com/stock_events/calendar?event_type=result_release&source=&country=")

time.sleep(10)

driver.quit()
#1. Scrape TradingView for This week + next week data. 
#2. show it in the dashboard. Maybe create a selector to select companies and show a more granular dashboard
#3. email capability? 
