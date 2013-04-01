#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib.request
import json
import calendar
import time;

url='http://www.wanikani.com/api/user/<api_key>/study-queue/'
try:
	resp = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
except URLError:
	print("URL ERR",end='')
except Exception:
	print("UNK ERR",end='')

info = resp['requested_information']
review_time = info['next_review_date']
time_now = calendar.timegm(time.gmtime())
if info['lessons_available'] > 0:
	print("L:",info['lessons_available'],end=" - " )
if info['reviews_available'] > 0:
	print("R:",info['reviews_available'], end='')
else:
	print("R:",int((review_time-time_now)/60), "mins", end='')
