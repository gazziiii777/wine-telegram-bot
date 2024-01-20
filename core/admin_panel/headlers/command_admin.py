# Этот хэндлер будет срабатывать на команду /start вне состояний
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message

from core.FSM.FSM import FSMPromoCodeAdd
from core.dispatcher import dp
from core.admin_panel.keyboard_admin import admin_keyboard
from core.db.promo_code import add_new_promo
from core.admin_panel.headlers import callback_admin


@dp.message(Command("admin"), StateFilter(default_state))
async def cmd_main_menu(message: Message):
    await message.answer(
        text="Панель Администратора",
        reply_markup=admin_keyboard.keyboard
    )


@dp.message(StateFilter(FSMPromoCodeAdd.promo_code_name))
async def process_question_to_support(message: Message, state: FSMContext):
    # Cохраняем введенное имя в хранилище по ключу "name"
    await state.update_data(promo_code_name=message.text)
    await message.answer(
        text='Теперь введите значение скидки для промокода например, если скидка 20 % введите 0.2 (обязательно точка), если 15 %, то 0.15')
    await state.set_state(FSMPromoCodeAdd.promo_code_value)


@dp.message(StateFilter(FSMPromoCodeAdd.promo_code_value))
async def process_question_to_support(message: Message, state: FSMContext):
    # Cохраняем введенное имя в хранилище по ключу "name"
    await state.update_data(promo_code_value=message.text)
    answer = await state.get_data()
    promo_add = await add_new_promo(answer.get('promo_code_name'), answer.get('promo_code_value'))
    print(promo_add)
    if promo_add == 0:
        await message.answer(
            text=f"Промокод {answer.get('promo_code_name')} уже есть в таблицеы",
            reply_markup=admin_keyboard.promo_add_keyboard

        )
    else:
        await message.answer(
            text=promo_add,
            reply_markup=admin_keyboard.promo_add_keyboard
        )
    await state.clear()
