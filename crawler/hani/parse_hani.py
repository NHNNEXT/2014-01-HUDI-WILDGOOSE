#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup

hani_URLs=[];

def get_artile_urls_with_pagenum(page):
	URLs = [];
	PRE_URL = "http://www.hani.co.kr/arti/?type=0&cline="
	i = 1

	URL = PRE_URL + str(page*10)

	#read URL and use beautifulsoup
	html_doc = urllib.urlopen(URL).read()
	soup = BeautifulSoup(html_doc)

	news_list = soup.find("div", "sorting-result-section").ul

	for news in news_list : #news_list is 'ul'
		if(i % 2 == 0):
			URL = "http://www.hani.co.kr"+news.dl.dt.a['href'] #URL
			if(URL.find("english_edition")== -1):
				try :
					URLs.append(URL)
				except :
					print "----URL parsing error: " + URL

		i = i + 1;

	return URLs

for i in range(1, 10) :
	hani_URLs = hani_URLs + get_artile_urls_with_pagenum(i)