import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from Anonymous import SUDO_USER
from Anonymous import app
from Anonymous.helper import UserType


@Client.on_message(filters.command(["spam"], ".") & (filters.me | filters.user(SUDO_USER)))
async def spam_handler(client: Client, message: Message):
        reply = client.reply_to_message
        reply_to_id = reply.id if reply else None
        cmd = client.text.split(None, 2)
        if not reply and app.long() == 1:
            await client.send_edit(
                "Reply or give me count & spam text after command.",
                delme=4
            )

        elif not reply and app.long() > 1:
            await m.delete()
            times = int(cmd[1]) if cmd[1].isdigit() else 0
            spam_msg = cmd[2]
            for _ in range(times):
                await client.send_message(
                    message.chat.id,
                    spam_msg,
                    reply_to_message_id=reply_to_id
                )
                await asyncio.sleep(0.10)

        elif reply:
            await message.delete()
            times = int(cmd[1]) if cmd[1].isdigit() else 0
            spam_msg = reply.id
            for _ in range(times):
                await client.copy_message(
                    message.chat.id,
                    message.chat.id,
                    spam_msg
                )



@Client.on_message(
    filters.command(["dspam", "delayspam"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def delayspam_handler(client: Client, message: Message):
        reply = message.reply_to_message
        cmd = message.command
        if client.long() < 3:
            await client.send_edit(
                f"Use like this: `.dspam [count spam] [delay time in seconds] [text messages]`"
            )

        elif app.long() > 2 and not reply:
            await message.delete()
            msg = message.text.split(None, 3)
            times = int(msg[1]) if msg[1].isdigit() else None
            sec = int(msg[2]) if msg[2].isdigit() else None
            text = msg[3]
            for _ in range(times):
                await client.send_message(
                    message.chat.id,
                    text
                )
                await asyncio.sleep(sec)
        else:
            await client.send_edit("Something wrong in spam command !")
