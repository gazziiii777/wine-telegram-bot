from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок
buttons_1 = [
    [
        InlineKeyboardButton(text='Рассылка', callback_data='pass'),
    ],
    [
        InlineKeyboardButton(text='Редактирование товаров', callback_data='pass')
    ],
    [
        InlineKeyboardButton(text='Редактирование промокодов', callback_data='promo_code_admin')
    ],
]

buttons_2 = [
    [
        InlineKeyboardButton(text='Добавить промокод', callback_data='add_promo_code'),
    ],
    [
        InlineKeyboardButton(text='Удалить промокод', callback_data='delete_promo_code')
    ],
    [
        InlineKeyboardButton(text='Назад', callback_data='admin_menu')
    ],
]

buttons_3 = [
    [
        InlineKeyboardButton(text='Добавить другой промокод', callback_data='add_promo_code'),
    ],
    [
        InlineKeyboardButton(text='Назад', callback_data='admin_menu')
    ],
]

keyboard = InlineKeyboardMarkup(inline_keyboard=buttons_1)
promo_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons_2)
promo_add_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons_3)
