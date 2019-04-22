import requests
import html
import json
from telegram.ext import Updater, CommandHandler
from requests import get
from telegram import ParseMode
from telegram.error import TelegramError
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html
import difflib
import subprocess
import time
from datetime import datetime, date
from glob import glob
from hashlib import md5
from os import remove, system, environ, path, getcwd, chdir, rename, stat
from github3 import GitHub, exceptions
from hurry.filesize import size, alternative
from pyDownload import Downloader
from requests import get, post

# telegram variables
bottoken = environ['bottoken']
cname = environ['codename']
telegram_chat = "@test_channel_68"

c_name = json.loads(get(
    "https://raw.githubusercontent.com/PixysOS-Devices/official_devices/master/" + cname + "/build.json").content)
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
    
    telegram_message = "⚡️ *New PixysOS Update* ⚡️\n\n 📱 New build available for *{}* `({})`\n" \
                    "   ▫️ *Build Version:* {} \n    ◾️ *Build Date:* {}\n    ▫️ *MD5:*```{}```\n\n" \
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
 


