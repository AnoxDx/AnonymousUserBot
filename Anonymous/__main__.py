import asyncio
import importlib
from pyrogram import Client, idle
from Anonymous.helper import join
from Anonymous.modules import ALL_MODULES
from Anonymous import clients, app, ids

async def start_bot():
    await app.start()
    print("started..")
    for all_module in ALL_MODULES:
        importlib.import_module("Anonymous.modules" + all_module)
        print(f"Successfully Imported {all_module} !")
    for cli in clients:
        try:
            await cli.start()
            Ub = await cli.get_me()
            await join(X)
            print("<<<Started UB>>>")
            ids.append(Ub.id)
        except Exception as e:
            print(f"{e}")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
