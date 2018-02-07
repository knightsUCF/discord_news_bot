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




        
########################################################################################3

# -*- coding: utf-8 -*-

'''
import re

from bs4 import BeautifulSoup

from scrapy import Spider, Request, Item, Field




class RedditItem(Item):
	subreddit = Field()
	link = Field()
	title = Field()
	date = Field()
	vote = Field()
	top_comment = Field()


class RedditSpider(Spider):
	name = 'reddit'
	allowed_domains = ['reddit.com']
	start_urls = ['https://www.reddit.com/r/economics', 
				'https://www.reddit.com/r/forex', 
				'https://www.reddit.com/r/wallstreetbets',  
				'https://www.reddit.com/r/investing', 
				'https://www.reddit.com/r/cryptocurrency', 
				'https://www.reddit.com/r/cryptomarkets', 
				'https://www.reddit.com/r/economy', 
				'https://www.reddit.com/r/worldnews', 
				'https://www.reddit.com/r/algotrading', 
				'https://www.reddit.com/r/news']


	def parse(self, response):
		links = response.xpath('//p[@class="title"]/a[@class="title may-blank "]/@href').extract()
		titles = response.xpath('//p[@class="title"]/a[@class="title may-blank "]/text()').extract()
		dates = response.xpath('//p[@class="tagline"]/time[@class="live-timestamp"]/@title').extract()
		votes = response.xpath('//div[@class="midcol unvoted"]/div[@class="score unvoted"]/text()').extract()
		comments = response.xpath('//div[@id="siteTable"]//a[@class="comments may-blank"]/@href').extract()


		for i, link in enumerate(comments):
			item = RedditItem()
			item['subreddit'] = str(re.findall('/r/[A-Za-z]*8?', link))[3:len(str(re.findall('/r/[A-Za-z]*8?', link))) - 2]
			item['link'] = links[i]
			item['title'] = titles[i]
			item['date'] = dates[i]
			if votes[i] == u'\u2022':
				item['vote'] = 'hidden'
			else:
				item['vote'] = int(votes[i])

			request = Request(link, callback=self.parse_comment_page)
			request.meta['item'] = item

			yield request


	def parse_comment_page(self, response):
		item = response.meta['item']

		top = response.xpath('//div[@class="commentarea"]//div[@class="md"]').extract()[0]
		top_soup = BeautifulSoup(top, 'html.parser')
		item['top_comment'] = top_soup.get_text().replace('\n', ' ')

		yield item


test = RedditSpider()
'''







# run()



########################################################################################


#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
"""
Description:
    config for the Scraper.py
"""
# change these to your login details
username = "wizardsprite"
password = "7haso6kSRiv4RL0cjK1-NChQ0-U"
# aVWoqAzFdmvQWw
output_file = "scraped_data.pkl"
output_csv_file = "output.csv"

# UNIQUE ID FOR THE THREAD GOES HERE - GET FROM THE URL
# Set unique id or subreddit
uniq_id = 'https://www.reddit.com/r/Forex/'

## override this in config to decide which attributes to save from a comment object
#def comment_to_list(comment):
#    return [comment.author, comment.body]

"""
Description:
    1. Scrape all comments from a given reddit thread
    2. Extract top level comments
    3. Save to a csv file
Author:
    Copyright (c) Ian Hussey 2016 (ian.hussey@ugent.be) 
    Released under the GPLv3+ license.
Known issues:
    None. 
Notes:
    1. Although the script only uses publiclly available information, 
    PRAW's call to the reddit API requires a reddit login (see line 47).
    2. Reddit API limits number of calls (1 per second IIRC). 
    For a large thread (e.g., 1000s of comments) script execution time may therefore be c.1 hour.
    3. Because of this bottleneck, the entire data object is written to a pickle before anything is discarded. 
    This speeds up testing etc.
    4. Does not extract comment creation date (or other properties), which might be useful. 
"""


'''
# Dependencies
import praw
import csv
import os
import imp
import sys
import pickle
# import Scraper_config as cfg

# Set encoding to utf-8 rather than ascii, as is default for python 2.
# This avoids ascii errors on csv write.
imp.reload(sys)
# sys.setdefaultencoding('utf-8') 

# Change directory to that of the current script
absolute_path = os.path.abspath(__file__)
directory_name = os.path.dirname(absolute_path)
os.chdir(directory_name)

# Acquire comments via reddit API



r = praw.Reddit(user_agent = "News", client_id = "aVWoqAzFdmvQWw", client_secret = password)

# r.login(username, password, disable_warning=True)

# override this in config to decide which attributes to save from a comment object
def default_comment_to_list(comment):
    return [comment.body]

if hasattr(cfg, "comment_to_list"):
    comment_to_list = comment_to_list
else:
    comment_to_list = default_comment_to_list
 

def get_submission_comments(uniq_id):
    submission = r.submission(submission_id=uniq_id)  # UNIQUE ID FOR THE THREAD GOES HERE - GET FROM THE URL
    submission.replace_more_comments(limit=None, threshold=0)  # all comments, not just first page

    # Save object to pickle
    output = open(cfg.output_file, 'wb')
    pickle.dump(submission, output, -1)
    output.close()

    ## Load object from pickle
    # pkl_file = open(cfg.output_file, 'rb')
    # submission = pickle.load(pkl_file)
    ##pprint.pprint(submission)
    # pkl_file.close()

    # Extract first level comments only
    forest_comments = submission.comments  # get comments tree
    already_done = set()
    top_level_comments = []
    for comment in forest_comments:
        if not hasattr(comment, 'body'):  # only comments with body text
            continue
        if comment.is_root:  # only first level comments
            if comment.id not in already_done:
                already_done.add(comment.id)  # add it to the list of checked comments
                top_level_comments.append(comment_to_list(comment))  # append to list for saving
                # print(comment.body)
    return top_level_comments

def get_subreddit_comments(uniq_id):
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
    comStream = praw.helpers.comment_stream(r, uniq_id[3:], limit=limit) # Get the comment string
    comments = map(lambda _: [next(comStream).__str__()], range(limit)) # Get the raw string of each comment obj
    return list(comments) # Convert to list if running on Python3

# uniq_id = cfg.uniq_id
if len(sys.argv) > 1:
    uniq_id = sys.argv[1]

if uniq_id[:3] == '/r/':
    top_level_comments = get_subreddit_comments(uniq_id)
else:
    top_level_comments = get_submission_comments(uniq_id)

# Save comments to disk
with open(cfg.output_csv_file, "wb") as output:
    writer = csv.writer(output)
    writer.writerows(top_level_comments)
'''


import praw
import re

reddit = praw.Reddit(user_agent = "News", client_id = "aVWoqAzFdmvQWw", client_secret = password)





# Output: 10 submission

'''
from praw.models import MoreComments
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body)
'''

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

        if now.hour is 12 and now.minute is 0:
            output = 'Top 10 threads in https://www.reddit.com/r/investing : \n \n \n'
            number = 0
            for submission in reddit.subreddit('investing').hot(limit=10):
                number += 1
                output += (str(number) + '.' + ' ' + submission.title + '\n\n')
            data = { "content": output }
            requests.post(key, data=data)

        if now.hour is 13 and now.minute is 0:
            output = 'Top 10 threads in https://www.reddit.com/r/cryptomarkets : \n \n \n'
            number = 0
            for submission in reddit.subreddit('cryptomarkets').hot(limit=10):
                number += 1
                output += (str(number) + '.' + ' ' + submission.title + '\n\n')
            data = { "content": output }
            requests.post(key, data=data)

        if now.hour is 14 and now.minute is 0:
            output = 'Top 10 threads in https://www.reddit.com/r/algotrading : \n \n \n'
            number = 0
            for submission in reddit.subreddit('algotrading').hot(limit=10):
                number += 1
                output += (str(number) + '.' + ' ' + submission.title + '\n\n')
            data = { "content": output }
            requests.post(key, data=data)


run()
