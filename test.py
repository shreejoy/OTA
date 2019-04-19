import json
from os import environ

from requests import post
    
# telegram variables
bottoken = environ['bottoken']
telegram_chat = "@test_channel_68"
# load the json file
with open('latest.json') as f:
    info = json.load(f)
# parse the json into telegram message
data = []
data.append('⚡️PixysOS Update⚡\n\n')
data.append('➡ *New build available for* {} (```{}```)\n'.format(info[0]['name'], info[0]['codename']))
data.append('👤 *By:* {} \n\n'.format(info[0]['maintainer_name']))

data.append('📆 *Build Date:* {}\n'.format(info[0]['build_date']))
data.append('ℹ *Build Version:* {} \n'.format(info[0]['version']))
data.append('ℹ *Build Type:* {} \n\n'.format(info[0]['build_type']))

data.append('⬇️ [Download Now]({}) \n'.format(info[0]['url']))
data.append('⬇️ [XDA Thread Link]({}) \n\n'.format(info[0]['xda_thread']))
 
data.append('#````{}```'.format(info[0]['rom_tag']))
data.append('#```{}```\n'.format(info[0]['codename']))
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
