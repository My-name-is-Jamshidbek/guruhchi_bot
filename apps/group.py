from aiogram.types import Message as m
import re

from loader import bot

async def group_on_new_chat_members(message: m):
    print(1)
    try:
        chat_id = message.chat.id

        # Odam qo'shganlarni izlash
        new_members = message.new_chat_members

        for member in new_members:
            # Odam qo'shilgan odam haqida ma'lumot olish
            member_info = await bot.get_chat_member(chat_id, member.id)
            
            # Agar odam qo'shilgan foydalanuvchi boshqaruvchi (admin) bo'lmasa, uning habarini o'chiramiz
            if member_info.status != 'administrator':
                await bot.delete_message(chat_id, message.message_id)
                await bot.send_message(chat_id, f"{member.first_name} {member.last_name} ({member.username}) guruhga qo'shildi, lekin admin sifatida emas. Uning habari o'chirildi.")
    except:
        await message.answer("‼Iltimos botga to'liq adminlik bering‼")
        
        
async def group_on_left_chat_member(message: m):
    print(1)
    try:
        chat_id = message.chat.id

        # Ayrilgan odam haqida ma'lumot olish
        left_member = message.left_chat_member

        # Ayrilgan odamning habarini o'chiramiz
        await bot.delete_message(chat_id, message.message_id)
        await bot.send_message(chat_id, f"{left_member.first_name} {left_member.last_name} ({left_member.username}) guruhdan chiqdi. Uning habari o'chirildi.")
    except:
        await message.answer("‼Iltimos botga to'liq adminlik bering‼")


async def group_check_for_links(message: m):
    print(1)
    chat_id = message.chat.id
    
    caption = message.caption if message.caption else ""

    text = caption.lower() + message.text.lower()
    
    # URL larini topish
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

    if urls:
        # Agar habarda URL bor bo'lsa, unga javob yozamiz va URL ni o'chiramiz
        reply_text = "Uzr, guruhda URL (havola) qo'shishni ta'qiqlashimiz mumkin. Iltimos, URL ni olib tashlang."
        await bot.delete_message(chat_id, message.message_id)
        await bot.send_message(chat_id, reply_text)