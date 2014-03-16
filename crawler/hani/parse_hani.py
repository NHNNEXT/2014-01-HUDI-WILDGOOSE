#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup

hani_URLs=[];

def find_last_pagenum():
	URL = "http://www.hani.co.kr/arti/?type=0&cline="
	html_doc = urllib.urlopen(URL).read()
	soup = BeautifulSoup(html_doc)
	return soup.find("a", "last")['href'].split("=")[2]

def get_artile_urls_with_pagenum(page):
	URLs = [];
	PRE_URL = "http://www.hani.co.kr/arti/?type=0&cline="
	i = 1

	URL = PRE_URL + str(page*10-1)

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

def extract_section(html_doc):
	soup = BeautifulSoup(html_doc)
	section = soup.find("div","article-category-title").table.tr.h3.img['alt'].encode("utf-8")
	return section

def extract_title(html_doc):
	soup = BeautifulSoup(html_doc)
	title = soup.find("div", "article-category-title").table.tr.td.next_sibling.next_sibling.h3.findAll(text=True)[0].encode("utf-8")
	return title

def extract_datetime(html_doc):
	soup = BeautifulSoup(html_doc)
	datetime = soup.find("p", "date").span.get_text().encode("utf-8").split(': ')[1].replace('.','-')
	return datetime

def trim_contents(html_doc):
	soup = BeautifulSoup(html_doc)

	# 사진이 있는경우 그 사진의 주석을 지운다.
	photo = soup.find("table", "photo-view-area")
	if(photo):
		photo.clear()

	contents = soup.find("div", "article-contents").findAll(text=True)
	content = " ".join(contents).encode("utf-8").strip().replace("\t", "")
	return content

def extract_contents(html_doc):
	content = trim_contents(html_doc).replace("\n", "").split('@hani')[0]
	return content[:content.rfind(".")+1]


def extract_author(html_doc):
	content = trim_contents(html_doc)
	find_author=[u" 기자 ", u" 선임기자",u" 특파원", u"편집장", u" 인턴기자", u"뉴스팀", u"뉴시스", u"연합뉴"]
	keyword = {"author_keyword" : find_author}

	# print len(find_author)
	# print find_author[3].encode('utf-8')
	escape = False
	for line in reversed(content.splitlines()):
		for keyword in find_author:
			if(line.rfind(keyword.encode('utf-8')) != -1):
				# print "author키워드: " + keyword.encode('utf-8')
				author = line
				escape = True
				break
			if(escape):
				break
	if(author.find('연합뉴') != -1):
		author = author[author.rfind('.')+1 :].strip()
	return author
		
def parse_article_with_url(url):
	parsed_article = dict()
	html_doc = urllib.urlopen(url).read() # 간단한 get요청
	parsed_article['URL'] = url
	parsed_article['section'] = extract_section(html_doc) # section 추출 차후에 특정 섹션(만화 등)은 파싱하지 않도록 조치 필요
	parsed_article['title'] = extract_title(html_doc)
	parsed_article['datetime'] = extract_datetime(html_doc) +':00' #초단위가 표시되지 않아 00초를 붙여줘서 형식 통일
	parsed_article['contents'] = extract_contents(html_doc)
	parsed_article['author'] = extract_author(html_doc)
	# parsed_article['provide'] = '한겨레'
	print parsed_article['author']


# 전체 기사의 URL을 모두 긁어온다
# for i in range(1, int(find_last_pagenum())) :
# 	hani_URLs = hani_URLs + get_artile_urls_with_pagenum(i)



# parse_article_with_url test
# parse_article_with_url('http://www.hani.co.kr/arti/society/society_general/628271.html')