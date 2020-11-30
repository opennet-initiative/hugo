#!/bin/sh
USER=root
HOST=ruri.on             
DIR=/var/www/downloads.opennet-initiative.de/www-testing/

hugo && rsync -avz --delete public/ ${USER}@${HOST}:${DIR}

exit 0
