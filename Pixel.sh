#!/usr/bin/env bash

function exports() {
  export CUSTOM_BUILD_TYPE=OFFICIAL
  export DEVICE_MAINTAINERS="Shreejoy Dash" # The maintainer of that device
  export KBUILD_BUILD_USER=${DEVICE_MAINTAINERS}
  export BUILD_NAME="Pixel Experience"
  }
  

  function use_ccache() {
    # CCACHE UMMM!!! Cooks my builds fast
   if [ "$use_ccache" = "true" ];
   then
      printf "CCACHE is enabled for this build"
      export USE_CCACHE=1
      export CCACHE_DIR=/home/shreejoy/ccache/pixys
      prebuilts/misc/linux-x86/ccache/ccache -M 50G
    elif [ "$use_ccache" = "false" ];
    then
       export CCACHE_DIR=/home/shreejoy/ccache/pixys
       ccache -C
       export USE_CCACHE=1
       prebuilts/misc/linux-x86/ccache/ccache -M 50G
       wait
       printf "CCACHE Cleared"
    fi
}

function clean_up() {
  # Its Clean Time
   if [ "$make_clean" = "true" ]
   then
      make clean && make clobber
   elif [ "$make_clean" = "false" ]
   then
      rm -rf out/target/product/*
      wait
      echo -e "OUT dir from your repo deleted";
   fi
   # Clean old device dependencies
   if [ "$clean_device" = "true" ];
   then
      if [ -e /home/pixys/source/clone_path.txt ];
      then
         clone_path=$(cat /home/shreejoy/clone_path.txt)
         if [ -z ${clone_path} ];
         then
            echo "clone_path.txt is empty so nothing to wipe"
         else
            for WORD in `cat /home/shreejoy/clone_path.txt`
            do
              printf "${Blue}Deleting obsolete path /home/pixys/source/${WORD}\n${Color_Off}"
              rm -rf $WORD
            done
            rm -rf /home/shreejoy/clone_path.txt
            touch /home/shreejoy/clone_path.txt
         fi
    else
        echo "clone_path.txt doesnt exist"
        touch /home/shreejoy/clone_path.txt
    fi
    build_init
   fi
}

function build_init() {
    rm -rf /home/pixys/source/json/"${DEVICE}".json
    rm -rf /home/pixys/source/devices_dep.json
    DEPS=$(curl -s https://raw.githubusercontent.com/PixysOS/PixysOS_jenkins/master/devices_dep.json | jq --arg DEVICE "$DEVICE" '. | .[$DEVICE]')
    #jq --arg DEVICE "$DEVICE" '. | .[$DEVICE]' /home/pixys/source/devices_dep.json > /home/pixys/source/json/"${DEVICE}".json
    #export dep_count=$(jq length /home/pixys/source/json/${DEVICE}.json)
    export dep_count=$(jq length <<< ${DEPS})
    printf "\n${UYellow}Cloning device specific dependencies \n\n${Color_Off}"
    for ((i=0;i<${dep_count};i++));
    do
       repo_url=$(jq -r --argjson i "$i" '.[$i].url' <<< ${DEPS})
       branch=$(jq -r --argjson i "$i" '.[$i].branch' <<< ${DEPS})
       target=$(jq -r --argjson i "$i" '.[$i].target_path' /<<< ${DEPS})
       printf "\n>>> ${Blue}Cloning to $target...\n${Color_Off}\n"
       git clone --recurse-submodules --depth=1 --quiet $repo_url -b $branch $target
       printf "${Color_Off}"
       if [ -e /home/pixys/source/$target ]
          then
             printf "\n${Green}Repo clone success...\n${Color_Off}"
             echo "$target" >> /home/pixys/source/clone_path.txt
           else
             sendTG "Could not clone some dependecies for [$DEVICE]($BUILD_URL)"
	         TGlogs "Could not clone some dependecies for [$DEVICE]($BUILD_URL)"
             printf "\n\n${Red}Repo clone fail...\n\n${Color_Off}"
             printf "${Cyan}Exiting${Color_Off}"
             sleep 5
             exit 1
            fi
    done
}
