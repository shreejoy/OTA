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
      export CCACHE_DIR=/home/shreejoy/ccache/pixel
      prebuilts/misc/linux-x86/ccache/ccache -M 50G
    elif [ "$use_ccache" = "false" ];
    then
       export CCACHE_DIR=/home/shreejoy/ccache/pixel
       ccache -C
       export USE_CCACHE=1
       prebuilts/misc/linux-x86/ccache/ccache -M 50G
       wait
       printf "CCACHE Cleared"
    fi
}



function build_init() {
   source build/envsetup.sh
   lunch aosp_rosy-userdebug
   mka bacon -j24
}

function status() {
   if [ -f out/target/product/rosy/Pixel*.zip ]
   then 
     
   fi
