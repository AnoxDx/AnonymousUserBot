import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 
from Anonymous import app, SUDO-USER
from pyrogram import filters, Client


START_TEXT = (
    f"**Hey {client.mention}  !\n\n>⚡ This is AmaX ! Your Assistant UB ! We are Glad to Assist You ⚡ \n\n<u>Thank You !</u>**"
)
START_PIC = 'https://graph.org/file/e6a9b462dd5d020d2af57.jpg'

@app.on_message(filters.command("start") & (filters.me | filters.user(SUDO_USER))
async def start(app, message):
    buttons = [
           [
                InlineKeyboardButton("Channel", url="t.me/BotsDom"),
                InlineKeyboardButton("Chats", url="t.me/OurTopics")
            ],
            ]
    await app.send_photo(message.chat.id, START_PIC, caption=START_TEXT, reply_markup=InlineKeyboardMarkup(buttons))
