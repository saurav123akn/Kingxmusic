import random 
from pyrogram import filters,Client,enums
from VIPMUSIC import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import ChatPermissions
from VIPMUSIC.mongo.nightmodedb import nightdb,nightmode_on,nightmode_off,get_nightchats 



CLOSE_CHAT = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages = False,
    can_send_other_messages = False,
    can_send_polls = False,
    can_change_info = False,
    can_add_web_page_previews = False,
    can_pin_messages = False,
    can_invite_users = True )


OPEN_CHAT = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages = True,
    can_send_other_messages = True,
    can_send_polls = True,
    can_change_info = True,
    can_add_web_page_previews = True,
    can_pin_messages = True,
    can_invite_users = True )
    
buttons = InlineKeyboardMarkup([[InlineKeyboardButton("๏ 𝐄ɴᴀʙʟᴇ ๏", callback_data="add_night"),InlineKeyboardButton("๏ 𝐃ɪsᴀʙʟᴇ ๏", callback_data="rm_night")]])         
add_buttons = InlineKeyboardMarkup([[InlineKeyboardButton(text= "๏ 𝐀ᴅᴅ 𝐌ᴇ 𝐈ɴ 𝐆ʀᴏᴜᴘ ๏", url=f"https://t.me/{app.username}?startgroup=true")]])
                              
@app.on_message(filters.command("nightmode") & filters.group)
async def _nightmode(_, message):
    return await message.reply_photo(photo="https://telegra.ph/file/5afd222f2ea02250419f9.jpg", caption="**𝐂ʟɪᴄᴋ 𝐎ɴ 𝐓ʜᴇ 𝐁ᴇʟᴏᴡ𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐄ɴᴀʙʟᴇ 𝐎ʀ 𝐃ɪsᴀʙʟᴇ 𝐍ɪɢʜᴛᴍᴏᴅᴇ 𝐈ɴ 𝐓ʜɪs 𝐂ʜᴀᴛ.**",reply_markup=buttons)
              
     
@app.on_callback_query(filters.regex("^(add_night|rm_night)$"))
async def nightcb(_, query : CallbackQuery):
    data = query.data 
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    check_night = await nightdb.find_one({"chat_id" : chat_id})
    administrators = []
    async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)     
    if user_id in administrators:   
        if data == "add_night":
            if check_night:        
                await query.message.edit_caption("**๏ 𝐍ɪɢʜᴛᴍᴏᴅᴇ 𝐈s 𝐀ʟʀᴇᴀᴅʏ 𝐄ɴᴀʙʟᴇᴅ 𝐈ɴ 𝐓ʜɪs 𝐂ʜᴀᴛ.**")
            elif not check_night :
                await nightmode_on(chat_id)
                await query.message.edit_caption("**๏ 𝐀ᴅᴅᴇᴅ 𝐂ʜᴀᴛ 𝐓ᴏ 𝐌ʏ 𝐃ᴀᴛᴀʙᴀsᴇ . 𝐓ʜɪs 𝐆ʀᴏᴜᴘ 𝐖ɪʟʟ 𝐁ᴇ 𝐂ʟᴏsᴇᴅ 𝐎ɴ 𝟷𝟸ᴀᴍ [IST] 𝐀ɴᴅ 𝐖ɪʟʟ 𝐎ᴘᴇɴᴇᴅ 𝐎ɴ 𝟶𝟼ᴀᴍ [IST] .**") 
        if data == "rm_night":
            if check_night:  
                await nightmode_off(chat_id)      
                await query.message.edit_caption("**๏ 𝐍ɪɢʜᴛᴍᴏᴅᴇ 𝐑ᴇᴍᴏᴠᴇᴅ 𝐅ʀᴏᴍ 𝐌ʏ 𝐃ᴀᴛᴀʙᴀsᴇ !**")
            elif not check_night:
                await query.message.edit_caption("**๏  𝐍ɪɢʜᴛᴍᴏᴅᴇ 𝐈s 𝐀ʟʀᴇᴀᴅʏ 𝐃ɪsᴀʙʟᴇᴅ  𝐈ɴ 𝐓ʜɪs 𝐂ʜᴀᴛ.**") 
            
    
    
async def start_nightmode() :
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for add_chat in chats:
        try:
            await app.send_photo(
                add_chat,
                photo="https://telegra.ph/file/ef772b84405e119014317.jpg",
                caption= f"**𝐌ᴀʏ 𝐓ʜᴇ 𝐀ɴɢᴇʟs 𝐅ʀᴏᴍ 𝐇ᴇᴀᴠᴇɴ 𝐁ʀɪɴɢ 𝐓ʜᴇ 𝐒ᴡᴇᴇᴛᴇsᴛ 𝐎ғ 𝐀ʟʟ 𝐃ʀᴇᴀᴍs 𝐅ᴏʀ 𝐘ᴏᴜ. 𝐌ᴀʏ 𝐘ᴏᴜ 𝐇ᴀᴠᴇ 𝐋ᴏɴɢ 𝐀ɴᴅ 𝐁ʟɪssғᴜʟ 𝐒ʟᴇᴇᴘ 𝐅ᴜʟʟ 𝐎ғ 𝐇ᴀᴘᴘʏ 𝐃ʀᴇᴀᴍs.\n\n𝐆ʀᴏᴜᴘ 𝐈s 𝐂ʟᴏsɪɴɢ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 𝐄ᴠᴇʀʏᴏɴᴇ !**",
                reply_markup=add_buttons,)
            
            await app.set_chat_permissions(add_chat,CLOSE_CHAT)

        except Exception as e:
            print(f"[bold red] Unable To close Group {add_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(start_nightmode, trigger="cron", hour=23, minute=59)
scheduler.start()

async def close_nightmode():
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for rm_chat in chats:
        try:
            await app.send_photo(
                rm_chat,
                photo="https://telegra.ph/file/17af366cac1f01baa45be.jpg",
                caption= f"**𝐆ʀᴏᴜᴘ 𝐈s 𝐎ᴘᴇɴɪɴɢ 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ 𝐄ᴠᴇʀʏᴏɴᴇ !\n\n𝐌ᴀʏ 𝐓ʜɪs 𝐃ᴀʏ 𝐂ᴏᴍᴇ 𝐖ɪᴛʜ 𝐀ʟʟ 𝐓ʜᴇ 𝐋ᴏᴠᴇ 𝐘ᴏᴜʀ 𝐇ᴇᴀʀᴛ 𝐂ᴀɴ 𝐇ᴏʟᴅ 𝐀ɴᴅ 𝐁ʀɪɴɢ 𝐘ᴏᴜ 𝐄ᴠᴇʀʏ 𝐒ᴜᴄᴄᴇss 𝐘ᴏᴜ 𝐃ᴇsɪʀᴇ. 𝐌ᴀʏ 𝐄ᴀᴄʜ 𝐎ғ 𝐘ᴏᴜʀ 𝐅ᴏᴏᴛsᴛᴇᴘs 𝐁ʀɪɴɢ 𝐉ᴏʏ 𝐓ᴏ 𝐓ʜᴇ 𝐄ᴀʀᴛʜ 𝐀ɴᴅ 𝐘ᴏᴜʀsᴇʟ 𝐈 𝐖𝐢sʜ 𝐘ᴏᴜ 𝐀 𝐌ᴀɢɪᴄᴀʟ ᴅ𝐃ᴀʏ 𝐀ɴᴅ 𝐀 𝐖ᴏɴᴅᴇʀғᴜʟ 𝐋ɪғᴇ 𝐀ʜᴇᴀᴅ.**",
                reply_markup=add_buttons,)
            await app.set_chat_permissions(rm_chat,OPEN_CHAT)

        except Exception as e:
            print(f"[bold red] Unable To open Group {rm_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(close_nightmode, trigger="cron", hour=6, minute=1)
scheduler.start()


