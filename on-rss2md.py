#!/usr/bin/env python3
#
# Script for creating an abstract of ONI RSS file in Markdown
#
import requests
import xml.etree.ElementTree as ET
import sys
from bs4 import BeautifulSoup

# download RSS
oni_rss_feed_url='https://stadtgestalten.org/stadt/groups/16/feed/'
r = requests.get(oni_rss_feed_url)
r.raise_for_status()
tree = ET.fromstring(r.text)

#make sure we have the Opennet RSS feed here
rss_title = tree.find('./channel/title').text
if rss_title.find('Opennet') == -1:
    print('Error: Downloaded feed from "' + oni_rss_feed_url + '" does not' \
      ' have "Opennet" in title.')
    sys.exit()

out_md = "" #for Markdown output
for item in tree.findall('./channel/item'):
    title = item.find('title').text
    link = item.find('link').text
    descr = item.find('description')

    abstract = ""
    html = BeautifulSoup(descr.text, features="lxml")
    for h in html.findAll('h3'):
        abstract += h.text + ", "

    if len(abstract) > 0:
        abstract = "Themen: " + abstract[:-2] # cut ", " at end
    else:
        #no headers found. Use text in <description> instead
        abstract = html.get_text()[0:150]
        #make sure last word is complete and not cut
        abstract = abstract[0:abstract.rfind(' ')]
        abstract += " ..."

    out_md += ' * <a href="' + link + '">' + title + '</a> ' + abstract + '\n'

print(out_md)
