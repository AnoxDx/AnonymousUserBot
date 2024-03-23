import asyncio
import time

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram import Client

import config

loop = asyncio.get_event_loop()
boot = time.time()

mongo = MongoClient(config.MONGO_DB_URI)
db = mongo.AFK

SUDOERS = config.SUDO_USER

Ano = Client(
    "Anonymous",
    config.API_ID,
    config.API_HASH,
    session_string=config.STRING_SESSION,
)


async def initiate_bot():
    global botid, botname, botusername
    await Ano.start()
    getme = await Ano.get_me()
    botid = getme.id
    botusername = (getme.username).lower()
    if getme.last_name:
        botname = getme.first_name + " " + getme.last_name
    else:
        botname = getme.first_name


loop.run_until_complete(initiate_bot())
