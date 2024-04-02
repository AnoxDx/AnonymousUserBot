from Anonymous import app
from pyrogram.types import Message
from pyrogram import filters, Client
from Anonymous import SUDO_USER

@Client.on_message(filters.command(["react"], ".") & filters.me | filters.user(SUDO_USER))
async def react(client: Client, message: Message):
 emoji = message.text.split(" ", 1)[1]
 await client.send_reaction(chat_id=message.chat.id, message_id=message.reply_to_message, emoji=emoji)

@Client.on_message(filters.command(["send"], ".") & filters.me | filters.user(SUDO_USER))
async def react(client: Client, message: Message):
 user_s_to_send = message.text.split(" ", 1)[1]
 emoji = message.text.split(" ", 2)[2]
 await client.send_reaction(chat_id=user_s_to_send, message_id=user_s_to_send, emoji=emoji)


#########################################THIS PLUGIN IS UNDER MAINTAINCE##########################################
