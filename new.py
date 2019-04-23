import requests
import html
import json
import difflib
import subprocess
import time
from datetime import datetime, date
from glob import glob
from hashlib import md5
from os import remove, system, environ, path, getcwd, chdir, rename, stat
from requests import get, post

# telegram variables
bottoken = environ['bottoken']
cname = "rosy"
telegram_chat = "@test_channel_68"

c_name = json.loads(get(
    "https://raw.githubusercontent.com/PixysOS-Devices/official_devices/master/{cname}/build.json").content)
devices = json.loads(get(
    "https://github.com/PixysOS-Devices/official_devices/blob/master/devices.json").content)
    
for v in devices:
    if ["codename"] == cname:
        device = v['name']
        maintainer_url = v['maintainer_url']
        maintainer_name = v['maintainer_name']
        xda_thread = v['xda_thread']
    else:
        print("No information about this device found")

for link in cname['response']:
    id= link['response']['id']
    build_date= link['response']['build_date']
    version= link['response']['version']
    filename= link['response']['filename']
    url= link['response']['url']
 
    print(build_date, version, filename, url, version)
    print(device, maintainer_url, maintainer_name, xda_thread)
    
    telegram_message = "тЪбя╕П *New PixysOS Update* тЪбя╕П\n\n ЁЯУ▒ New build available for *{}* `({})`\n" \
                     "   тЦля╕П *Build Version:* {} \n    тЧ╛я╕П *Build Date:* {}\n    тЦля╕П *MD5:*```{}```\n\n" \
                     "*Download:* [{}]({}) \n\n" \
           .format(device, cname, version, build_date, id, filename, url) 
                    
    params = (
        ('chat_id', telegram_chat),
        ('text', telegram_message),
        ('parse_mode', "Markdown"),
        ('disable_web_page_preview', "yes")
    )
    telegram_url = "https://api.telegram.org/bot" + bottoken + "/sendMessage"
    telegram_req = post(telegram_url, params=params)
    telegram_status = telegram_req.status_code
    if telegram_status == 200:
        print("{0}: Telegram Message sent".format(device))
    else:
        print("Telegram Error") 
