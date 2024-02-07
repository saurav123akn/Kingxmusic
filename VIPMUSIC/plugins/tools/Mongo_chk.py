from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
import re
from VIPMUSIC import app


mongo_url_pattern = re.compile(r'mongodb(?:\+srv)?:\/\/[^\s]+')


@app.on_message(filters.command("mongochk"))
async def mongo_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply("𝐏ʟᴢᴢ 𝐄ɴᴛᴇʀ 𝐘ᴏᴜʀ 𝐌ɴɢᴏ ᴅʙ 𝐔ʀʟ 𝐀ꜰᴛᴇʀ 𝐓ʜʀ 𝐂ᴏᴍᴍᴀɴᴅ. Example: `/mongochk your_mongodb_url`")
        return

    mongo_url = message.command[1]
    if re.match(mongo_url_pattern, mongo_url):
        try:
            # Attempt to connect to the MongoDB instance
            client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
            client.server_info()  # Will cause an exception if connection fails
            await message.reply("𝐌𝗼𝗻𝗴𝗼𝗗𝗕 𝐔𝗥𝗟 𝐈𝘀 𝐕𝗮𝗹𝗶𝗱 𝐀𝗻𝗱 𝐂𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝐒𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹✅")
        except Exception as e:
            await message.reply(f"𝐅ᴀɪʟᴇᴅ 𝐓ᴏ 𝐂ᴏɴɴᴇᴄᴛ 𝐓ᴏ 𝐌ᴏɴɢᴏᴅʙ: {e}")
    else:
        await message.reply("𝐈ɴᴠᴀʟɪᴅ 𝐌ɴɢᴏᴅʙ 𝐔ʀʟ 𝐅ᴏᴛᴍᴀᴛ😖")
