#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup
import re

def parseArticle(URL):

	#read URL and use beautifulsoup
	html_doc = urllib.urlopen(URL).read()
	soup = BeautifulSoup(html_doc)
	
	title = soup.find("div", "article-category-title").table.tr.td.next_sibling.next_sibling.h3.findAll(text=True)[0].encode("utf-8")
	section = soup.find("div", "article-category-title").table.tr.h3.img['alt'].encode("utf-8")
	dateTime = soup.find("p", "date").span.get_text().encode("utf-8").split(': ')[1].replace('.','-')
	
	if(section != '만화'):
		contents = soup.find("div", "article-contents").findAll(text=True)
		content = " ".join(contents).encode("utf-8").strip()
		if(soup.find("div", "article-alignC") != None):
			content = content[content.find('\n'):]


		rep_pos = content.rfind(" 기자 ") #기자가 없으면 -1 return
		if(rep_pos != -1):
			email = content.rfind(".kr")
			author = content[content.split('@hani')[0].rfind(".")+1:email+3].split(" 기자")[0] + content[rep_pos-9:email+3].split(" 기자")[1]
		else:
			rep_pos = content.rfind(" 선임기자 ")
			if(rep_pos != -1):
				email = content.rfind(".kr")
				author = content[rep_pos-12:rep_pos+1] + content[rep_pos+14:email+3]		
			else:
				rep_pos = content.rfind("뉴스팀") 
				if(rep_pos != -1): #온라인 뉴스팀인 경우
					author = content[rep_pos-12:rep_pos+9] #한글은 3개
				else:
					rep_pos = content.rfind("뉴시스") 
					if(rep_pos != -1):#뉴시스인 경우
						author = "뉴시스"
					else:
						rep_pos = content.rfind("연합뉴")
						if(rep_pos != -1):#연합뉴스인 경우
							author = "연합뉴스"
						else:
							author = " "

		content = content[content.find('\n'):content.split('@hani')[0].rfind(".")].strip()
		if(content.rfind("【") != -1):
			content = content[:content.rfind("【")].strip()

		print URL
		# print title
		# print section
		# print content
		# print dateTime
		print author.strip()

def parsePage(page):
	PRE_URL = "http://www.hani.co.kr/arti/?type=0&cline="
	i = 1

	#make file
	if (page == 1) :
		f = open('parsedHani', 'w')
	else :
		f = open('parsedHani', 'a')
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
					parseArticle(URL)
				except :
					print "----error: " + URL

		i = i + 1;
	f.close()

for i in range(1, 50) :
	parsePage(i)