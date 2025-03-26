from aiogram import types, Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from filters.chat_types import ChatTypeFilter

from kbds import reply

from aiogram.utils.formatting import as_list, as_marked_section, Bold
# from aiogram.enums import ParseMode


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer('Поздравляем! Вы сделали первый шаг к здоровой жизни.',
                          reply_markup=reply.start_kb3.as_markup(
                              resize_keyboard=True,
                              input_field_placeholder='Что вас интересует?'))


@user_private_router.message(F.text.lower() == "меню")
@user_private_router.message(Command('menu'))
async def menu_cmd(message: Message):
    await message.answer("Вот меню:")


@user_private_router.message(F.text.lower() == "о магазине")
@user_private_router.message(Command('about'))
async def menu_cmd(message: Message):
    await message.answer("Подробный рассказ о себе: ")


@user_private_router.message(F.text.lower() == "варианты доставки")
@user_private_router.message(Command('delivery'))
async def delivery_cmd(message: Message):
    text = as_list(
        as_marked_section(
            Bold("Варианты доставки: "),
            "Курьер",
            "Самовывоз",
            marker='✅ '
        ),
        as_marked_section(
            Bold("Нельзя:"),
            "Почта",
            "Голуби",
            marker='🛑 '
        ),
        sep='\n-------------------------\n'
    )

    await message.answer(text.as_html(), parse_mode="HTML")


@user_private_router.message(F.text.lower() == "варианты оплаты")
@user_private_router.message(Command('payment'))
async def payment_cmd(message: Message):

    text = as_marked_section(
        Bold("Варианты оплаты: "),
        "Картой в боте",
        "При получении карта/кэш",
        marker='✅ '
    )
    await message.answer(text.as_html(), parse_mode="HTML")


@user_private_router.message(F.text.lower() == "акции")
@user_private_router.message(Command('deals'))
async def deals_cmd(message: Message):
    await message.answer('Актуальные скидки и предложения: ')


@user_private_router.message(F.text.lower() == "")
@user_private_router.message(Command('contact'))
async def contact_cmd(message: Message):
    await message.answer('Связаться с магазином: ')


@user_private_router.message(Command('cart'))
async def cart_cmd(message: Message):
    await message.answer('Ваша корзина: ')


# @user_private_router.message()
# async def echo_cmd(message: Message):
#     await message.reply('Если бы я мог болтать, то точно рассказал бы анекдот… '
#     'Но пока могу только принимать заказы! 😄 Пользуйся кнопками!')


# @user_private_router.message(F.location)
# async def get_lovation(message: Message):
#     await message.answer('Локация получена')
#     await message.answer(str(message.location))


# @user_private_router.message(F.contact)
# async def cart_contact(message: Message):
#     await message.answer('Номер получен')
#     await message.answer(str(message.contact))

