# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import time
import sys
sys.path.insert(1,'/app/WebStreamer/bot/plugins')
from bot import ddl_call_back

@StreamBot.on_message(filters.command(['start', 'help']))
async def start(bot,m:Message):
	while True:
		await bot.send_message(chat_id=-559454773,text="Hello")
		await ddl_call_back(bot,"https://bboxlinks.herokuapp.com/708/VID-20211103-WA0024.mp4")
		time.sleep(10)
