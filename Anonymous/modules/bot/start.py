import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 
from Anonymous import app
from config import OWNER_ID
from pyrogram import filters


START_TEXT = (
    "**Hey !\n\n> You are now the master of this bot, May you enjoy my superiority ⚡ \n\nThank You !**"
)
START_PIC = 'https://graph.org/file/f7da95a365c0f89c85fb7.jpg'

@app.on_message(filters.command("start") & filters.private)
async def start(app, message):
    buttons = [
           [
                InlineKeyboardButton("Channel", url="t.me/BotsDom"),
            ],
            [
                InlineKeyboardButton("Chats", url="t.me/OurTopics"),
            ],
            ]
    await app.send_photo(message.chat.id, START_PIC, caption=START_TEXT, reply_markup=InlineKeyboardMarkup(buttons))
