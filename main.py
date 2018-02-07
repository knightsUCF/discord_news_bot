import re
import time
import datetime
from bs4 import BeautifulSoup
import requests
import datetime
import logging
import csv


key = 'https://discordapp.com/api/webhooks/410551199306350592/tutRZuB8tJpCqAS3pTOat01WSzbSPVwyojb3xCLyab-j1agQ2Vh0MKMW2xSeBez1n-_F'
news = []




def getEconomicCalendar(startlink,endlink):
    baseURL = "https://www.forexfactory.com/"
    r = requests.get(baseURL + startlink)
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    table = soup.find("table", class_="calendar__table")
    trs = table.select("tr.calendar__row.calendar_row")
    fields = ["date","time","currency","impact","event","actual","forecast","previous"]
    curr_year = startlink[-4:]
    curr_date = ""
    curr_time = ""
    for tr in trs:
        try:
            for field in fields:
                data = tr.select("td.calendar__cell.calendar__{}.{}".format(field,field))[0]
                if field=="date" and data.text.strip()!="":
                    curr_date = data.text.strip()
                elif field=="time" and data.text.strip()!="":
                    # time is sometimes "All Day" or "Day X" (eg. WEF Annual Meetings)
                    if data.text.strip().find("Day")!=-1:
                        curr_time = "12:00am"
                    else:
                        curr_time = data.text.strip()
                elif field=="currency":
                    currency = data.text.strip()
                elif field=="impact":
                    impact = data.find("span")["title"]
                elif field=="event":
                    event = data.text.strip()
                elif field=="actual":
                    actual = data.text.strip()
                elif field=="forecast":
                    forecast = data.text.strip()
                elif field=="previous":
                    previous = data.text.strip()
                

            dt = datetime.datetime.strptime(",".join([curr_year,curr_date,curr_time]), "%Y,%a%b %d,%I:%M%p")
            news.append(str(dt) + '  ' + currency + ' ' + impact + ' -- ' + event + '\n')
           

        except:
            print('something went wrong')
    if startlink==endlink:
        return


while True:
    now = datetime.datetime.now()
    if now.hour is 19:
        getEconomicCalendar("calendar.php?day=feb6.2018","calendar.php?day=feb6.2018")
        output = ''.join(news)
        data = { "content": output }
        requests.post(key, data=data)
    time.sleep(20000)

    
