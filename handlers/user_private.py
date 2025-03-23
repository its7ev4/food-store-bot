from aiogram import types, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart



user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer('Поздравляем! Вы сделали первый шаг к здоровой жизни.')


@user_private_router.message(Command('menu'))
async def menu_cmd(message: Message):
    await message.answer("Вот меню: ")

