import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 
from Anonymous import app, SUDO_USER
from pyrogram import filters, Client


START_TEXT = (
    f"**Hey Master!\n\n⚡ This is AmaX ! Your Assistant UB ! We are Glad to Assist You ⚡ \n\n<u>Thank You !</u>**"
)
START_PIC = 'https://graph.org/file/e6a9b462dd5d020d2af57.jpg'
PAGE_TEXT = """[AmaX UserBot](https://t.me/TheAmaX) is an **OPEN SOURCE** Project: \n𝗍𝗁𝖺𝗍 𝗆𝖾𝖺𝗇𝗌 𝖺𝗇𝗒 𝗈𝗇𝖾 𝖼𝖺𝗇 𝗋𝖾𝖺𝖽 𝖺𝗇𝖽 𝗎𝗌𝖾 𝗂𝗍 𝖿𝗋𝖾𝖾𝗅𝗒 𝖺𝗇𝖽 𝖼𝖺𝗇 𝖿𝗂𝗇𝖽 𝖻𝗎𝗀𝗌 𝖺𝗇𝖽 𝗀𝖾𝗍 𝗄𝗇𝗈𝗐 𝗍𝗁𝖾 𝗌𝖾𝖼𝗎𝗋𝗂𝗍𝗒 𝗅𝖾𝗏𝖾𝗅 𝗈𝖿 𝗍𝗁𝖾 **[REPO](https://github.com/AnoxDx/AnonymousUserBot)**"""

@app.on_message(filters.command("start") & (filters.me | filters.user(SUDO_USER)))
async def start(app, message):
    buttons = [
           [
                InlineKeyboardButton("Channel", url="t.me/TheAmaX"),
                InlineKeyboardButton("Chats", url="t.me/AmaXchats")
            ],
           [
                 InlineKeyboardButton('SOURCE', callback_data="HELP")
            ]
            ]
    await app.send_photo(message.chat.id, START_PIC, caption=START_TEXT, reply_markup=InlineKeyboardMarkup(buttons))


@app.on_callback_query()
async def callback_query(Client, CallbackQuery):
 PAGE_BUTTONS = [
        [
            InlineKeyboardButton("Source Repo", url="https://github.com/AnoxDx/AnonymousUserBot"),
            InlineKeyboardButton('⟲ ʙᴀᴄᴋ', callback_data="OKBHAY")
        ]
 ]
 buttons = [
           [
                InlineKeyboardButton("Channel", url="t.me/TheAmaX"),
                InlineKeyboardButton("Chats", url="t.me/AmaXchats")
            ],
           [
                 InlineKeyboardButton('SOURCE', callback_data="HELP")
            ]
            ]
 if CallbackQuery.data == "HELP":
    await CallbackQuery.edit_message_text(
            PAGE_TEXT,
            reply_markup=InlineKeyboardMarkup(PAGE_BUTTONS)
        )
 if CallbackQuery.data == "OKBHAY":
    await CallbackQuery.edit_message_text(
             START_TEXT,
             reply_markup=InlineKeyboardMarkup(buttons)
         )
