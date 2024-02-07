from pyrogram import filters
from pyrogram.types import Message

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>𝐄xᴀᴍᴘʟᴇ :</b>\n\n/𝐀utoend [𝐄ɴᴀʙʟᴇ | 𝐃ɪsᴀʙʟᴇ]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "» 𝐀ᴜᴛᴏ 𝐄ɴᴅ 𝐒ᴛʀᴇᴀᴍ 𝐄ɴᴀʙʟᴇᴅ.\n\n𝐀ssɪsᴛᴀɴᴛ 𝐖ɪʟʟ 𝐀ᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ 𝐋ᴇᴀᴠᴇ 𝐓ʜᴇ 𝐕ɪᴅᴇᴏᴄʜᴀᴛ 𝐀ғᴛᴇʀ 𝐅ᴇᴡ 𝐌ɪɴs 𝐄ʜᴇɴ 𝐍ᴏ 𝐎ɴᴇ 𝐈s 𝐋ɪsᴛᴇɴɪɴɢ."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("» 𝐀ᴜᴛᴏ 𝐄ɴᴅ 𝐒ᴛʀᴇᴀᴍ 𝐃ɪsᴀʙʟᴇᴅ.🌟💥")
    else:
        await message.reply_text(usage)
