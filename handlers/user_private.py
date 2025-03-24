from aiogram import types, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from filters.chat_types import ChatTypeFilter


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer('Поздравляем! Вы сделали первый шаг к здоровой жизни.')


@user_private_router.message(Command('menu'))
async def menu_cmd(message: Message):
    await message.answer("Вот меню: ")


@user_private_router.message(Command('about'))
async def menu_cmd(message: Message):
    await message.answer("Подробный рассказ о себе: ")


@user_private_router.message(Command('cart'))
async def cart_cmd(message: Message):
    await message.answer('Ваша корзина: ')


@user_private_router.message(Command('delivery'))
async def delivery_cmd(message: Message):
    await message.answer('ИНформация о доставке: ')


@user_private_router.message(Command('payment'))
async def payment_cmd(message: Message):
    await message.answer('Информация об оплате: ')


@user_private_router.message(Command('deals'))
async def deals_cmd(message: Message):
    await message.answer('Актуальные скидки и предложения: ')


@user_private_router.message(Command('contact'))
async def contact_cmd(message: Message):
    await message.answer('Связаться с магазином: ')


@user_private_router.message()
async def echo_cmd(message: Message):
    await message.reply('Если бы я мог болтать, то точно рассказал бы анекдот… '
    'Но пока могу только принимать заказы! 😄 Пользуйся кнопками!')