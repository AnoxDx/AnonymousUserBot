from pyrogram import Client
from config import API_ID, API_HASH, OWNER_ID, BOT_TOKEN
from datetime import datetime
import time
from aiohttp import ClientSession
import config

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
clients = []
ids = []

SUDO_USERS = config.OWNER_ID
aiosession = ClientSession()

if API_ID:
   API_ID = API_ID
else:
   print("WARNING: API ID NOT FOUND USING AMAX API ⚡")
   API_ID = "6435225"

if API_HASH:
   API_HASH = API_HASH
else:
   print("WARNING: API HASH NOT FOUND USING AMAX API ⚡")   
   API_HASH = "4e984ea35f854762dcde906dce426c2d"

if not BOT_TOKEN:
   print("WARNING: BOT TOKEN NOT FOUND PLZ ADD ⚡")   

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
)
