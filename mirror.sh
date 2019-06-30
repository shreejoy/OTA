#!/usr/bin/env bash
cd /home/rof/src/github.com/shreejoy/test
#wget -O /home/rof/src/github.com/shreejoy/test/devices.json https://raw.githubusercontent.com/shreejoy/test/master/devices.json?token=AJKZ7EFWUY4EWYVZWYFJLNC5EH2KM
LINK=$(jq -r '.url' devices.json)
FILE_NAME=$(jq -r '.fname' devices.json)
wget $LINK
echo "Mirroring $FILE_NAME"
scp $FILE_NAME pshreejoy15@frs.sourceforge.net:/home/frs/p/shreejoy
