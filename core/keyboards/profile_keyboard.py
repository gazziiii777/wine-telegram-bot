from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок
buttons_1 = [
    [
        InlineKeyboardButton(text='Редактирование данных', callback_data='edit_profile')
    ],
[
        InlineKeyboardButton(text='Назад', callback_data='main_menu')
    ],
]

# Создаем объект инлайн-клавиатуры
profile = InlineKeyboardMarkup(inline_keyboard=buttons_1)
