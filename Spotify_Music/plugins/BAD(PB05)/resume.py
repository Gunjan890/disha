from pyrogram import filters
from pyrogram.types import Message

from Spotify_Music import app
from Spotify_Music.core.call import Spotify
from Spotify_Music.utils.database import is_music_playing, music_on
from Spotify_Music.utils.decorators import AdminRightsCheck
from Spotify_Music.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["resume", "cresume"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await Spotify.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
  
