from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from core.FSM.FSM import FSMPromoCodeAdd
from core.dispatcher import dp
from core.settings import settings
from core.admin_panel.keyboard_admin import admin_keyboard


@dp.callback_query(F.data == "admin_menu")
async def admin_menu(callback: CallbackQuery):
    if callback.from_user.id == settings.bots.admin_id:
        await callback.message.edit_text(
            text="Введите название промокода который добавить в бд",
            reply_markup=admin_keyboard.keyboard
        )


@dp.callback_query(F.data == "promo_code_admin")
async def promo_code_admin(callback: CallbackQuery):
    if callback.from_user.id == settings.bots.admin_id:
        await callback.message.edit_text(
            text="Работа с просокодами",
            reply_markup=admin_keyboard.promo_keyboard
        )


@dp.callback_query(F.data == "add_promo_code")
async def add_promo_code(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id == settings.bots.admin_id:
        await callback.message.edit_text(
            text="Введите название промокода который добавить в бд",
        )
        # Устанавливаем состояние ожидания ввода имени
        await state.set_state(FSMPromoCodeAdd.promo_code_name)
