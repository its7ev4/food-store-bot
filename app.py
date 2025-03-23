import asyncio 
import os

from aiogram import Bot, Dispatcher

from dotenv import find_dotenv, load_dotenv
from handlers.user_private import user_private_router


load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


dp.include_router(user_private_router)

ALLOWED_UPDATES = ['message, edited_message']


async def main():
    await bot.delete_webhook(drop_pending_updates=True)  # бесконечно проверяем обнолвения нашего бота
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)  


asyncio.run(main())