from pyrogram import Client
from config import API_ID, API_HASH, OWNER_ID, BOT_TOKEN, STRING_SESSION
from datetime import datetime
import time
from aiohttp import ClientSession

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
clients = []
accounts = []

SUDO_USER = OWNER_ID
aiosession = ClientSession() 

if STRING_SESSION:
   client = Client(name="pyrocli", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION, plugins=dict(root="Anonymous/modules"))
   clients.append(client)
    
