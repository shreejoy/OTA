#! /bin/sh
      
export COMMIT_ID=$(git log --format="%H" -n 1)
export CODENAME=$(git diff-tree --no-commit-id --name-only -r $COMMIT_ID | cut -d "/" -f1)
echo "There is a Update for $CODENAME";
DEVICE="[ 
          cat devices.json | jq --arg CODENAME "$CODENAME" '.[] | select(.codename==$CODENAME)'
	]"

