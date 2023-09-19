from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import executor
from aiogram.types import ContentType as ct
import logging
import re

# from database.database import get_all_premium_audiobook_address, get_all_premium_book_address, get_user_premium_books_address, get_user_premium_audiobooks_address
from config import ADMIN_ID, ADMIN_IDS, TOKEN

# Bot tokenini quyidagi o'zgaruvchiga o'zgartiring
TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(content_types=[ct.NEW_CHAT_MEMBERS, ct.LEFT_CHAT_MEMBER])
async def usermanager(message: types.Message):
    await message.delete()    


@dp.message_handler(content_types=[ct.TEXT])
async def contentmanager(message: types.Message):
    chat_id = message.chat.id
    
    caption = message.caption if message.caption else ""

    text = caption.lower() + message.text.lower()
    
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

    if urls:
        await bot.delete_message(chat_id, message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)