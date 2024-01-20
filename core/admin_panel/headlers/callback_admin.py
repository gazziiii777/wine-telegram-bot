from aiogram import F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from core.FSM.FSM import FSMPromoCodeAdd
from core.dispatcher import dp
from core.settings import settings


@dp.callback_query(F.data == "add_promo_code")
async def basket(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id == settings.bots.admin_id:
        await callback.message.edit_text(
            text="Введите название промокода который добавить в бд",
        )
        # Устанавливаем состояние ожидания ввода имени
        await state.set_state(FSMPromoCodeAdd.promo_code_name)


