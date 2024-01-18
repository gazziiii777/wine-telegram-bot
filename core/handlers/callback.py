from aiogram import F
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto

from core.dispatcher import dp, bot
from core.keyboards import main_menu_keyboard, profile_keyboard, assortment_keyboard
from core.db.register_user import profile_info
from core.db.wine import assortment_wine
from core.db.shoping_cart import shopping_cart_checker, shopping_add_item,shopping_delete_item

wine_list = []
shopping_cart = []
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
    global shopping_cart
    count = 0
    wine_list = await assortment_wine("sparkling_wine_white")
    shopping_cart = await shopping_cart_checker(callback.from_user.id, wine_list[count][1])
    await callback.message.delete()
    await bot.send_photo(
        callback.from_user.id,
        photo=FSInputFile(
            path=wine_list[count][5]
        ),
        reply_markup=assortment_keyboard.carousel,
        caption=f"<b>{wine_list[count][3]}</b>\n<b>Артикул:</b> {wine_list[count][1]}\n<b>Производитель:</b> {wine_list[count][2]}\n{f'<b>Цена:</b> <s>{wine_list[count][6]}</s>' if wine_list[count][7] != 0 else f'<b>Цена:</b> {wine_list[count][6]}'}\n{f'<b>🔥 Цена со скидкой:</b> {wine_list[count][7]} 🔥' if wine_list[count][7] != 0 else ''}\n--------------------------------------\n🛒 <b>Корзина</b>\n <i>{f"В корзине {shopping_cart} шт.\n На сумму: {shopping_cart*wine_list[count][7] if wine_list[count][7] != 0 else shopping_cart*wine_list[count][6]}" if shopping_cart != 0 else "В крзине нету этого товара"}</i>" м 
    )


@dp.callback_query(F.data == "forward")
async def forward(callback: CallbackQuery):
    global count
    global wine_list
    global shopping_cart
    if count != len(wine_list) - 1:
        await callback.answer()
        count += 1
        shopping_cart = await shopping_cart_checker(callback.from_user.id, wine_list[count][1])
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=FSInputFile(wine_list[count][5]),
                caption=f"<b>{wine_list[count][3]}</b>\n<b>Артикул:</b> {wine_list[count][1]}\n<b>Производитель:</b> {wine_list[count][2]}\n{f'<b>Цена:</b> <s>{wine_list[count][6]}</s>' if wine_list[count][7] != 0 else f'<b>Цена:</b> {wine_list[count][6]}'}\n{f'<b>🔥 Цена со скидкой:</b> {wine_list[count][7]} 🔥' if wine_list[count][7] != 0 else ''}\n--------------------------------------\n🛒 <b>Корзина</b>\n <i>{f"В корзине {shopping_cart} шт.\n На сумму: {shopping_cart*wine_list[count][7] if wine_list[count][7] != 0 else shopping_cart*wine_list[count][6]}" if shopping_cart != 0 else "В крзине нету этого товара"}</i>"
            ),
            reply_markup=assortment_keyboard.carousel,
        )
    else:
        await callback.answer(
            text="asasdasdsadadsda",
            show_alert=True
        )


@dp.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    global count
    global shopping_cart
    if count != 0:
        count -= 1
        await callback.answer()
        shopping_cart = await shopping_cart_checker(callback.from_user.id, wine_list[count][1])
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=FSInputFile(wine_list[count][5]),
                caption=f"<b>{wine_list[count][3]}</b>\n<b>Артикул:</b> {wine_list[count][1]}\n<b>Производитель:</b> {wine_list[count][2]}\n{f'<b>Цена:</b> <s>{wine_list[count][6]}</s>' if wine_list[count][7] != 0 else f'<b>Цена:</b> {wine_list[count][6]}'}\n{f'<b>🔥 Цена со скидкой:</b> {wine_list[count][7]} 🔥' if wine_list[count][7] != 0 else ''}\n--------------------------------------\n🛒 <b>Корзина</b>\n <i>{f"В корзине {shopping_cart} шт.\n На сумму: {shopping_cart*wine_list[count][7] if wine_list[count][7] != 0 else shopping_cart*wine_list[count][6]}" if shopping_cart != 0 else "В крзине нету этого товара"}</i>"
            ),
            reply_markup=assortment_keyboard.carousel,
        )
    else:
        await callback.answer(
            text="asdadsda",
            show_alert=True
        )


@dp.callback_query(F.data == "add_item")
async def add_item(callback: CallbackQuery):
    global wine_list
    await callback.answer()
    shopping_cart_add = await shopping_add_item(callback.from_user.id, wine_list[count][1], wine_list[count][3])
    await bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            media=FSInputFile(wine_list[count][5]),
            caption=f"<b>{wine_list[count][3]}</b>\n<b>Артикул:</b> {wine_list[count][1]}\n<b>Производитель:</b> {wine_list[count][2]}\n{f'<b>Цена:</b> <s>{wine_list[count][6]}</s>' if wine_list[count][7] != 0 else f'<b>Цена:</b> {wine_list[count][6]}'}\n{f'<b>🔥 Цена со скидкой:</b> {wine_list[count][7]} 🔥' if wine_list[count][7] != 0 else ''}\n--------------------------------------\n🛒 <b>Корзина</b>\n <i>{f"В корзине {shopping_cart_add} шт.\n На сумму: {shopping_cart_add*wine_list[count][7] if wine_list[count][7] != 0 else shopping_cart_add*wine_list[count][6]}" if shopping_cart_add != 0 else "В крзине нету этого товара"}</i>"
        ),
        reply_markup=assortment_keyboard.carousel,
    )


@dp.callback_query(F.data == "delete_item")
async def delete_item(callback: CallbackQuery):
    global wine_list
    global count
    await callback.answer()
    shopping_cart_delete = await shopping_delete_item(callback.from_user.id, wine_list[count][1], wine_list[count][3])
    await bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            media=FSInputFile(wine_list[count][5]),
            caption=f"<b>{wine_list[count][3]}</b>\n<b>Артикул:</b> {wine_list[count][1]}\n<b>Производитель:</b> {wine_list[count][2]}\n{f'<b>Цена:</b> <s>{wine_list[count][6]}</s>' if wine_list[count][7] != 0 else f'<b>Цена:</b> {wine_list[count][6]}'}\n{f'<b>🔥 Цена со скидкой:</b> {wine_list[count][7]} 🔥' if wine_list[count][7] != 0 else ''}\n--------------------------------------\n🛒 <b>Корзина</b>\n <i>{f"В корзине {shopping_cart_delete} шт.\n На сумму: {shopping_cart_delete*wine_list[count][7] if wine_list[count][7] != 0 else shopping_cart_delete*wine_list[count][6]}" if shopping_cart_delete != 0 else "В крзине нету этого товара"}</i>"
        ),
        reply_markup=assortment_keyboard.carousel,
    )
