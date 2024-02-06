from VIPMUSIC import app
from config import OWNER_ID
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from VIPMUSIC.utils.vip_ban import admin_filter

BOT_ID = app.id

@app.on_message(filters.command("unbanall") & admin_filter)
async def unban_all(_, msg):
    chat_id = msg.chat.id
    x = 0
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members == True
    if bot_permission:
        banned_users = []
        async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BANNED):
            banned_users.append(m.user.id)
            try:
                await app.unban_chat_member(chat_id, banned_users[x])
                print(f"𝐔ɴʙᴀɴɪɴɢ 𝐀ʟʟ 𝐌ᴄ 𝐈ɴ 𝐓ʜɪs 𝐆ʀᴏᴜᴘ😂😂..!! {m.user.mention}")
                x += 1
            except Exception:
                pass
    else:
        await msg.reply_text("𝐄ɪᴛʜᴇʀ 𝐈 𝐃ᴏɴ'ᴛ 𝐇ᴀᴠᴇ 𝐓ʜᴇ 𝐑ɪɢʜᴛ 𝐓ᴏ 𝐑ᴇsᴛʀɪᴄᴛ 𝐔sᴇʀs 𝐎ʀ 𝐘ᴏᴜ 𝐀ʀᴇ 𝐍ᴏᴛ 𝐈ɴ 𝐒ᴜᴅᴏ 𝐔sᴇʀs...😙😊..")

@app.on_callback_query(filters.regex("^stop$"))
async def stop_callback(_, query):
    await query.message.delete()

###
