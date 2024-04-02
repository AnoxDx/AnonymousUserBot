from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
DEVS = [1669178360, 1450303652]
from Anonymous.helper.PyroHelpers import get_ub_chats
from Anonymous.modules.basic.profile import extract_user, extract_user_and_reason
from Anonymous.database import gmutedb as Gmute
from Anonymous.modules.help import *

ok = []

@Client.on_message(filters.command("gmute", ".") & filters.me)
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"`Please specify a valid user!`")
        return
    if user.id == client.me.id:
        return await ex.edit("**Soon**")
    if user.id in DEVS:
        return await ex.edit("**He is Dev**")
    try:
        replied_user = reply.from_user
        if replied_user.is_self:
            return await ex.edit("`you can't gmute yourself.`")
    except BaseException:
        pass

    try:
        if (await Gmute.is_gmuted(user.id)):
            return await ex.edit("`User already gmuted`")
        await Gmute.gmute(user.id)
        ok.append(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) globally gmuted!")
        try:
            common_chats = await client.get_common_chats(user.id)
            for i in common_chats:
                await i.restrict_member(user.id, ChatPermissions())
        except BaseException:
            pass
    
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(filters.command("ungmute", ".") & filters.me)
async def ungmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"`Please specify a valid user!`")
        return

    try:
        replied_user = reply.from_user
        if replied_user.is_self:
            return await ex.edit("`Calm down anybob, you can't ungmute yourself.`")
    except BaseException:
        pass

    try:
        if not (await Gmute.is_gmuted(user.id)):
            return await ex.edit("`User already ungmuted`")
        await Gmute.ungmute(user.id)
        ok.remove(user.id)
        try:
            common_chats = await client.get_common_chats(user.id)
            for i in common_chats:
                await i.unban_member(user.id)
        except BaseException:
            pass
        await ex.edit(
            f"[{user.first_name}](tg://user?id={user.id}) globally ungmuted!"
        )
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(filters.command("listgmute", ".") & filters.me)
async def gmutelist(client: Client, message: Message):
    users = (await Gmute.gmute_list())
    ex = await message.edit_text("`Processing...`")
    if not users:
        return await ex.edit("There are no Muted Users yet")
    gmute_list = "**GMuted Users:**\n"
    count = 0
    for i in users:
        count += 1
        gmute_list += f"**{count} -** `{i.sender}`\n"
    return await ex.edit(gmute_list)

if ok:
 @Client.on_message(filters.incoming & filters.group)
 async def globals_check(client: Client, message: Message):
    if not message:
        return
    if not message.from_user:
        return
    user_id = message.from_user.id
    chat_id = message.chat.id
    if not user_id:
        return
    if (await Zaid.gban_info(user_id)):
        try:
            await client.ban_chat_member(chat_id, user_id)
        except BaseException:
            pass

    if (await Gmute.is_gmuted(user_id)):
        try:
            await message.delete()
        except errors.RPCError:
            pass
        try:
            await client.restrict_chat_member(chat_id, user_id, ChatPermissions())
        except BaseException:
            pass

    message.continue_propagation()

