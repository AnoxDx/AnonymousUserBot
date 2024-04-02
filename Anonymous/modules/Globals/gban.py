from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
DEVS = [1669178360, 1450303652]
from Anonymous.helper.Pyt import get_ub_chats
from Anonymous.modules.basic.profile import extract_user, extract_user_and_reason
from Anonymous.database import gbandb as Ano
from Anonymous.modules.help import *

ok = []

@Client.on_message(filters.command("gban", ".") & filters.me)
async def gban_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`Gbanning...`")
    else:
        ex = await message.edit("`Gbanning....`")
    if not user_id:
        return await ex.edit("I can't find that user.")
    if user_id == client.me.id:
        return await ex.edit("**...**")
    if user_id in DEVS:
        return await ex.edit("**He is Dev**")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`Please specify a valid user!`")

    if (await Ano.gban_info(user.id)):
        return await ex.edit(
            f"[user](tg://user?id={user.id}) **it's already on the gbanned list**"
        )
    f_chats = await get_ub_chats(client)
    if not f_chats:
        return await ex.edit("**You don't have a GC that you admin 🥺**")
    er = 0
    done = 0
    for gokid in f_chats:
        try:
            await client.ban_chat_member(chat_id=gokid, user_id=int(user.id))
            done += 1
        except BaseException:
            er += 1
    await Ano.gban_user(user.id)
    ok.append(user.id)
    msg = (
        r"**\\#GBanned_User//**"
        f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    msg += f"\n**Affected To:** `{done}` **Chats**"
    await ex.edit(msg)


@Client.on_message(filters.command("ungban", ".") & filters.me)
async def ungban_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply("`UnGbanning...`")
    else:
        ex = await message.edit("`UnGbanning....`")
    if not user_id:
        return await ex.edit("I can't find that user.")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`Please specify a valid user!`")

    try:
        if not (await Ano.gban_info(user.id)):
            return await ex.edit("`User already ungban`")
        ung_chats = await get_ub_chats(client)
        ok.remove(user.id)
        if not ung_chats:
            return await ex.edit("**Damn ! You don't have any group**")
        er = 0
        done = 0
        for good_boi in ung_chats:
            try:
                await client.unban_chat_member(chat_id=good_boi, user_id=user.id)
                done += 1
            except BaseException:
                er += 1
        await Ano.ungban_user(user.id)
        msg = (
            r"**\\#UnGbanned_User//**"
            f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})"
            f"\n**User ID:** `{user.id}`"
        )
        if reason:
            msg += f"\n**Reason:** `{reason}`"
        msg += f"\n**Affected To:** `{done}` **Chats**"
        await ex.edit(msg)
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(filters.command("listgban", ".") & filters.me)
async def gbanlist(client: Client, message: Message):
    users = (await Ano.gban_list())
    ex = await message.edit_text("`Processing...`")
    if not users:
        return await ex.edit("No Users have been Banned yet")
    gban_list = "**GBanned Users:**\n"
    count = 0
    for i in users:
        count += 1
        gban_list += f"**{count} -** `{i.sender}`\n"
    return await ex.edit(gban_list)
