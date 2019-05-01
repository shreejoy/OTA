#! /bin/sh
      
# export ID=fc72922bcf7d03a2c21c2da18a6db99ddbf1279f
export COMMIT_ID=$(git log --format="%H" -n 1)
export CODENAME=$(git diff-tree --no-commit-id --name-only -r $COMMIT_ID | cut -d "/" -f1)
# export CODENAME=santoni
echo "There is a Update for $CODENAME";
DEVICE="[$(cat devices.json | jq -c --arg CODENAME "$CODENAME" '.[] | select(.codename==$CODENAME)')]"
git clone  git@gitlab.com:pshreejoy15/rom_ota.git
rm -rf rom_ota/pixys.json
echo "$DEVICE" >> rom_ota/pixys.json
cd rom_ota
wget https://gitlab.com/pshreejoy15/ota/raw/master/jsonFormatter.py 
python3 jsonFormatter.py
git add . 
git commit -m "$(date) $CODENAME update"
cd ..
python3 new.py



