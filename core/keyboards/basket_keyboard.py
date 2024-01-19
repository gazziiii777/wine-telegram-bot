from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buttons_1 = [
    [
        InlineKeyboardButton(text='Оформить заказ', callback_data='сheckout')
    ],
    [
        InlineKeyboardButton(text='Изменить', callback_data='pass'),
    ],
    [
        InlineKeyboardButton(text='Ассортимент', callback_data='assortment')
    ],
]

# Создаем объекты инлайн-кнопок
buttons_2 = [
    [
        InlineKeyboardButton(text='◀️', callback_data='back_basket'),
        InlineKeyboardButton(text='▶️', callback_data='forward_basket')
    ],
    [

        InlineKeyboardButton(text='-', callback_data='delete_item_basket'),
        InlineKeyboardButton(text='+', callback_data='add_item_basket')
    ],
    [
        InlineKeyboardButton(text='Оформить заказ', callback_data='сheckout')
    ],
    [
        InlineKeyboardButton(text='Назад', callback_data='assortment_back')
    ],
]

basket = InlineKeyboardMarkup(inline_keyboard=buttons_1)
basket_carousel = InlineKeyboardMarkup(inline_keyboard=buttons_2)
