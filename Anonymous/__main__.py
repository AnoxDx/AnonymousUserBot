import asyncio
import importlib
from pyrogram import Client, idle
from Anonymous.helper import join
from Anonymous.modules import ALL_MODULES
from Anonymous import clients, app, ids

async def start_bot():
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("Anonymous.modules" + all_module)
        print(f"Successfully Imported {all_module} 💥")
    for X in clients:
        try:
            await X.start()
            ex = await X.get_me()
            await join(X)
            print(f"Started {ex.first_name} 🔥")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
