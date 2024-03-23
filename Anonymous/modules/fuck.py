from Anonymous import Ano
from pyrogram.types import Message
from pyrogram import Client, filters
import config

@Ano.on_message(filters.command(["fuck"], ".") & (filters.me))
async def fuck(client, message):
   X = await message.reply_text("**Fucking...**")
   time.sleep(1.0)
   await Ano.edit_message_text(chat_id=message.chat.id, message_id=X.id, text="""**.                       /¯ )
                      /¯  /
                    /    /
              /´¯/'   '/´¯¯•¸
          /'/   /    /       /¨¯\
        ('(   (   (   (  ¯~/'  ')
         \                        /
          \                _.•´
            \              (
              \**""")

add_command_help(
    "fuck",
    [
        [".fuck", "Its animation command just try it..."],
    ],
)
