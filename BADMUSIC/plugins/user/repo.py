import asyncio

from BADMUSIC import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_message(filters.command(["repo"], prefixes=["."]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/bda2c51bd00c8f4710b04.mp4",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention} [☆ ʀᴇᴘᴏ 💗](https://t.me/CENSORED_POLITICSSS)",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="☆ ᴏᴡɴᴇʀ 💗 ", url=f"https://t.me/CENSORED_POLITICSSS"
            ),
            InlineKeyboardButton(
                text="☆ ɢʀᴏᴜᴘ 💗", url=f"https://t.me/TSERIESSUPPORTCHAT"
            ),
        ],
          [
            InlineKeyboardButton(
                text="☆ ᴄʜᴀɴɴᴇʟ 💗 ", url=f"https://t.me/TSERIESUPDATESS"
            ),
            InlineKeyboardButton(
                text="☆ ʀᴇᴘᴏ 💗", url=f"https://t.me/CENSORED_POLITICSSS"
            ),
        ],
                [
                    InlineKeyboardButton(
                        "✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ],
            ]
        )
    )
  
