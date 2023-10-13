#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>✰ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n✰ Language : <code>Python3</code>\n✰ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n✰ Source Code : <a href='https://t.me/+S-Y0_x6tMA81ODM1'>Click here</a>\n✰ Channel : <a href='https://t.me/+g4T8qKy5Gow3MjVl'>Click here</a>\n✰ Support Group : <a href='https://t.me/mallumovies_1'>Click here</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("𝐂𝐋𝐎𝐒𝐄", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
