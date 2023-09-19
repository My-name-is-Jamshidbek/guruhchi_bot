from aiogram import executor
from aiogram.dispatcher.filters import Text
from app import dp

# Bu dastur faqat o'zgartirilgan tahrirlovchilar (asosiy komponentlar) bilan ishlaydi
executor.start_polling(dp, skip_updates=True)