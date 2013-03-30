#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib.request
import simplejson
import datetime
import time;

url='http://www.wanikani.com/api/user/<apikey>/study-queue/'
resp = simplejson.load(urllib.request.urlopen(url))

info = resp['requested_information']
review_time = info['next_review_date']
time_now = int(time.time())
if info['lessons_available'] > 0:
	print("L:",info['lessons_available'],end=" - " )
if time_now-review_time < 0:
	print("R:",info['reviews_available'], end=' ')
else:
	print("R:",(time_now-review_time)/60, "mins", end=' ')
