import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

from config import TOKEN

# Bot tokenini o'zgartiring
API_TOKEN = TOKEN

# Botni yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
