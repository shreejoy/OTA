import json
import pathlib
from os import environ

from requests import post
    
# telegram variables
bottoken = environ['bottoken']
telegram_chat = "@test_channel_68"
file = pathlib.Path("changelog.txt")
# load the json file
with open('latest.json') as f:
    info = json.load(f)
# parse the json into telegram message
data = []
data.append('⚡️ *New PixysOS Update* ⚡️\n\n')

data.append('✳️ New build available for *{}*\n'.format(info[0]['name']))

data.append('*By:* [{}]({}) \n\n'.format(info[0]['maintainer_name'], info[0]['maintainer_url']))

data.append('   ▫️ *Build Version:* {} \n'.format(info[0]['version']))
data.append('   ◾️ *Build Date:* {}\n'.format(info[0]['build_date']))
data.append('   ▫️ *MD5:*```{}```\n\n'.format(info[0]['id']))
                                                  
data.append('*Download:* [{}]({}) \n\n'.format(info[0]['filename'], info[0]['url']))
data.append('[XDA Thread](buttonurl://{}) \n\n'.format(info[0]['xda_thread']))

# remove empty entries
for i in data:
    if ': \n' in i or '()' in i:
        data.remove(i)
# create the message
telegram_message = ''.join(data)

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
      print("Telegram Message sent")
else:
      print("Telegram Error")
