from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок
buttons_1 = [
    [
        InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
    ],
    [
        InlineKeyboardButton(text='Корзина', callback_data='basket')
    ],
]

buttons_2 = [
    [
        InlineKeyboardButton(text='Ввести промокод еще раз', callback_data='promo_code')
    ],
    [
        InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
    ],
    [
        InlineKeyboardButton(text='Корзина', callback_data='basket')
    ],
]
# Создаем объект инлайн-клавиатуры
correct = InlineKeyboardMarkup(inline_keyboard=buttons_1)
incorrect = InlineKeyboardMarkup(inline_keyboard=buttons_2)
