#! /bin/sh
      
      export ID=$TRAVIS_COMMIT
	  git diff-tree --no-commit-id --name-only -r $TRAVIS_COMMIT > commit.txt
    echo "$(<commit .txt )"
      cat commit.txt | cut -d "/" -f1
      
for i in $(jq -r ".[] | .codename" devices.json)
  do
      if grep $i commit.txt; then
      echo -e " ";
      echo -e "There is a new update for $i ";
      echo -e " ";
      echo -e "Getting build information from remote source !!";
      export cname=$i
      echo -e " ";
else
      echo -e "No new update for $i"
      fi
done	
