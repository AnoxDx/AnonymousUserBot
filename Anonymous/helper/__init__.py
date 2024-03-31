import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Anonymous"])

async def join(client):
    try:
        await client.join_chat("BotsDom")
    except BaseException:
        pass
