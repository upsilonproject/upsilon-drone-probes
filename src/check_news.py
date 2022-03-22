#!/usr/bin/python

from upsilon.service import ServiceController

import time
import feedparser
import sys

url = "http://feeds.bbci.co.uk/news/rss.xml"
feed = feedparser.parse(url);

srv = ServiceController();
srv['news'] = []

for news in feed['entries']:
	if "updated_parsed" in news:
		date = news['updated_parsed']
	else:
		date = news['published_parsed']

	story = {
		"title": news['title'],
		"url": news['id'],
		"time": time.strftime("%Y-%m-%d %H:%S", date),
		"source": url
	}

	srv['news'].append(story);

srv.exitOk("News checked.")
