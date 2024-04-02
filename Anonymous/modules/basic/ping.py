import random
import asyncio
from datetime import datetime
from pyrogram.types import Message
from Anonymous import app, SUDO_USER
from pyrogram import Client, filters


# animations
data = [
    "🕜",
    "🕡",
    "🕦",
    "🕣",
    "🕥",
    "🕧",
    "🕓",
    "🕔",
    "🕒",
    "🕑",
    "🕐"
]

pings = []


@Client.on_message(filters.command(["ping"], ".") & (filters.me | filters.user(SUDO_USER)))
async def ping(client: Client, message: Message):
        if len(message.command) == 1:
            start = datetime.now()
            await message.edit_text(". . .")
            end = datetime.now()
            m_s = (end - start).microseconds / 1000
            await message.edit_text(
                f"**Pöng !**\n`{m_s} ms`\n⧑ {client.me.mention}",
                disable_web_page_preview=True
            )
        elif len(message.command) == 2:
            cmd = message.command
            count = int(cmd[1]) if cmd[1] and cmd[1].isdigit() else 0
            if count <= 1:
                return await message.edit_text(
                    f"Use `.ping` for pings less than 1."
                )

            else:
                try:
                    for _ in range(count):
                        await infinite()
                        await message.edit_text(". . .")
                        await asyncio.sleep(0.30)
                    await message.edit_text("".join(pings))
                    pings.clear()
                except Exception as e:
                    return await message.edit_text("Something went wrong in ping module.")
