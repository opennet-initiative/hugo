#!/bin/sh
USER=root
HOST=ruri.on             
DIR=/var/www/downloads.opennet-initiative.de/www-testing/

#change baseurl as long as we publish under downloads.on-i.de/www-testing
perl -pi -e 's/baseurl = .*/baseurl = "\/www-testing\/" /g' config.toml
#generate and copy files
hugo && rsync -avz --delete public/ ${USER}@${HOST}:${DIR}
#revert baseurl
perl -pi -e 's/baseurl = .*/baseurl = "\/" /g' config.toml

exit 0
