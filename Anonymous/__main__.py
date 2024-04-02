import asyncio
import importlib
from pyrogram import Client, idle
from Anonymous.helper import join
from Anonymous.modules import ALL_MODULES
from Anonymous import clients, app, accounts

async def run_bot():
    await app.start()
    print("started..")
    for all_module in ALL_MODULES:
        importlib.import_module("Anonymous.modules" + all_module)
        print(f"Successfully Imported {all_module} !")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            print("Started !")
            accounts.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(run_bot())
