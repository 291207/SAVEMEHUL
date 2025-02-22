from pyrogram import filters
from devgagan import app
from devgagan.core import script
from devgagan.core.func import subscribe
from config import OWNER_ID ,SUPPORT, CHANNEL
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton 

# ------------------- Start-Buttons ------------------- #

buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Join Channel", url=f"https://t.me/{CHANNEL}")],
        [InlineKeyboardButton("Buy Premium", url=f"https://t.me/{SUPPORT}")]
    ]
)

@app.on_message(filters.command("start"))
async def start(_, message):
    join = await subscribe(_, message)
    if join == 1:
        return
    await message.reply_photo(photo="https://telegra.ph/file/fea4ba680cebc4ac23b78.mp4",
                              caption=script.START_TXT.format(message.from_user.mention), 
                              reply_markup=buttons)
