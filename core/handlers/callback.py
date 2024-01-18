from aiogram import F
from aiogram.types import CallbackQuery, Update

from core.dispatcher import dp
from core.keyboards import main_menu_keyboard, profile_keyboard
from core.db.register_user import profile_info


@dp.callback_query(F.data == "main_menu")
async def main_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f"Главное меню",
        reply_markup=main_menu_keyboard.main_menu
    )


@dp.callback_query(F.data == "profile")
async def profile(callback: CallbackQuery):
    your_profile = await profile_info(callback.from_user.id)
    await callback.message.edit_text(
        text=f"<b>Ваш профиль:</b>\n<b>ник в телеграмме:</b> @{your_profile[2]}\n<b>ФИО</b> {your_profile[3]}\n<b>номер телефона:</b> {your_profile[4]}\n<b>адрес доставки:</b> {your_profile[5]}\n<b>Почта:</b> {your_profile[6]}",
        reply_markup=profile_keyboard.profile
    )
