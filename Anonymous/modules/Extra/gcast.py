from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import PeerIdInvalid
from Anonymous import app, SUDO_USER


@Client.on_message(filters.command(["gcast"], ".") & (filters.me | filters.user(SUDO_USER)))
async def gcast(client: Client, message: Message):
    tlen = len(message.text.split())

    if tlen == 1:
        return await client.send_message(
            message.from_user.id,
            "Give me some broadcasting message."
        )

    text = message.text.split(None, 1)[1]
    count = 0

    for user_id in client.getdv("BOT STARTED"):
        try:
            await client.resolve_peer(user_id)
            done = await client.send_message(user_id, text)
            if done:
                count += 1
        except PeerIdInvalid:
            pass
    await client.send_message(
        message.from_user.id,
        f"Broadcast done, messages sent to {count} users."
    )


