import requests
from bs4 import BeautifulSoup as soup
from datetime import datetime

URLs = [
        "https://cloud.timeedit.net/hh/web/schema/ri1X5071Z4104vQQ3wZ5759Y63yY5Y67QQ.html",
        #"https://cloud.timeedit.net/hh/web/schema/ri1X5071Z6104vQQ3wZ5759Y64yY5Y67QQ.html",
        #"https://cloud.timeedit.net/hh/web/schema/ri1X5081Z5104vQQ3wZ5759Y60yY5Y67QQ.html"
        ]
roomNames = [
    "R3144",
    "R3147",
    "R4145"
]

currDayNumber = datetime.today().weekday()

for index, URL in enumerate(URLs):
    with requests.get(format(URL)) as page:
        soup = soup(page.text, 'html.parser')

    if not soup:
        break
    getcurrweekdaysHtml = soup.find_all("div", {"class": "weekDay"})
    currDaySoupHtml = getcurrweekdaysHtml[currDayNumber].find_all("div", {"class": "weekDiv"})[1]
    currDayTimeDivArr = currDaySoupHtml.find_all("div", {"class": "timeDiv"})

    bookingsToday = []

    for booking in currDayTimeDivArr[::-1]:
        bookingsToday.append(''.join(map(str, booking.contents)))

    if bookingsToday:
        for times in bookingsToday:
            print(times)
    else:
        print("its empty YAY!")