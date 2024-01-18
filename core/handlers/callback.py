from aiogram import F
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto

from core.dispatcher import dp, bot
from core.keyboards import main_menu_keyboard, profile_keyboard, assortment_keyboard
from core.db.register_user import profile_info
from core.db.wine import assortment_wine

wine_list = []
count = 0


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


@dp.callback_query(F.data == "assortment")
async def assortment(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f"Ассортимент",
        reply_markup=assortment_keyboard.assortment
    )


@dp.callback_query(F.data == "sparkling_wine")
async def sparking_wine(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f"sparkling_wine",
        reply_markup=assortment_keyboard.sparking_wine
    )


@dp.callback_query(F.data == "sparkling_wine_white")
async def sparkling_wine_white(callback: CallbackQuery):
    global wine_list
    global count
    count = 0
    wine_list = await assortment_wine("sparkling_wine_white")
    await callback.message.delete()
    await bot.send_photo(
        callback.from_user.id,
        photo=FSInputFile(
            path=wine_list[count][5]
        ),
        reply_markup=assortment_keyboard.carousel,
        caption=f"<b>Ca' del Cino, Vino Spumante Dolce</b>\n<b>Артикул:</b> {wine_list[0][1]}\n<b>Производитель:</b> {wine_list[0][2]}\n{f'<b>Цена:</b> <s>{wine_list[0][6]}</s>' if wine_list[0][7] != 0 else f'<b>Цена:</b> {wine_list[0][6]}'}\n{f'<b>🔥 Цена со скидкой:</b> {wine_list[0][7]} 🔥' if wine_list[0][7] != 0 else ' '}\n\n--------------------------------------\n🛒 <b>Корзина</b>\n <i>В крзине нету этого товара</i>"
    )


@dp.callback_query(F.data == "forward")
async def add_item(callback: CallbackQuery):
    global count
    cat = FSInputFile(wine_list[0][5])
    await bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            media=cat,
            caption="asdadsa"
        ),
        reply_markup=assortment_keyboard.carousel,
    )
