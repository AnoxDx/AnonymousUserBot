import random
import importlib
import time
import asyncio
from pyrogram.types import Message
import config
from pyrogram import Client, filters

AnoxDx = Client(
  name="PyrogramBot",
  api_id=config.API_ID,
  api_hash=config.API_HASH,
  bot_token=config.BOT_TOKEN
)
