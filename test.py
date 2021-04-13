# Import the Libraries #

from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib.request
import pyttsx3
from datetime import *

today_date = str(date.today())
print(today_date)


# Create the required dictionaries #
authors = []
quotes = []


#Function that gets the request from the website#

def quote_scraper(theme):
    theme = str(theme)
    URL = f'https://www.goodreads.com/quotes/tag/{theme}'
    webpage = requests.get(URL)
    soup = BeautifulSoup(webpage.text , 'html.parser')
    quote_text = soup.find_all('div', attrs = {'class':'quoteText'})

    for i in quote_text:

        quote = i.text.strip().split('\n')[0] 
        #print(quote)
        author = i.find('span',attrs={'class':'authorOrTitle'})
        author = author.text.strip()
        #print(author)
        quotes.append(quote)
        authors.append(author)
    

quote_scraper('love')
print(quotes)
print(authors)

#This opens a new folder and saves a single quote in it#
q_saver = open(r"qsaved.txt","w+")
q_saver.writelines(quotes[7])
q_saver.writelines(authors[7])



#this narrates the particular quote#
engine = pyttsx3.init()
engine.setProperty('rate', 150)

engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')


engine.setProperty('voice', voices[1].id)
#engine.say(quotes[0])
#engine.say(authors[0])
engine.runAndWait()
engine.stop()
