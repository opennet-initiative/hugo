#!/bin/bash

HTDOCS=/var/www/www.opennet-initiative.de/

#generate RSS abstract. Exit this script on failure
./on-rss2md.py > content/posts/oni-rss-post.md || exit $?

#generate next event list
./on-ics2md.py > content/posts/oni-ics-events.md || exit $?

hugo --quiet || exit $?

rsync -avzq --delete public/ ${HTDOCS} || exit $?
