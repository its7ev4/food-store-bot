from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder 
from aiogram.types import KeyboardButtonPollType


ADMIN_KB = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Добавить товар'),
            KeyboardButton(text='Изменить товар'),
            
        ],

        [
            KeyboardButton(text="Удалить товар")
        ],

        [   
            KeyboardButton(text="Я так просто посмотреть зашёл"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Жмякай"
)


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            KeyboardButton(text='О магазине'),
            KeyboardButton(text="Варианты оплаты"),
        ],

        [   KeyboardButton(text="Варианты доставки"),
            KeyboardButton(text="Акции")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Жмякай"
)


# del_kbd = ReplyKeyboardRemove() для удаления кнопок


start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text='Меню'),
    KeyboardButton(text='О магазине'),
    KeyboardButton(text="Варианты оплаты"),
    KeyboardButton(text="Варианты доставки"),
    KeyboardButton(text="Акции")      
)
start_kb2.adjust(3, 2)


start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.row(KeyboardButton(text='Оставить отзыв')) # добавление новым рядом



test_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Создать опрос', request_poll=KeyboardButtonPollType()),
        ],
        [
            KeyboardButton(text='Отправить номер 📞', request_contact=True),
            KeyboardButton(text="Отпраивть лоакцию 🗺️", request_location=True)
        ]
    ]
)


