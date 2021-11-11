# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import time
""""
@StreamBot.on_message(filters.command(['start', 'help']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, Send me a file to get an instant stream link.',
                  reply_markup=InlineKeyboardMarkup(
                      [[
                            InlineKeyboardButton(
                                  f'{emoji.STAR} Source {emoji.STAR}',
                                  url='https://github.com/EverythingSuckz/TG-FileStreamBot')
                        ]]
                  ))"""
async def start():
	#hile True:
		await StreamBot.send_message(chat_id=-559454773,text="Hello")
		#me.sleep(10)
