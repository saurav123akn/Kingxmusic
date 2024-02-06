from asyncio import sleep
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import MessageDeleteForbidden, RPCError
from pyrogram.types import Message
from VIPMUSIC.utils.vip_ban import admin_filter
from VIPMUSIC import app


@app.on_message(filters.command("purge") & admin_filter)
async def purge(app: app, msg: Message):
    
    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="𝐈 𝐂ᴀɴ'ᴛ 𝐏ᴜʀɢᴇ 𝐌ᴇssᴀɢᴇs 𝐈ɴ 𝐀 𝐁ᴀsɪᴄ 𝐆ʀᴏᴜᴘ 𝐌ᴀᴋᴇ 𝐒ᴜᴘᴇʀ 𝐆ʀᴏᴜᴘ.")
        return

    if msg.reply_to_message:
        message_ids = list(range(msg.reply_to_message.id, msg.id))

        def divide_chunks(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        
        m_list = list(divide_chunks(message_ids))

        try:
            for plist in m_list:
                await app.delete_messages(chat_id=msg.chat.id, message_ids=plist, revoke=True)
                
            await msg.delete()
        except MessageDeleteForbidden:
            await msg.reply_text(text="𝐈 𝐂ᴀɴ'ᴛ 𝐃ᴇʟᴇᴛᴇ 𝐀ʟʟ 𝐌ᴇssᴀɢᴇs. 𝐓ʜᴇ 𝐌ᴇssᴀɢᴇs 𝐌ᴀʏ 𝐁ᴇ 𝐓ᴏᴏ 𝐎ʟᴅ, 𝐈 𝐌ɪɢʜᴛ 𝐍ᴏᴛ 𝐇ᴀᴠᴇ 𝐃ᴇʟᴇᴛᴇ 𝐑ɪɢʜᴛs, 𝐎ʀ 𝐓ʜɪs 𝐌ɪɢʜᴛ 𝐍ᴏᴛ 𝐁ᴇ 𝐀 𝐒ᴜᴘᴇʀɢʀᴏᴜᴘ!!....")
            return
            
        except RPCError as ef:
            await msg.reply_text(text=f"𝐔ꜰꜰꜰ 𝐒ᴏᴍᴇ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀᴇᴅ, 𝐑ᴇᴘᴏʀᴛ 𝐈ᴛ 𝐔sɪɴɢ😢😣...`/bug`<b>ᴇʀʀᴏʀ:</b> <code>{ef}</code>")
        count_del_msg = len(message_ids)
        sumit = await msg.reply_text(text=f"ᴅᴇʟᴇᴛᴇᴅ <i>{count_del_msg}</i> ᴍᴇssᴀɢᴇs")
        await sleep(3)
        await sumit.delete()
        return
    await msg.reply_text("𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐌ᴇssᴀɢᴇ 𝐓ᴏ 𝐒ᴛᴀʀᴛ 𝐏ᴜʀɢᴇ !")
    return





@app.on_message(filters.command("spurge") & admin_filter)
async def spurge(app: app, msg: Message):

    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="𝐈 𝐂ᴀɴ'ᴛ 𝐏ᴜʀɢᴇ 𝐌ᴇssᴀɢᴇs 𝐈ɴ 𝐀 𝐁ᴀsɪᴄ 𝐆ʀᴏᴜᴘ 𝐌ᴀᴋᴇ 𝐒ᴜᴘᴇʀ 𝐆ʀᴏᴜᴘ.")
        return

    if msg.reply_to_message:
        message_ids = list(range(msg.reply_to_message.id, msg.id))

        def divide_chunks(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        m_list = list(divide_chunks(message_ids))

        try:
            for plist in m_list:
                await app.delete_messages(chat_id=msg.chat.id, message_ids=plist, revoke=True)
            await msg.delete()
        except MessageDeleteForbidden:
            await msg.reply_text(text="𝐈 𝐂ᴀɴ'ᴛ 𝐃ᴇʟᴇᴛᴇ 𝐀ʟʟ 𝐌ᴇssᴀɢᴇs. 𝐓ʜᴇ 𝐌ᴇssᴀɢᴇs 𝐌ᴀʏ 𝐁ᴇ 𝐓ᴏᴏ 𝐎ʟᴅ, 𝐈 𝐌ɪɢʜᴛ 𝐍ᴏᴛ 𝐇ᴀᴠᴇ 𝐃ᴇʟᴇᴛᴇ 𝐑ɪɢʜᴛs, 𝐎ʀ 𝐓ʜɪs 𝐌ɪɢʜᴛ 𝐍ᴏᴛ 𝐁ᴇ 𝐀 𝐒ᴜᴘᴇʀɢʀᴏᴜᴘ!!....")
            return
            
        except RPCError as ef:
            await msg.reply_text(text=f"𝐔ꜰꜰꜰ 𝐒ᴏᴍᴇ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀᴇᴅ, 𝐑ᴇᴘᴏʀᴛ 𝐈ᴛ 𝐔sɪɴɢ😢😣... `/bug`<b>ᴇʀʀᴏʀ:</b> <code>{ef}</code>")           
            return        
    await msg.reply_text("𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐌ᴇssᴀɢᴇ 𝐓ᴏ 𝐒ᴛᴀʀᴛ 𝐏ᴜʀɢᴇ !")
    return


@app.on_message(filters.command("del") & admin_filter)
async def del_msg(app: app, msg: Message):
    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="𝐈 𝐂ᴀɴ'ᴛ 𝐏ᴜʀɢᴇ 𝐌ᴇssᴀɢᴇs 𝐈ɴ 𝐀 𝐁ᴀsɪᴄ 𝐆ʀᴏᴜᴘ 𝐌ᴀᴋᴇ 𝐒ᴜᴘᴇʀ 𝐆ʀᴏᴜᴘ.")
        return        
    if msg.reply_to_message:
        await msg.delete()
        await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.reply_to_message.id)
    else:
        await msg.reply_text(text="𝐖ʜᴀᴛ 𝐃ᴏ 𝐘ᴏᴜ 𝐖ᴀɴᴛ 𝐓ᴏ 𝐃ᴇʟᴇᴛᴇ...𝐏ʟᴢᴢ 𝐓ᴇʟʟ...!!")
        return

