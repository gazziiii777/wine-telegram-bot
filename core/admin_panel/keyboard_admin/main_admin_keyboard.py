from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок
buttons_1 = [
    [
        InlineKeyboardButton(text='Рассылка', callback_data='pass'),
    ],
    [

        InlineKeyboardButton(text='Добавить товар', callback_data='pass')
    ],
    [
        InlineKeyboardButton(text='Добавить промокод', callback_data='add_promo_code')
    ],
]

keyboard = InlineKeyboardMarkup(inline_keyboard=buttons_1)