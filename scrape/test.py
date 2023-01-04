
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://plugin.eventscalendar.co/widget.html?pageId=rnzr4&compId=comp-jg2l6cob&viewerCompId=comp-jg2l6cob&siteRevision=69&viewMode=site&deviceType=desktop&locale=en&tz=America%2FNew_York&regionalLanguage=en&width=980&height=600&instance=bplNgPqFrXD115kQsFCdssYajjSx_ICEYK4iJPImA7E.eyJpbnN0YW5jZUlkIjoiMTA3MzVhYzAtYjNjOS00YzZhLTg2M2QtMzkxMThiMmQ0MWNiIiwiYXBwRGVmSWQiOiIxMzNiYjExZS1iM2RiLTdlM2ItNDliYy04YWExNmFmNzJjYWMiLCJzaWduRGF0ZSI6IjIwMjItMTItMDNUMTY6NDA6MDguMTM0WiIsInZlbmRvclByb2R1Y3RJZCI6InByZW1pdW0iLCJkZW1vTW9kZSI6ZmFsc2UsIm9yaWdpbkluc3RhbmNlSWQiOiI2MDNkODcyNi1hM2I3LTQ2YWItOTkzYi1hMzM0YjFmZTJmODIiLCJhaWQiOiI3MGU1OWNmNC00YzhjLTQ5NmItOGZhMC1kODU5MTFkZWQxY2UiLCJzaXRlT3duZXJJZCI6IjMxNDkwNGM4LTZkNWYtNGRiMS1hNzM2LTE4MDM5MmE5OGJmYiJ9&currency=USD&currentCurrency=USD&commonConfig=%7B%22brand%22%3A%22wix%22%2C%22bsi%22%3A%22adcc5aaf-81a9-4ade-94cb-da0ce6aa4115%7C2%22%2C%22BSI%22%3A%22adcc5aaf-81a9-4ade-94cb-da0ce6aa4115%7C2%22%7D&vsi=f03ef16b-a661-4171-9516-1f4fb446a770")
title = driver.title
driver.implicitly_wait(60)
links = driver.find_elements(By.PARTIAL_LINK_TEXT, value=" ")
event_list = []
for link in links:
    link.click()
    events = driver.find_elements(by=By.CLASS_NAME, value="popup-body")
    time.sleep(0.02)
    for event in events:
        event = event.text.split("\n")
        if "Open" not in event[0] \
                and "Vinyl" not in event[0] \
                and "$" not in event[0] \
                and "USA" not in event[0] \
                and "Trivia" not in event[0] \
                and "Music" not in event[0]\
                and "Party" not in event[0]\
                and "Boulder" not in event[0]\
                and len(event) == 3:
            event_list.append(event)
    driver.find_element(by=By.CLASS_NAME, value="popup-close").click()
    time.sleep(0.02)

print(event_list)
driver.quit()

