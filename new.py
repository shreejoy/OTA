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

#Telegram variables
bottoken = environ['bottoken']
cname = "rosy"
telegram_chat = "@test_channel_68"

c_name = json.loads(get("https://raw.githubusercontent.com/PixysOS-Devices/official_devices/master/" + cname + "/build.json").content)
devices = json.loads(get("https://raw.githubusercontent.com/shreejoy/official_devices-3/master/devices.json").content)

if c_name and devices:
    v = devices[0]
    device = v['name']
    maintainer_url = v['maintainer_url']
    maintainer_name = v['maintainer_name']  
    xda_thread = v['xda_thread']

    codename = c_name['response'][0]
    r_id = codename['id']
    build_date = codename['datetime']
    version = codename['version']
    filename = codename['filename']
    url = codename['url']

    telegram_message = (f"⚡️ *New PixysOS Update* ⚡️\n\n📱 New build available for *{device}*`({cname})`\n\n"\
                        f"By: [{maintainer_name}]({maintainer_url})\n\n"\
                        f"   ▫️*Build Version: {version}*\n   ◾️*Build Date: {build_date}*\n   ▫️*MD5:* ```{r_id}```"\
                        f"*Download:* [{filename}]({url})")
                
    params = (('chat_id', telegram_chat),
              ('text', telegram_message),
              ('parse_mode', "Markdown"),
              ('disable_web_page_preview', "yes"))

    telegram_url = "https://api.telegram.org/bot" + bottoken + "/sendMessage"
    telegram_req = post(telegram_url, params=params)
    telegram_status = telegram_req.status_code
    if telegram_status == 200:
        print(f"{device}: Telegram Message sent")
    else:
        print("Telegram Error")
else:
    print("Couldn't fetch both required items.")
