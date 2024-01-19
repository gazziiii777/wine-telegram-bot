from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message

from core.FSM.FSM import FSMPromoCode
from core.dispatcher import dp
from core.keyboards import main_menu_keyboard
from core.db.register_user import register_user, creating_a_shopping_cart, creating_user_promo_code


# Этот хэндлер будет срабатывать на команду /start вне состояний
@dp.message(Command("support"), StateFilter(default_state))
async def cmd_main_menu(message: Message):
    await register_user(message.from_user.id, message.from_user.username)
    await creating_a_shopping_cart(str(message.from_user.id))
    await creating_user_promo_code(message.from_user.id)
    await message.answer(
        text="кайфарик марик тут типо тоже текст",
        reply_markup=main_menu_keyboard.main_menu
    )


# Этот хэндлер будет срабатывать, если введено корректное имя
# и переводить в состояние ожидания ввода возраста
@dp.message(StateFilter(FSMPromoCode.promo_code))
async def process_question_to_support(message: Message, state: FSMContext):
    # Cохраняем введенное имя в хранилище по ключу "name"
    await state.update_data(promo_code = True)
    promo = await state.get_data()
    await message.answer(
        text=f'<b>Пожалуйста, проверьте свое письмо перед отправкой в техподдержку: {promo.get('promo_code')}</b>',
    )
    await state.clear()