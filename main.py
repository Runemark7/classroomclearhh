import requests
from bs4 import BeautifulSoup as soup
from datetime import datetime

URLs = [
    "https://cloud.timeedit.net/hh/web/schema/ri1X5071Z4104vQQ3wZ5759Y63yY5Y67QQ.html",
    "https://cloud.timeedit.net/hh/web/schema/ri1X5071Z6104vQQ3wZ5759Y64yY5Y67QQ.html",
    "https://cloud.timeedit.net/hh/web/schema/ri1X5071Z0104vQQ3wZ5759Y64yY5Y67QQ.html",
    "https://cloud.timeedit.net/hh/web/schema/ri1X5071Z1104vQQ3wZ5759Y64yY5Y67QQ.html",
    "https://cloud.timeedit.net/hh/web/schema/ri1X5081Z5104vQQ3wZ5759Y60yY5Y67QQ.html",
    "https://cloud.timeedit.net/hh/web/schema/ri1X5081Z3104vQQ3wZ5759Y60yY5Y67QQ.html"
]
roomNames = [
    "R3144",
    "R3147",
    "R3145",
    "R3336",
    "R4145",
    "R4341"
]

currDayNumber = datetime.today().weekday()
for i in range(len(URLs)):
    print(roomNames[i])

    page = requests.get(URLs[i])
    page_soup = soup(page.text, "html.parser")

    getcurrweekdaysHtml = page_soup.find_all("div", {"class": "weekDay"})
    currDaySoupHtml = getcurrweekdaysHtml[currDayNumber].find_all("div", {"class": "weekDiv"})[1]
    currDayTimeDivArr = currDaySoupHtml.find_all("div", {"class": "timeDiv"})

    bookingsToday = []

    for index in range(0, len(currDayTimeDivArr), 2):
        endTime = currDayTimeDivArr[index]
        startTime = currDayTimeDivArr[index+1]
        bookingsToday.append(startTime.text + " - " + endTime.text)

    if bookingsToday:
        for times in bookingsToday:
            print(times)
    else:
        print("its empty YAY!")
