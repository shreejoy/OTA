import json, requests
from telegram import Bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater

bottoken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
BOT = Bot(token=bottoken)
UPDATER = Updater(bot=BOT, use_context=True)
TG_ADMIN = "xxxxxxxxxxxxxxxxxxxxxx"

bl = []

def check_names(url):
  geturl = requests.get(url)
  getjson = json.loads(geturl.text)
  
  for jsn in getjson:
    if len(jsn["name"]) > 15:
      bl.append(jsn["name"])
      
check_names('https://raw.githubusercontent.com/PixelExperience/official_devices/master/team/maintainers.json')
check_names('https://raw.githubusercontent.com/PixelExperience/official_devices/master/team/core.json')

message = "The following users have names bigger than 15 characters \n\n"

for b in bl:
  message = message + b + '\n'
  
UPDATER.bot.send_message(chat_id=TG_ADMIN, text=message, parse_mode='HTML', disable_web_page_preview='yes')
