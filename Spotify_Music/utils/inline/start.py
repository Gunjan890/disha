from pyrogram.types import InlineKeyboardButton

import config
from Spotify_Music import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="🌹 ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ 🌹", url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="🌹 ʜᴇʟᴘ 🌹", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text=" sᴇᴛ ", callback_data="settings_helper"
            ),
        ],
      [
             InlineKeyboardButton(text="🌹 ᴄʟᴏsᴇ 🌹", callback_data="close"),
    ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="🌹 ʜᴇʟᴘ 🌹", callback_data="settings_back_helper"),
            InlineKeyboardButton(text=" ❤️‍🔥 ᴋɪɴɢ 🌹", url=f"https://t.me/apna_gunjan"),
            ],
                    [
                    InlineKeyboardButton(text="🌹 ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ 🌹", url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="🌹 Group 🌹", url=f"https://t.me/+8huyLCAdA6o0OWRl"),
             InlineKeyboardButton(text="🌹 ᴄʟᴏsᴇ 🌹", callback_data="close"),
    ],
    ]
    return buttons
    
    
