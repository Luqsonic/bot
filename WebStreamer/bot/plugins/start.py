# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import time

@StreamBot.on_message(filters.command(['start', 'help']))
async def start(bot,m:Message):
	while True:
		await bot.send_message(chat_id=-559454773,text="Hello")
		time.sleep(10)
