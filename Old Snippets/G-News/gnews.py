# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 03:42:23 2018

@author: Avis_King
"""

import bs4
import lxml 
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def news(xml_news_url):
	Client=urlopen(xml_news_url)
	xml_page=Client.read()
	Client.close()
	
	soup_page=soup(xml_page,"xml")
	news_list=soup_page.findAll("item")
	
	for news in news_list:
		print(news.title.text)
		print(news.link.text)
		print(news.pubDate.text)	
		print("\n\n\n\n")
		


news_url="https://news.google.com/news/rss/?ned=us&gl=US&hl=en"
sports_url="https://news.google.com/news/rss/headlines/section/topic/SPORTS.en_in/Sports?ned=in&hl=en-IN&gl=IN"


news(news_url)	
news(sports_url)