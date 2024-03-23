import random
import importlib
import time
import asyncio
from pyrogram.types import Message
import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from Anonymous import Ano
from Anonymous.modules.help import add_command_help

START_BUTTONS = [
    [
        InlineKeyboardButton('⚡ ꜱᴜᴘᴘᴏʀᴛ ⚡', url='https://t.me/BotsDom')
    ]
]

CMD_HELP = {}

@Ano.on_message(filters.command(["start"], ".") & (filters.me))
async def start(client, message):
   X = await message.reply_text("**Starting...**", reply_markup=InlineKeyboardMarkup(START_BUTTONS))
   time.sleep(1.0)
   await Ano.edit_message_text(chat_id=message.chat.id, message_id=X.id, text="**Got it :\n\nJust a moment**", reply_markup=InlineKeyboardMarkup(START_BUTTONS))
   time.sleep(1.0)
   await Ano.edit_message_text(chat_id=message.chat.id, message_id=X.id, text="**TADDAAA :**\n\nIt's Your Own UserBot\n**#AnonymousUserBot**", reply_markup=InlineKeyboardMarkup(START_BUTTONS))

add_command_help(
    "start",
    [
        [".start", "Check if bot is alive"]
    ],
)
