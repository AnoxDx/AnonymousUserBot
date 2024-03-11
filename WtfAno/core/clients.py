import asyncio
import glob
import importlib
import os
import sys
from pathlib import Path

import pyroaddon  # pylint: disable=unused-import
from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from .config import ENV, Config
from .database import db
from .logger import LOGS


class AnonClient(Client):
    def __init__(self) -> None:
        self.users: list[Client] = []
        self.bot: Client = Client(
            name="AnonymousBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="Wtfano.plugins.bot"),
        )

    async def start_user(self) -> None:
        sessions = await db.get_all_sessions()
        for i, session in enumerate(sessions):
            try:
                client = Client(
                    name=f"User#{i + 1}",
                    api_id=Config.API_ID,
                    api_hash=Config.API_HASH,
                    session_string=session["session"],
                )
                await client.start()
                me = await client.get_me()
                self.users.append(client)
                LOGS.info(
                    f"{Symbols.arrow_right * 2} Started User {i + 1}: '{me.first_name}' {Symbols.arrow_left * 2}"
                )
                is_in_logger = await self.validate_logger(client)
                if not is_in_logger:
                    LOGS.warning(
                        f"Client #{i+1}: '{me.first_name}' is not in Logger Group! Check and add manually for proper functioning."
                    )
                try:
                   await self.one.join_chat("EvonixZone")
                   await self.two.join_chat("BotsDom")
                   await self.three.join_chat("OurTopics")
                pass
                   assistants.append(1)
                try:
                   await self.one.send_message(config.LOGGER_ID, "AnonymousBot Started")
                except:
                   LOGGER(__name__).error(
                    "Userbot has failed to access the log Group. Make sure that you have added User to your log group and promoted as admin!"
                )
                   exit()
                   self.one.id = self.one.me.id
                   self.one.name = self.one.me.mention
                   self.one.username = self.one.me.username
                   assistantids.append(self.one.id)
                   LOGGER(__name__).info(f"Assistant Started as {self.one.name}")

    async def start_bot(self) -> None:
        await self.bot.start()
        me = await self.bot.get_me()
        LOGS.info(
            f"➥ Started AnonymousBot Client..."
        )

    async def load_plugin(self) -> None:
        count = 0
        files = glob.glob("WtfAno/plugins/user/*.py")
        unload = await db.get_env(ENV.unload_plugins) or ""
        unload = unload.split(" ")
        for file in files:
            with open(file) as f:
                path = Path(f.name)
                shortname = path.stem.replace(".py", "")
                if shortname in unload:
                    os.remove(Path(f"WtfAno/plugins/user/{shortname}.py"))
                    continue
                if shortname.startswith("__"):
                    continue
                fpath = Path(f"Hellbot/plugins/user/{shortname}.py")
                name = "Hellbot.plugins.user." + shortname
                spec = importlib.util.spec_from_file_location(name, fpath)
                load = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(load)
                sys.modules["WtfAno.plugins.user." + shortname] = load
                count += 1
            f.close()
        LOGS.info(
            f"≛ Loaded User Plugins"
        )

    async def validate_logger(self, client: Client) -> bool:
        try:
            await client.get_chat_member(Config.LOGGER_ID, "me")
            return True
        except Exception:
            return await self.join_logger(client)

    async def join_logger(self, client: Client) -> bool:
        try:
            invite_link = await self.bot.export_chat_invite_link(Config.LOGGER_ID)
            await client.join_chat(invite_link)
            return True
        except Exception:
            return False

    async def start_message(self, version: dict) -> None:
        await self.bot.send_animation(
            Config.LOGGER_ID,
            "https://te.legra.ph/file/8deca5343c64d9db9401f.mp4",
            f"**⇛ 𝖳𝗁𝖾 𝖠𝗇𝗈𝗇𝗒𝗆𝗈𝗎𝗌 𝖡𝗈𝗍 𝗂𝗌 𝖠𝖼𝗍𝗂𝗏𝖺𝗍𝖾𝖽**\n\n"
            f"**⇛ 𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆 𝖵𝖾𝗋𝗌𝗂𝗈𝗇:** `{version['pyrogram']}`\n"
            f"**⇛ 𝖯𝗒𝗍𝗁𝗈𝗇 𝖵𝖾𝗋𝗌𝗂𝗈𝗇:** `{version['python']}`\n\n",
            parse_mode=ParseMode.MARKDOWN,
            disable_notification=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("𝘚𝘰𝘶𝘳𝘤𝘦", url="https://github.com/AnoxDx/AnonymousUserBot"),
                    ],
                    [
                        InlineKeyboardButton("𝘜𝘱𝘥𝘢𝘵𝘦𝘴", url="https://t.me/BotsDom"),
                    ],
                ]
            ),
        )

    async def startup(self) -> None:
        LOGS.info(
            f"꙰ 𝘐𝘵'𝘴 𝘈𝘯𝘰𝘯𝘺𝘮𝘰𝘶𝘴 𝘜𝘴𝘦𝘳 𝘉𝘰𝘵  ꙰"
        )
        await self.start_bot()
        await self.start_user()
        await self.load_plugin()


class CustomMethods(AnonClient):
    async def input(self, message: Message) -> str:
        """Get the input from the user"""
        if len(message.command) < 2:
            output = ""

        else:
            try:
                output = message.text.split(" ", 1)[1].strip() or ""
            except IndexError:
                output = ""

        return output

    async def edit(
        self,
        message: Message,
        text: str,
        parse_mode: ParseMode = ParseMode.DEFAULT,
        no_link_preview: bool = True,
    ) -> Message:
        """Edit or Reply to a message, if possible"""
        if message.from_user and message.from_user.id in Config.STAN_USERS:
            if message.reply_to_message:
                return await message.reply_to_message.reply_text(
                    text,
                    parse_mode=parse_mode,
                    disable_web_page_preview=no_link_preview,
                )
            return await message.reply_text(
                text, parse_mode=parse_mode, disable_web_page_preview=no_link_preview
            )
        return await message.edit_text(
            text, parse_mode=parse_mode, disable_web_page_preview=no_link_preview
        )

    async def _delete(self, message: Message, delay: int = 0) -> None:
        """Delete a message after a certain period of time"""
        await asyncio.sleep(delay)
        await message.delete()

    async def delete(
        self, message: Message, text: str, delete: int = 10, in_background: bool = True
    ) -> None:
        """Edit a message and delete it after a certain period of time"""
        to_del = await self.edit(message, text)
        if in_background:
            asyncio.create_task(self._delete(to_del, delete))
        else:
            await self._delete(to_del, delete)

    async def error(self, message: Message, text: str, delete: int = 10) -> None:
        """Edit an error message and delete it after a certain period of time if mentioned"""
        to_del = await self.edit(message, f"{Symbols.cross_mark} **Error:** \n\n{text}")
        if delete:
            asyncio.create_task(self._delete(to_del, delete))

    async def _log(self, tag: str, text: str, file: str = None) -> None:
        """Log a message to the Logger Group"""
        msg = f"**#{tag.upper()}**\n\n{text}"
        try:
            if file:
                try:
                    await self.bot.send_document(Config.LOGGER_ID, file, caption=msg)
                except:
                    await self.bot.send_message(
                        Config.LOGGER_ID, msg, disable_web_page_preview=True
                    )
            else:
                await self.bot.send_message(
                    Config.LOGGER_ID, msg, disable_web_page_preview=True
                )
        except Exception as e:
            raise Exception(f"{Symbols.cross_mark} LogErr: {e}")

    async def check_and_log(self, tag: str, text: str, file: str = None) -> None:
        """Check if :
        \n-> the Logger Group is available
        \n-> the logging is enabled"""
        status = await db.get_env(ENV.is_logger)
        if status and status.lower() == "true":
            await self._log(tag, text, file)


Anonymous = CustomMethods()
