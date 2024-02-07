from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="֎𝐇ᴇʟᴘ֍", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="֎𝐒ᴜᴘᴘᴏʀᴛ֍", url=f"https://t.me/TEAM_CDX"
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="༒𝐊𝐈𝐍𝐆༒", url=f"https://t.me/King_oF_Heartx),
            InlineKeyboardButton(text="༒𝐐𝐔𝐄𝐄𝐍༒", url=f"https://t.me/QUEENN_OF_HEART),
        ],
        [
            InlineKeyboardButton(text="֎𝐇ᴇʟᴘ֍", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="֎𝐒ᴜᴘᴘᴏʀᴛ֍", url=f"https://t.me/TEAM_CDX"),
        ],
    ]
    return buttons
