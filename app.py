import asyncio 
import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import BotCommandScopeAllPrivateChats

from dotenv import find_dotenv, load_dotenv

from handlers.user_private import user_private_router
from common.bot_cmds_list import private
from handlers.user_group import user_group_router
from handlers.admin_private import admin_router


load_dotenv(find_dotenv())

ALLOWED_UPDATES = ['message, edited_message']



bot = Bot(token=os.getenv('TOKEN'))
bot.my_admins_list = []

dp = Dispatcher()


dp.include_routers(user_private_router, user_group_router, admin_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)  # бесконечно проверяем обнолвения нашего бота
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    #  await bot.delete_my_commands(scope=BotCommandScopeAllPrivateChats())  для удаления синей кнопки "меню"
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)  


asyncio.run(main())