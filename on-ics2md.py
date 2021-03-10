#!/usr/bin/env python3
#
# Zeige kommende Opennet Veranstaltungen an (in Markdown Format)
#
import requests
from ics import Calendar #pip3 install ics

oni_ics_url='https://stadtgestalten.org/opennet/events/public.ics'
r = requests.get(oni_ics_url)
r.raise_for_status()

c = Calendar(r.text)
for e in c.timeline:
	print("* {} am  {}, siehe <a href=\"{}\">{}</a>".format(e.name, e.begin.format('DD.MM.YYYY HH:mm'), e.url, e.url))
