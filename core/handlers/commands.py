from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message

from core.FSM.FSM import FSMPromoCode
from core.dispatcher import dp
from core.keyboards import main_menu_keyboard, promo_code_keyboard
from core.db.register_user import register_user, creating_a_shopping_cart, creating_user_promo_code
from core.db.promo_code import check_promo


# Этот хэндлер будет срабатывать на команду /start вне состояний
@dp.message(Command("start"), StateFilter(default_state))
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
    await state.update_data(user_id=message.from_user.id, text=message.text)
    promo = await state.get_data()
    answer_promo = await check_promo(promo.get('user_id'), promo.get('text'))
    if answer_promo != 0:
        await message.answer(
            text=f'{answer_promo}',
            reply_markup= promo_code_keyboard.correct
        )
    else:
        await message.answer(
            text=f'Промокода <b>{promo.get('text')}</b> не не существует',
            reply_markup= promo_code_keyboard.incorrect
        )
    await state.clear()
