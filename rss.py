#!/usr/bin/env python
# Author: Ryan Brown
# Description: checks github and notifies if there are new commits
import pynotify
import feedparser
import re
import datetime
if not pynotify.init("Version Control Notifier"):
	exit()

def pull_feeds():
	#Returns a list of raw version control feeds
	#Bitbucket feed (0)
	feed =feedparser.parse("https://bitbucket.org/rbrown/atom/feed?token=0ab0af15b07352b1596a30bed1293615")
	#Github feeds (1)
	feed2 =feedparser.parse("https://github.com/ryansb.private.actor.atom?token=cae0b3520b731518fcc0f2fc683cae31")
	return [feed, feed2]
#def github_find_author(raw):
#def bitbucket_find_author(raw):
n = pynotify.Notification(pull_feeds()[0]['entries'][0]['title'], "Message")
n.show()

n = pynotify.Notification(pull_feeds()[1]['entries'][0]['title'], "Message")
n.show()
#n = pynotify.Notification("Title", "Message")
#n.show()