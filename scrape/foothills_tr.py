from bs4 import BeautifulSoup
import requests
from datetime import datetime


def fhtr():
    fht = []
    eid = 1
    urls = [
        "https://www.foothillsbrewing.com/events/category/tasting-room/",
        'https://www.foothillsbrewing.com/events/category/tasting-room/page/2/',
        'https://www.foothillsbrewing.com/events/category/tasting-room/page/3/'
    ]
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        events = soup.findAll('div', attrs={"class": "event row"})
        for event in events:
            event_header = event.find("h3").contents[0].strip()
            if 'Food' in event_header:
                if 'Food Truck – ' in event_header:
                    event_header = event_header.replace("Food Truck – ", "")
                elif " Food Truck" in event_header:
                    event_header = event_header.replace(" Food Truck", "")
                location = event.find("span", attrs={"class": "tastingRoom eventLabel"}).contents[0].strip()
                if location == 'Tasting':
                    location = 'Tasting Room - Foothills Brewing'
                event_date = event.find("span", attrs={"class": "date"}).contents[0].strip()
                event_time = event.find("span", attrs={"class": "time"}).contents[0].strip()
                times = event_time.split(' - ')
                start = datetime.strptime(event_date + ' ' + times[0], '%B %d, %Y %I:%M %p')
                end = datetime.strptime(event_date + ' ' + times[1], '%B %d, %Y %I:%M %p')
                uid = 'fhtr' + event_header + start.strftime("%m/%d/%Y %H:%M:%S") + end.strftime("%m/%d/%Y %H:%M:%S")
                eid += 1
                fht.append((location, event_header, start, end, eid, uid))
    return fht


print(fhtr())

