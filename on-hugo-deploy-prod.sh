#!/bin/bash

HTDOCS=/var/www/www.opennet-initiative.de/

#get RSS abstract and exit this script on failure
md_text=$(./on-rss2md.py) || exit $?

echo ${md_text} > content/posts/oni-rss-post.md

hugo && rsync -avz --delete public/ ${HTDOCS}
