from Anonymous import app, API_ID, API_HASH
from config import OWNER_ID
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    "**Hey !\n\n> You are now the master of this bot, May you enjoy my superiority ⚡ \n\nThank You !**"
)
ALIVE_PIC = 'https://graph.org/file/f7da95a365c0f89c85fb7.jpg'

@app.on_message(filters.user(OWNER_ID) & filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("Channel", url="t.me/BotsDom"),
            ],
            [
                InlineKeyboardButton("Chats", url="t.me/OurTopics"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

@app.on_message(filters.user(OWNER_ID) & filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("Booting Your Client")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Zaid/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully As {user.first_name} ✅.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
