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




def get_economic_calendar(startlink,endlink):
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
            print('Oops! Something went wrong...')

    if startlink == endlink:
        return



def date(month_day):
    chars = 'calendar.php?day=MONTHDAY.2018'
    subbed = re.sub('MONTHDAY', month_day, chars)
    return subbed



def get_month():
    formatted_month = ''
    d = datetime.date.today()
    month = d.month
    if month is 1:
        formatted_month = 'jan'
    if month is 2:
        formatted_month = 'feb'
    if month is 3:
        formatted_month = 'march'
    if month is 4:
        formatted_month = 'apr'
    if month is 5:
        formatted_month = 'may'
    if month is 6:
        formatted_month = 'jun'
    if month is 7:
        formatted_month = 'jul'
    if month is 8:
        formatted_month = 'aug'
    if month is 9:
        formatted_month = 'sep'
    if month is 10:
        formatted_month = 'oct'
    if month is 11:
        formatted_month = 'nov'
    if month is 12:
        formatted_month = 'dec'
    return formatted_month



def get_day():
    d = datetime.date.today()
    return str(d.day)



def get_complete_date():
     calendar_date = get_month() + get_day()
     return calendar_date



def run():
    while True:

        time.sleep(60)
        
        now = datetime.datetime.now()
        
        if now.hour is 0 and now.minute is 0:
            get_economic_calendar(date(get_complete_date()),date(get_complete_date()))
            output = ''.join(news)
            data = { "content": output }
            requests.post(key, data=data)

        if now.hour is 2 and now.minute is 45:
            output = 'London market opens in 15 minutes'
            data = { "content": output }
            requests.post(key, data=data)

        if now.hour is 3 and now.minute is 0:
            output = 'London Market Open'
            data = { "content": output }
            requests.post(key, data=data)

        if now.hour is 7 and now.minute is 45:
            data = {"content": "New York market opens in 15 minutes"}
            requests.post(key, data=data)

        if now.hour is 8 and now.minute is 0:
            output = 'New York Market Open'
            data = { "content": output }
            requests.post(key, data=data)

        if now.hour is 9 and now.minute is 15:
            data = {"content": "New York equities market opens in 15 minutes"}
            requests.post(key, data=data)

        if now.hour is 9 and now.minute is 30:
            data = {"content": "New York Equities Market Open"}
            requests.post(key, data=data)

        if now.hour is 15 and now.minute is 45:
            data = {"content": "Sydney market opens in 15 minutes"}
            requests.post(key, data=data)

        if now.hour is 16 and now.minute is 0:
            output = 'Sydney Market Open'
            data = { "content": output }
            requests.post(key, data=data)

        if now.hour is 17 and now.minute is 45:
            data = {"content": "Tokyo market opens in 15 minutes"}
            requests.post(key, data=data)

        if now.hour is 18 and now.minute is 0:
            output = 'Tokyo Market Open'
            data = { "content": output }
            requests.post(key, data=data)
        
        
run()
