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
data.append('➡ *New build available for* ({}) ({}) \n'.format(info[0]['name'], info[0]['codename']))
data.append('👤 *By:* {} \n\n'.format(info[0]['maintainer_name']))

data.append('📆 *Build Date:* {} \n'.format(info[0]['build_date']))
data.append('ℹ *Build Version:* {} \n'.format(info[0]['version']))
data.append('ℹ *Build Type:* {} \n\n'.format(info[0]['build_type']))

data.append('⬇️ [Download Now: ]({}) \n'.format(info[0]['url']))
data.append('⬇️ [XDA Thread Link: ]({}) \n\n'.format(info[0]['xda_thread']))

data.append('#```{}```#```{}```\n'.format(info[0]['rom_tag'], info[0]['codename']))
    
# remove empty entries
for i in data:
    if ': \n' in i or '()' in i:
        data.remove(i)
# create the message
telegram_message = ''.join(data)

files = (
    ('chat_id', telegram_chat),
    ('text', telegram_message),
    ('parse_mode', "Markdown"),
    ('disable_web_page_preview', "yes")
)
url = "https://api.telegram.org/bot" + bottoken + "/sendMessage"
# post to telegram
telegram_req = post(url, files=files)
status = telegram_req.status_code
response = telegram_req.reason
if status == 200:
    print("Message sent")
else:
    print("Error: " + response)
