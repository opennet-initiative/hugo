#!/bin/bash

HTDOCS=/var/www/www.opennet-initiative.de/

#generate RSS abstract. Exit this script on failure
./on-rss2md.py > content/posts/oni-rss-post.md || exit $?

hugo && rsync -avz --delete public/ ${HTDOCS}
