#!/usr/bin/env python3
#
# Script for creating an abstract of ONI RSS file in Markdown
#
import requests
import xml.etree.ElementTree as ET
import sys
from bs4 import BeautifulSoup
import re

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
count = 0
for item in tree.findall('./channel/item'):
    if count >= 5:
        break   #only show first 5 items
    else:
        count += 1

    title = item.find('title').text
    link = item.find('link').text
    descr = item.find('description')

    abstract = ""
    html = BeautifulSoup(descr.text, features="lxml")
    #add colon character because after html2text conversion we need to 
    # make clear what is headline and what is normal text.
    for h in html.findAll(re.compile("h[1-5]")): #matches h1, h2, h3, ...
        h.string = h.string + ": "

    abstract = html.get_text()[0:300]
    #make sure last word is complete and not cut
    abstract = abstract[0:abstract.rfind(' ')]
    abstract += " ..."
    abstract = abstract.replace("\n", " ")
    abstract = abstract.replace("\t", " ")

    out_md += ' * <p style="text-align: justify"><a href="' + link + '">' + title + '</a> ' + abstract + '</p>\n'

print(out_md)
