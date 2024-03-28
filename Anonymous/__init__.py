import asyncio
import time

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram import Client

import config

SUDOERS = config.OWNER_ID

Ano = Client(
    "Anonymous",
    config.API_ID,
    config.API_HASH,
    session_string=config.STRING_SESSION,
)

