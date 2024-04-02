from pyrogram.types import Message
from pyrogram.enums import ChatType
from pyrogram import Client, filters
from Anonymous import app

@Client.on_message(filters.command(["stats"], ".") & filters.me)
async def stats(client: Client, message: Message):
    """ dialogstats handler for stats plugin """
    try:
        await client.send_edit("`Getting stats . . .`")

        bot = 0
        user = 0
        group = 0
        channel = 0
        stats_format = """
        • **STATS FOR:** {}

        🤖 • **BOTS:** {}
        👨 • **USERS:** {}
        🛡️ • **GROUPS:** {}
        ⚙️ • **CHANNELS:** {}
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

        await client.send_edit(stats_format.format(client.UserMention(), bot, user, group, channel))
    except Exception as e:
        await client.error(e)
