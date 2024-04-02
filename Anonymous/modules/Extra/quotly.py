import asyncio
from pyrogram.types import Message
from Anonymous import app, SUDO_USER
from pyrogram import Client, filters


@Client.on_message(filters.me & filters.command(["q", "quotly"], "."))
async def quotly(client: Client, message: Message):
        reply = message.reply_to_message
        if not reply:
            return await message.edit_text("Reply to any users text message")

        if len(message.command) > 1:
            color = message.text.split(None, 1)[1]
        else:
            color = "black"

        msg_one = await message.edit_text("Making a Quote . . .")
        await client.send_message("QuotLyBot", f"/qcolor {color}")
        await reply.forward("QuotLyBot")
        is_sticker = True
        while is_sticker:
            try:
                msg = await client.get_last_msg(chat_id="QuotLyBot")
                if msg.sticker and msg.sticker.file_id:
                    is_sticker = False
            except Exception:
                await asyncio.sleep(0.10)
        if msg.id:
            await asyncio.gather(
                msg_one.delete(),
                client.copy_message(
                    message.chat.id,
                    "QuotLyBot",
                    msg.id
                )
            )
