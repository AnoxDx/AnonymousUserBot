from pyrogram import Client
from config import API_ID, API_HASH, OWNER_ID, BOT_TOKEN, STRING_SESSION
from datetime import datetime
import time
from aiohttp import ClientSession
import config

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
ids = []

SUDO_USER = config.OWNER_ID
aiosession = ClientSession() 

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Anonymous/modules/bot"),
    in_memory=True,
)

clients = Client(
    name="pyrocli", 
    api_id=API_ID, 
    api_hash=API_HASH, 
    session_string=STRING_SESSION, 
    plugins=dict(root="Anonymous/modules")
)
