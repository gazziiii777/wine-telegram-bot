from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок
buttons_1 = [
    [
        InlineKeyboardButton(text='Мой профиль', callback_data='profile')
    ],
    [
        InlineKeyboardButton(text='Ассортимент', callback_data='assortment')
    ],
    [
        InlineKeyboardButton(text='Акции', callback_data='sales')
    ],
    [
        InlineKeyboardButton(text='Корзина', callback_data='basket')
    ],
    [
        InlineKeyboardButton(text='Промокод', callback_data='promo_code')
    ],
    [
        InlineKeyboardButton(text='FAQ', callback_data='FAQ'),
        InlineKeyboardButton(text='Написать сомелье', callback_data='write_sommelier')
    ],
]
# Создаем объект инлайн-клавиатуры
main_menu = InlineKeyboardMarkup(inline_keyboard=buttons_1)
