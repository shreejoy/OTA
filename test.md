PixysOS Updater Backend
=======================

Copyright (c) 2017 The LineageOS Project
Copyright (c) 2018-2019 PixysOS

Adding a new device and its dependencies
---
1. Add your device to devices.json, sorted alphanumerically by codename. Fields are documented below.
2. Add your device releted dependencies to devices_deps.json, sorted alphanumerically by codenames. Fields are documted below.

### devices.json

* `name`: The codename of the device - example `beryllium`
* `brand`: The full name - example `Pocophone F1`
* `codename`: The full name - example `Pocophone F1`
* `maintainer_name`: The full name - example `Pocophone F1`
* `maintainer_xda`: The full name - example `Pocophone F1`
* `maintainer_telegram_id`: Your name
* `xda_thread_link`: URL to XDA thread of your device
