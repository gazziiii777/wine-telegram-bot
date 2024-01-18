from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message

from core.dispatcher import dp
from core.keyboards import main_menu_keyboard
from core.db.register_user import register_user, creating_a_shopping_cart


# Этот хэндлер будет срабатывать на команду /start вне состояний
@dp.message(Command("start"), StateFilter(default_state))
async def cmd_main_menu(message: Message):
    await register_user(message.from_user.id, message.from_user.username)
    await creating_a_shopping_cart(str(message.from_user.id))
    await message.answer(
        text="кайфарик марик тут типо тоже текст",
        reply_markup=main_menu_keyboard.main_menu
    )
