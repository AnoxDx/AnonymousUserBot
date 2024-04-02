import time
import wikipediaapi
from pyrogram.types import Message
from pyrogram import Client, filters
from Anonymous import app, SUDO_USER



@Client.on_message(filters.command("wiki", ".") & filters.me)
async def wiki(bot: Client, message: Message):
    if len(message.command) == 1:
        await message.edit_text("Give me some query to search on wikipedia . . .")

    elif len(message.command) > 1 and len(message.command) < 4096:
        try:
            obj = wikipediaapi.Wikipedia("en")
            text = message.text.split(None, 1)[1]
            result = obj.page(text)
            await message.edit_text(f"Searching for: __{text}__ . . .")
            if result:
                giveresult = result.summary
                if len(giveresult) <= 4096:
                    await message.edit_text(f"**Results for:** `{text}`\n\n```{giveresult}```")
                else:
                    await message.edit_text(f"**Results for:** `{text}`\n\n```{giveresult[:4095]}```")
            else:
                await message.edit_text("No results found !")
        except Exception as e:
            await message.edit_text("Something went wrong !\n\n: {e}")
    else:
        await message.edit_text("Something went wrong !")
