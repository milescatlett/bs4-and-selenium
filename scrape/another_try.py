
import requests
from bs4 import BeautifulSoup

# Foothills Tasting Room
urls = [
    "https://plugin.eventscalendar.co/widget.html?pageId=rnzr4&compId=comp-jg2l6cob&viewerCompId=comp-jg2l6cob&siteRevision=69&viewMode=site&deviceType=desktop&locale=en&tz=America%2FNew_York&regionalLanguage=en&width=980&height=600&instance=bplNgPqFrXD115kQsFCdssYajjSx_ICEYK4iJPImA7E.eyJpbnN0YW5jZUlkIjoiMTA3MzVhYzAtYjNjOS00YzZhLTg2M2QtMzkxMThiMmQ0MWNiIiwiYXBwRGVmSWQiOiIxMzNiYjExZS1iM2RiLTdlM2ItNDliYy04YWExNmFmNzJjYWMiLCJzaWduRGF0ZSI6IjIwMjItMTItMDNUMTY6NDA6MDguMTM0WiIsInZlbmRvclByb2R1Y3RJZCI6InByZW1pdW0iLCJkZW1vTW9kZSI6ZmFsc2UsIm9yaWdpbkluc3RhbmNlSWQiOiI2MDNkODcyNi1hM2I3LTQ2YWItOTkzYi1hMzM0YjFmZTJmODIiLCJhaWQiOiI3MGU1OWNmNC00YzhjLTQ5NmItOGZhMC1kODU5MTFkZWQxY2UiLCJzaXRlT3duZXJJZCI6IjMxNDkwNGM4LTZkNWYtNGRiMS1hNzM2LTE4MDM5MmE5OGJmYiJ9&currency=USD&currentCurrency=USD&commonConfig=%7B%22brand%22%3A%22wix%22%2C%22bsi%22%3A%22adcc5aaf-81a9-4ade-94cb-da0ce6aa4115%7C2%22%2C%22BSI%22%3A%22adcc5aaf-81a9-4ade-94cb-da0ce6aa4115%7C2%22%7D&vsi=f03ef16b-a661-4171-9516-1f4fb446a770"
]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    events = soup.findAll('div', attrs={"class": "slide-container"})
    print(events)
