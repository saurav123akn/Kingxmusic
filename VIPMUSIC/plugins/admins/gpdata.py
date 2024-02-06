from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from VIPMUSIC import app
from config import OWNER_ID
from VIPMUSIC.misc import SUDOERS
from pyrogram.types import Message
from VIPMUSIC.utils.vip_ban import admin_filter
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton



# ------------------------------------------------------------------------------- #


@app.on_message(filters.command("pin") & admin_filter & SUDOERS)
async def pin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("𝐒ᴏʀʀʏ 𝐃ᴀʀʟɪɴɢ 𝐁ᴜᴛ 𝐓ʜɪs 𝐂ᴏᴍᴍᴀɴᴅ 𝐖ᴏʀᴋs 𝐎ɴʟʏ 𝐎ɴ 𝐆ʀᴏᴜᴘs !!!😊😙")
    elif not replied:
        await message.reply_text("𝐏ʟᴢᴢ 𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐌ᴇssᴀɢᴇ 𝐓ᴏ 𝐏ɪɴ 𝐈ᴛ")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.pin()
                await message.reply_text(f"𝐈 𝐇ᴀᴠᴇ 𝐒ᴜᴄᴄᴇssғᴜʟʟʏ 𝐏ɪɴɴᴇᴅ 𝐌ᴇssᴀɢᴇ!\n\nᴄʜᴀᴛ: {chat_title}\n𝐀ᴅᴍɪɴ: {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 𝐕ɪᴇᴡ 𝐌ᴇssᴀɢᴇ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))


@app.on_message(filters.command("pinned"))
async def pinned(_, message):
    chat = await app.get_chat(message.chat.id)
    if not chat.pinned_message:
        return await message.reply_text("𝐔ꜰꜰꜰꜰ 𝐍ᴏ 𝐏ɪɴɴᴇᴅ 𝐌ᴇssᴀɢᴇ 𝐅ᴏᴜɴᴅ😢...")
    try:        
        await message.reply_text("𝐇ᴇʏ 𝐉ᴀᴀɴ 𝐇ᴇʀᴇ 𝐈s 𝐓ʜᴇ 𝐋ᴀᴛᴇsᴛ 𝐏ɪɴɴᴇᴅ 𝐌ᴇssᴀɢᴇ😙😁...",reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton(text="📝 𝐕ɪᴇᴡ 𝐌ᴇssᴀɢᴇ",url=chat.pinned_message.link)]]))  
    except Exception as er:
        await message.reply_text(er)


# ------------------------------------------------------------------------------- #

@app.on_message(filters.command("unpin") & admin_filter & SUDOERS)
async def unpin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("𝐒ᴏʀʀʏ 𝐃ᴀʀʟɪɴɢ 𝐁ᴜᴛ 𝐓ʜɪs 𝐂ᴏᴍᴍᴀɴᴅ 𝐖ᴏʀᴋs 𝐎ɴʟʏ 𝐎ɴ 𝐆ʀᴏᴜᴘs !!!😊😙")
    elif not replied:
        await message.reply_text("𝐑ᴇᴘʟʏ 𝐓ᴏ ᴀ 𝐌ᴇssᴀɢᴇ 𝐓ᴏ 𝐔ɴᴘɪɴ 𝐈ᴛ !")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.unpin()
                await message.reply_text(f"𝐒ᴜᴄᴄᴇssғᴜʟʟʏ 𝐔ɴᴘɪɴɴᴇᴅ 𝐌ᴇssᴀɢᴇ!\n\n**ᴄʜᴀᴛ:** {chat_title}\n**ᴀᴅᴍɪɴ:** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 ᴠɪᴇᴡs ᴍᴇssᴀɢᴇ ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))




# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("removephoto") & admin_filter & SUDOERS)
async def deletechatphoto(_, message):
      
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("𝐏ʀᴏᴄᴇssɪɴɢ....😁😁...")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("𝐒ᴏʀʀʏ 𝐃ᴀʀʟɪɴɢ 𝐁ᴜᴛ 𝐓ʜɪs 𝐂ᴏᴍᴍᴀɴᴅ 𝐖ᴏʀᴋs 𝐎ɴʟʏ 𝐎ɴ 𝐆ʀᴏᴜᴘs !!!😊😙") 
      try:
         if admin_check.privileges.can_change_info:
             await app.delete_chat_photo(chat_id)
             await msg.edit("𝐒ᴜᴄᴄᴇssғᴜʟʟʏ 𝐑ᴇᴍᴏᴠᴇᴅ 𝐏ʀᴏғɪʟᴇ 𝐏ʜᴏᴛᴏ 𝐅ʀᴏᴍ 𝐆ʀᴏᴜᴘ !\nʙʏ {}".format(message.from_user.mention))    
      except:
          await msg.edit("𝐓ʜᴇ 𝐔sᴇʀ 𝐌ᴏsᴛ 𝐍ᴇᴇᴅ 𝐂ʜᴀɴɢᴇ 𝐈ɴғᴏ 𝐀ᴅᴍɪɴ 𝐑ɪɢʜᴛs 𝐓ᴏ 𝐑ᴇᴍᴏᴠᴇ 𝐆ʀᴏᴜᴘ 𝐏ʜᴏᴛᴏ !")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("setphoto")& admin_filter & SUDOERS)
async def setchatphoto(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("𝐏ʀᴏᴄᴇssɪɴɢ....😁😁...")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("𝐒ᴏʀʀʏ 𝐃ᴀʀʟɪɴɢ 𝐁ᴜᴛ 𝐓ʜɪs 𝐂ᴏᴍᴍᴀɴᴅ 𝐖ᴏʀᴋs 𝐎ɴʟʏ 𝐎ɴ 𝐆ʀᴏᴜᴘs !!!😊😙") 
      elif not reply:
           await msg.edit("𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐏ʜᴏᴛᴏ 𝐎ʀ 𝐃ᴏᴄᴜᴍᴇɴᴛ.")
      elif reply:
          try:
             if admin_check.privileges.can_change_info:
                photo = await reply.download()
                await message.chat.set_photo(photo=photo)
                await msg.edit_text("𝐒ᴜᴄᴄᴇssғᴜʟʟʏ 𝐍ᴇᴡ 𝐏ʀᴏғɪʟᴇ 𝐏ʜᴏᴛᴏ 𝐈ɴsᴇʀᴛ !\nʙʏ {}".format(message.from_user.mention))
             else:
                await msg.edit("𝐒ᴏᴍᴇᴛʜɪɴɢ 𝐖ʀᴏɴɢ 𝐇ᴀᴘᴘᴇɴᴇᴅ 𝐓ʀʏ 𝐀ɴᴏᴛʜᴇʀ 𝐏ʜᴏᴛᴏ !")
     
          except:
              await msg.edit("𝐓ʜᴇ 𝐔sᴇʀ 𝐌ᴏsᴛ 𝐍ᴇᴇᴅ 𝐂ʜᴀɴɢᴇ 𝐈ɴғᴏ 𝐀ᴅᴍɪɴ 𝐑ɪɢʜᴛs 𝐓ᴏ 𝐑ᴇᴍᴏᴠᴇ 𝐆ʀᴏᴜᴘ 𝐏ʜᴏᴛᴏ !")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("settitle")& admin_filter & SUDOERS)
async def setgrouptitle(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("𝐏ʀᴏᴄᴇssɪɴɢ....😁😁...")
    if message.chat.type == enums.ChatType.PRIVATE:
          await msg.edit("𝐒ᴏʀʀʏ 𝐃ᴀʀʟɪɴɢ 𝐁ᴜᴛ 𝐓ʜɪs 𝐂ᴏᴍᴍᴀɴᴅ 𝐖ᴏʀᴋs 𝐎ɴʟʏ 𝐎ɴ 𝐆ʀᴏᴜᴘs !!!😊😙")
    elif reply:
          try:
            title = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**sᴜᴄᴄᴇssғᴜʟʟʏ ɴᴇᴡ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ɪɴsᴇʀᴛ !\nʙʏ** {}".format(message.from_user.mention))
          except AttributeError:
                await msg.edit("𝐓ʜᴇ 𝐔sᴇʀ 𝐌ᴏsᴛ 𝐍ᴇᴇᴅ 𝐂ʜᴀɴɢᴇ 𝐈ɴғᴏ 𝐀ᴅᴍɪɴ 𝐑ɪɢʜᴛs 𝐓ᴏ 𝐂ʜᴀɴɢᴇ 𝐆ʀᴏᴜᴘ 𝐓ɪᴛʟᴇ !")   
    elif len(message.command) >1:
        try:
            title = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("𝐒ᴜᴄᴄᴇssғᴜʟʟʏ 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ 𝐍ᴀᴍᴇ 𝐈ɴsᴇʀᴛ !\nʙʏ** {}".format(message.from_user.mention))
        except AttributeError:
               await msg.edit("𝐓ʜᴇ 𝐔sᴇʀ 𝐌ᴏsᴛ 𝐍ᴇᴇᴅ 𝐂ʜᴀɴɢᴇ 𝐈ɴғᴏ 𝐀ᴅᴍɪɴ 𝐑ɪɢʜᴛs 𝐓ᴏ 𝐂ʜᴀɴɢᴇ 𝐆ʀᴏᴜᴘ 𝐓ɪᴛʟᴇ !")
          

    else:
       await msg.edit("𝐘ᴏᴜ 𝐍ᴇᴇᴅ 𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐓ᴇxᴛ 𝐎ʀ 𝐆𝐢ᴠᴇ 𝐒ᴏᴍᴇ 𝐓ᴇxᴛ 𝐓ᴏ 𝐂ʜᴀɴɢᴇ 𝐆ʀᴏᴜᴘ 𝐓ɪᴛʟᴇ")


# --------------------------------------------------------------------------------- #



@app.on_message(filters.command("setdiscription") & admin_filter & SUDOERS)
async def setg_discription(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("𝐏ʀᴏᴄᴇssɪɴɢ....😁😁...")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("𝐒ᴏʀʀʏ 𝐃ᴀʀʟɪɴɢ 𝐁ᴜᴛ 𝐓ʜɪs 𝐂ᴏᴍᴍᴀɴᴅ 𝐖ᴏʀᴋs 𝐎ɴʟʏ 𝐎ɴ 𝐆ʀᴏᴜᴘs !!!😊😙")
    elif reply:
        try:
            discription = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("𝐒ᴜᴄᴄᴇssғᴜʟʟʏ 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ 𝐃ɪsᴄʀɪᴘᴛɪᴏɴ 𝐈ɴsᴇʀᴛ!\nʙʏ {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("𝐓ʜᴇ 𝐔sᴇʀ 𝐌ᴜsᴛ 𝐇ᴀᴠᴇ 𝐂ʜᴀɴɢᴇ 𝐈ɴғᴏ 𝐀ᴅᴍɪɴ 𝐑ɪɢʜᴛs 𝐓ᴏ 𝐂ʜᴀɴɢᴇ 𝐆ʀᴏᴜᴘ 𝐃ɪsᴄʀɪᴘᴛɪᴏɴ!")   
    elif len(message.command) > 1:
        try:
            discription = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("𝐒ᴜᴄᴄᴇssғᴜʟʟʏ 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ 𝐃ɪsᴄʀɪᴘᴛɪᴏɴ 𝐈ɴsᴇʀᴛ!\nʙʏ {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("𝐓ʜᴇ 𝐔sᴇʀ 𝐌ᴜsᴛ 𝐇ᴀᴠᴇ 𝐂ʜᴀɴɢᴇ 𝐈ɴғᴏ 𝐀ᴅᴍɪɴ 𝐑ɪɢʜᴛs 𝐓ᴏ 𝐂ʜᴀɴɢᴇ 𝐆ʀᴏᴜᴘ 𝐃ɪsᴄʀɪᴘᴛɪᴏɴ!")
    else:
        await msg.edit("𝐘ᴏᴜ 𝐍ᴇᴇᴅ 𝐓ᴏ 𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐓ᴇxᴛ 𝐎ʀ 𝐆ɪᴠᴇ 𝐒ᴏᴍᴇ 𝐓ᴇxᴛ 𝐓ᴏ 𝐂ʜᴀɴɢᴇ 𝐆ʀᴏᴜᴘ 𝐃ɪsᴄʀɪᴘᴛᴏɴ!")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("leavegroup")& SUDOERS)
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = "**sᴜᴄᴄᴇssғᴜʟʟʏ ʜɪʀᴏ !!.**"
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)


# --------------------------------------------------------------------------------- #

