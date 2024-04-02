from pyrogram.types import Message
from pyrogram.enums import ChatType
from pyrogram import Client, filters
from Anonymous import app
from Anonymous.helper.Pyt import ReplyCheck

@Client.on_message(filters.command(["stats"], ".") & filters.me)
async def stats(client: Client, message: Message):
    Ano = await message.edit_text("`Collecting stats...`")
    bot = 0
    user = 0
    group = 0
    channel = 0
    stats_format = """
➨ **STATS :**

➥ **BOTS:** {}
➥ **USERS:** {}
➥ **GROUPS:** {}
➥ **CHANNELS:** {}

**© Collected by [AmaX UserBot](https://t.me/TheAmaX) !**
"""

    async for A in client.get_dialogs():
        if A.chat.type == ChatType.CHANNEL:
            channel += 1
        if A.chat.type == ChatType.BOT:
            bot += 1
        if A.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
            group += 1
        if A.chat.type == ChatType.PRIVATE:
            user += 1

    await Ano.edit_text(stats_format.format(bot, user, group, channel))
