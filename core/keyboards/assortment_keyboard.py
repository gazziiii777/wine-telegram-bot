from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок
buttons_1 = [
    [
        InlineKeyboardButton(text='◀️', callback_data='back'),
        InlineKeyboardButton(text='▶️', callback_data='forward')
    ],
    [

        InlineKeyboardButton(text='-', callback_data='delete_item'),
        InlineKeyboardButton(text='+', callback_data='add_item')
    ],
    [
        InlineKeyboardButton(text='Корзина', callback_data='add_items')
    ],
    [
        InlineKeyboardButton(text='Назад', callback_data='sparkling_wine_back')
    ],
]
buttons_2 = [
    [
        InlineKeyboardButton(text='Игристое вино', callback_data='sparkling_wine'),
    ],
    [
        InlineKeyboardButton(text='Белые вина', callback_data='delete_items'),
    ],
    [
        InlineKeyboardButton(text='Розовые вина', callback_data='add_items')
    ],
    [
        InlineKeyboardButton(text='Красные вина', callback_data='add_items')
    ],
    [
        InlineKeyboardButton(text='Крепленые вина', callback_data='add_items')
    ],
    [
        InlineKeyboardButton(text='Крепкие напитки', callback_data='add_items')
    ],
    [
        InlineKeyboardButton(text='Назад', callback_data='main_menu')
    ],
]

buttons_3 = [
    [
        InlineKeyboardButton(text='Белое', callback_data='sparkling_wine_white'),
    ],
    [
        InlineKeyboardButton(text='Розовае', callback_data='sparkling_wine_pink'),
    ],
    [
        InlineKeyboardButton(text='Назад', callback_data='assortment')
    ],

]

assortment = InlineKeyboardMarkup(inline_keyboard=buttons_2)
carousel = InlineKeyboardMarkup(inline_keyboard=buttons_1)
sparking_wine = InlineKeyboardMarkup(inline_keyboard=buttons_3)
