import requests
from bs4 import BeautifulSoup
import time
from csv import writer
import datetime
from splinter import Browser

# url = 'https://www.buzzfeed.com/'
browser = Browser('chrome')
url = 'http://www.calnewport.com/blog'
blogtitle = {'class_': 'blogtitle'}
dateposted = 'small'


response = requests.get(url)
time.sleep(2)
# sleep so that the website doesn't think you're a robot

soup = BeautifulSoup(response.text, 'html.parser')
# initializes Beautiful Soup Library

posts = soup.find_all('article')

with open ('post.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Link', 'Date', 'Date and Time Pulled']
    csv_writer.writerow(headers)

    for post in posts:
        timestamp = datetime.datetime.now()
        title = post.find(**blogtitle).get_text()
        links = post.find('a')['href']
        date = post.find(dateposted).getText()
        csv_writer.writerow([title, links, date, timestamp])
        # print(title, links, date)

# 1. Find more sites and aggregate the data into the csv format that you've defined.
# 2. Append new information to the bottom of the csv (or create new csvs) includiding date information
# (look into the datetime module)
# 3. Find a non-static website (e.g. one that doesn't load at runtime) and use selenium or a variant of it to automate
# the browser actually opening
# to get the data