import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from VIPMUSIC import app
from VIPMUSIC.utils.vip_ban import admin_filter

SPAM_CHATS = {}

@app.on_message(filters.command(["utag", "uall"], prefixes=["/", "@", ".", "#"]) & admin_filter)
async def tag_all_users(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    if len(message.text.split()) == 1:
        await message.reply_text("𝐆ɪᴠᴇ 𝐒ᴏᴍᴇ 𝐓ᴇxᴛ 𝐓ᴏ 𝐓ᴀɢ 𝐀ʟʟ, 𝐋ɪᴋᴇ `@utag Hi Friends`")
        return

    text = message.text.split(None, 1)[1]
    if text:
        await message.reply_text("𝐔ᴛᴀɢ [𝐔ɴʟɪᴍɪᴛᴇᴅ 𝐓ᴀɢ] 𝐒ᴛᴀʀᴛᴇᴅ 𝐒ᴜᴄᴄᴇssғᴜʟʟʏ!😙😃\n\n**➥ 𝐎ғғ 𝐓ᴀɢɢɪɴɢ 𝐁ʏ /stoputag**")

    SPAM_CHATS[chat_id] = True
    f = True
    while f:
        if SPAM_CHATS.get(chat_id) == False:
            await message.reply_text("𝐔ɴʟɪᴍɪᴛᴇᴅ 𝐓ᴀɢ 𝐀ʟʟ 𝐒ᴜᴄᴄᴇssғᴜʟʟʏ 𝐒ᴛᴏᴘᴘᴇᴅ!😙😀")
            break
        usernum = 0
        usertxt = ""
        try:
            async for m in app.get_chat_members(message.chat.id):
                if m.user.is_bot:
                    continue
                usernum+= 1
                usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
                if usernum == 5:
                    await app.send_message(message.chat.id, f'{text}\n{usertxt}\n\n|| ➥ 𝐎ғғ 𝐓ᴀɢɢɪɴɢ 𝐁ʏ /stoputag ||')
                    usernum = 0
                    usertxt = ""
                    await asyncio.sleep(5)
        except Exception as e:
            print(e)

@app.on_message(filters.command(["stoputag", "stopuall", "offutag", "offuall", "utagoff", "ualloff"], prefixes=["/", ".", "@", "#"]) & admin_filter)
async def stop_tagging(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    if SPAM_CHATS.get(chat_id) == True:
        SPAM_CHATS[chat_id] = False
        return await message.reply_text("𝐓ᴀɢ 𝐏ʀᴏᴄᴇꜱꜱ 𝐒ᴛᴏᴘᴇᴅ 𝐒ᴜᴄᴄᴇꜱꜰᴜʟʟʏ!😙😊")
    except KeyError:
        await message.reply_text("𝐍ᴏ 𝐀ᴄᴛɪᴠᴇ 𝐓ᴀɢɢɪɴɢ 𝐏ʀᴏᴄᴇꜱꜱ 𝐅ᴏᴜɴᴅ!😙😀")
