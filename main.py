import random
import importlib
import time
import asyncio
from pyrogram.types import Message
import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery

AnoxDx = Client(
  name="PyrogramBot",
  api_id=config.API_ID,
  api_hash=config.API_HASH,
  string_session=config.STRING_SESSION
)
START_BUTTONS = [
    [
        InlineKeyboardButton('⚡ ꜱᴜᴘᴘᴏʀᴛ ⚡', url='https://t.me/BotsDom')
    ]
]

@AnoxDx.on_message(filters.command(["start"], ".") & (filters.me))
  async def start(client, message):
     X = await message.reply_text("**Starting...**")
     time.sleep(1.0)
     await AnoxDx.edit_message_text(chat_id=message.chat.id, message_id=X.id, text="**TADDAAA :**\n\nIt's Your Own UserBot\n**#AnonymousUserBot**", reply_markup=InlineKeyboardMarkup(START_BUTTONS))

AnoxDx.run()
