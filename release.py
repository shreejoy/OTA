import json
import os
from pathlib import Path
import shutil
from telegram import Bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater

BOT_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
BOT = Bot(token=BOT_TOKEN)
UPDATER = Updater(bot=BOT, use_context=True)
TG_CHAT = "@PixysOS"

def send_message(message):
  shutil.copy2('/src/dir/file.ext', '/dst/dir/newname.ext')

def main():
  FILENAME = os.environ("FILENAME")
  DEVICE = os.environ("DEVICE")
  
  if 'GAPPS' in FILENAME:
    FOLDER = 'ten_gapps'
  else:
    FOLDER = 'ten'
    
  if FILENAME and DEVICE:
    build_path = "/home/ftp/uploads/.test/" + DEVICE + "/" + FOLDER + "/" + FILENAME
  else:
    MESSAGE = "Error FILENAME or DEVICE not defined"
    send_message_maintainers()
  
  rom_file = Path(build_path)
  if rom_file.exists():
    
