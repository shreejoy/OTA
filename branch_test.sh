#!/usr/bin/env bash
#Usage bash branch_test.sh GITHUB_USERNAME GITHUB_PASSWORD
export USER_NAME="$1"
export USER_PASSWD="$2"
export bottoken="$3"
rm -rf pass.txt fail.txt ignored.txt devices.json
wget -q https://raw.githubusercontent.com/PixelExperience/official_devices/master/devices.json
count=$(jq length devices.json)
echo "Total $count devices are officially supported"
for ((i=0;i<=$count;i++));
do
#echo "$i"
   jq -r --arg i "$i" '.['$i']' devices.json > device.json
   brand=$(jq -r '.brand' device.json)
#echo "$brand"
   codename=$(jq -r '.codename' device.json)
#echo "$codename"  
 checking="device_${brand}_${codename}" 
echo "https://github.com/PixelExperience-Devices/$checking" >> repo.txt 
 #echo "$checking"
  repo_url="https://${USER_NAME}:${USER_PASSWD}@github.com/PixelExperience-Devices/$checking"
   git ls-remote -q "$repo_url" > remote.txt
   cat remote.txt | tail -n +2 | sed -r 's/.{52}//' > remote.bak
   mv remote.bak remote.txt
   for q in $(jq -r '.supported_versions[].version_code' device.json);
   do
      if [[ "$q" = "pie" ]];
          then
             if grep -x "$q" remote.txt;
                 then
                    echo "$codename has pie banch" >> pass.txt
         else
                    echo "$codename don't have pie banch" >> fail.txt
         fi
          elif [[ "$q" = "pie_caf" ]]; 
          then
             q="caf"
         if grep $q remote.txt;
                 then 
                    echo "$codename has pie-caf banch" >> pass.txt
          else
                    echo "$codename dont have pie-caf banch" >> fail.txt
		 fi		
          else 
             echo "$codename has ignoreable branch" >> ignored.txt
          fi
        done;
	   rm -rf remote.txt
   mv device.json $codename.json 
  mv $codename.json test
done;
FILE_NAME="pass.txt"
curl -F chat_id="-1001234543125" -F document=@"$FILE_NAME" https://api.telegram.org/bot$bottoken/sendDocument
FILE_NAME="fail.txt"
curl -F chat_id="-1001234543125" -F document=@"$FILE_NAME" https://api.telegram.org/bot$bottoken/sendDocument
