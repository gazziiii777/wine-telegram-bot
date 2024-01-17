from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок
buttons_1 = [
    [
        InlineKeyboardButton(text='Регистрация', callback_data='register')
    ],
]

# Создаем объект инлайн-клавиатуры
register = InlineKeyboardMarkup(inline_keyboard=buttons_1)
