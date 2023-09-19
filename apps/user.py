from aiogram.types import Message as m, InputFile, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext as s

from loader import bot
from states import UserState

async def start_user(m: m):
    await m.answer("@mal_un")
