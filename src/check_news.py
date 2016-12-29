#!/bin/python

from upsilon.serviceHelpers import *

import time
import feedparser
import sys

url = "http://feeds.bbci.co.uk/news/rss.xml"
url = sys.argv[1]
feed = feedparser.parse(url);

metadata = clsmetadata();
metadata['news'] = []

for news in feed['entries']:
	if "updated_parsed" in news:
		date = news['updated_parsed']
	else:
		date = news['published_parsed']

	story = {
		"title": news['title'],
		"url": news['id'],
		"time": time.strftime("%Y-%m-%d %H:%S", date),
		"source": sys.argv[2]
	}

	metadata['news'].append(story);

exit(OK, metadata, "News checked.")
