import random
import importlib
import time
import asyncio
import os
from platform import python_version
from pyrogram import __version__ as versipyro
from pyrogram.types import Message
import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from Anonymous.modules.help.basic import edit_or_reply
from Anonymous.helper.Pyt import ReplyCheck
from Anonymous.modules.help import add_help_cmd
from Anonymous.modules.help.get import get_readable_time
from Anonymous import CMD_HELP

alive_logo = "https://telegra.ph//file/02469a3da0b5840bd9fe5.mp4"
StartTime = time.time()
modules = CMD_HELP
BOT_VER = "3.0@main"

@Client.on_message(filters.command(["alive", "awake"], ".") & filters.me)
async def alive(client: Client, message: Message):
    xx = await edit_or_reply(message, "⚡️")
    await asyncio.sleep(2)
    send = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    uptime = await get_readable_time((time.time() - StartTime))
    man = (
        f"**[AmaX-UserBot](https://t.me/TheAmaX) is Up Alive.**\n\n"
        f"⚡️ <b>Master :</b> {client.me.mention} \n"
        f"⚡️ <b>Modules :</b> <code>{len(modules)} Modules</code> \n"
        f"⚡️ <b>Bot Version :</b> <code>{BOT_VER}</code> \n"
        f"⚡️ <b>Python Version :</b> <code>{python_version()}</code> \n"
        f"⚡️ <b>Pyrogram Version :</b> <code>{versipyro}</code> \n"
        f"⚡️ <b>Bot Uptime :</b> <code>{uptime}</code> \n\n"
        f"    **📌 [𝗦𝘂𝗽𝗽𝗼𝗿𝘁](https://t.me/AmaXChats)** | **📌 [𝗖𝗵𝗮𝗻𝗻𝗲𝗹](https://t.me/TheAmaX)** | **📌 [𝗢𝘄𝗻𝗲𝗿](tg://user?id={client.me.id})**"
    )
    try:
        await asyncio.gather(
            xx.delete(),
            send(
                message.chat.id,
                alive_logo,
                caption=man,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except BaseException:
        await xx.edit(man, disable_web_page_preview=True)


add_help_cmd(
    "alive",
    [
        [".alive", "Check if bot is alive"]
    ],
)
