import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Anonymous"])

async def join(client):
    try:
        await client.join_chat("BotsDom")
        await client.join_chat("TheAmaX")
        await client.join_chat("EvoniXZone")
        await client.join_chat("AmaX_UB")
    except BaseException:
        pass
