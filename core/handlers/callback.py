from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto

from core.dispatcher import dp, bot
from core.keyboards import main_menu_keyboard, profile_keyboard, assortment_keyboard, basket_keyboard
from core.db.register_user import profile_info
from core.db.wine import assortment_wine
from core.db.shoping_cart import shopping_cart_checker, shopping_add_item, shopping_delete_item, shopping_cart_get, \
    increase_count
from core.srt.generate_str import wine_info_str, placing_an_order, shopping_cart_basket_str
from core.FSM.FSM import FSMPromoCode

wine_list = []
shopping_cart = []
wine_list_info = []
shopping_cart_basket = []
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


@dp.callback_query(F.data == "assortment_back")
async def assortment(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
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
@dp.callback_query(F.data == "sparkling_wine_pink")
@dp.callback_query(F.data == "white_wine")
async def sparkling_wine_white(callback: CallbackQuery):
    global wine_list
    global count
    global shopping_cart
    global wine_list_info
    wine_list = await assortment_wine(callback.data)
    if len(wine_list) != 0:
        count = 0
        wine_list_info = await assortment_wine(callback.data + '_info')
        shopping_cart = await shopping_cart_checker(callback.from_user.id, wine_list[count][1])
        wine_str = await wine_info_str(wine_list, wine_list_info, shopping_cart, count)
        await callback.message.delete()
        await bot.send_photo(
            callback.from_user.id,
            photo=FSInputFile(
                path=wine_list[count][5]
            ),
            reply_markup=assortment_keyboard.carousel,
            caption=wine_str
        )
    else:
        await callback.answer(
            text="Нету",
            show_alert=True
        )


@dp.callback_query(F.data == "forward")
@dp.callback_query(F.data == "forward_basket")
async def forward(callback: CallbackQuery):
    global count
    if callback.data == "forward":
        global wine_list
        global shopping_cart
        if count != len(wine_list) - 1:
            await callback.answer()
            count += 1
            shopping_cart = await shopping_cart_checker(callback.from_user.id, wine_list[count][1])
            wine_str = await wine_info_str(wine_list, wine_list_info, shopping_cart, count)
            await bot.edit_message_media(
                chat_id=callback.message.chat.id,
                message_id=callback.message.message_id,
                media=InputMediaPhoto(
                    media=FSInputFile(wine_list[count][5]),
                    caption=wine_str
                ),
                reply_markup=assortment_keyboard.carousel,
            )
        else:
            await callback.answer(
                text="asasdasdsadadsda",
                show_alert=True
            )
    if callback.data == "forward_basket":
        global shopping_cart_basket
        if count != len(shopping_cart_basket) - 1:
            await callback.answer()
            count += 1
            basket_str = await shopping_cart_basket_str(shopping_cart_basket, count)
            await bot.edit_message_media(
                chat_id=callback.message.chat.id,
                message_id=callback.message.message_id,
                media=InputMediaPhoto(
                    media=FSInputFile(f"core/db/data_bases/images/{shopping_cart_basket[count][2]}.jpg"),
                    caption=basket_str
                ),
                reply_markup=basket_keyboard.basket_carousel,
            )
        else:
            await callback.answer(
                text="asasdasdsadadsda",
                show_alert=True
            )


@dp.callback_query(F.data == "back")
@dp.callback_query(F.data == "back_basket")
async def back(callback: CallbackQuery):
    global count
    global shopping_cart
    if callback.data == "back":
        if count != 0:
            count -= 1
            await callback.answer()
            shopping_cart = await shopping_cart_checker(callback.from_user.id, wine_list[count][1])
            wine_str = await wine_info_str(wine_list, wine_list_info, shopping_cart, count)
            await bot.edit_message_media(
                chat_id=callback.message.chat.id,
                message_id=callback.message.message_id,
                media=InputMediaPhoto(
                    media=FSInputFile(wine_list[count][5]),
                    caption=wine_str
                ),
                reply_markup=assortment_keyboard.carousel,
            )
        else:
            await callback.answer(
                text="asdadsda",
                show_alert=True
            )
    if callback.data == "back_basket":
        global shopping_cart_basket
        if count != 0:
            await callback.answer()
            count -= 1
            basket_str = await shopping_cart_basket_str(shopping_cart_basket, count)
            await bot.edit_message_media(
                chat_id=callback.message.chat.id,
                message_id=callback.message.message_id,
                media=InputMediaPhoto(
                    media=FSInputFile(f"core/db/data_bases/images/{shopping_cart_basket[count][2]}.jpg"),
                    caption=basket_str
                ),
                reply_markup=basket_keyboard.basket_carousel,
            )
        else:
            await callback.answer(
                text="asasdasdsadadsda",
                show_alert=True
            )


@dp.callback_query(F.data == "add_item")
@dp.callback_query(F.data == "add_item_basket")
async def add_item(callback: CallbackQuery):
    global wine_list
    global shopping_cart_basket
    if callback.data == "add_item":
        await callback.answer()
        shopping_cart_add = await shopping_add_item(callback.from_user.id, wine_list[count][1], wine_list[count][3], *[
            wine_list[count][-1] if wine_list[count][-1] != 0 else wine_list[count][-2]])
        wine_str = await wine_info_str(wine_list, wine_list_info, shopping_cart_add, count)
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=FSInputFile(wine_list[count][5]),
                caption=wine_str
            ),
            reply_markup=assortment_keyboard.carousel,
        )
    if callback.data == 'add_item_basket':
        print(shopping_cart_basket[count][-2])
        await callback.answer()
        await increase_count(callback.from_user.id, shopping_cart_basket[count][2])
        shopping_cart_basket = await shopping_cart_get(callback.from_user.id)
        print(shopping_cart_basket[count][-2])
        basket_str = await shopping_cart_basket_str(shopping_cart_basket, count)
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=FSInputFile(f"core/db/data_bases/images/{shopping_cart_basket[count][2]}.jpg"),
                caption=basket_str
            ),
            reply_markup=basket_keyboard.basket_carousel,
        )


@dp.callback_query(F.data == "delete_item")
@dp.callback_query(F.data == "delete_item_basket")
async def delete_item(callback: CallbackQuery):
    global wine_list
    global count
    global shopping_cart_basket
    if callback.data == "delete_item":
        await callback.answer()
        shopping_cart_delete = await shopping_delete_item(callback.from_user.id, wine_list[count][1])
        wine_str = await wine_info_str(wine_list, wine_list_info, shopping_cart_delete, count)
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=FSInputFile(wine_list[count][5]),
                caption=wine_str
            ),
            reply_markup=assortment_keyboard.carousel,
        )
    if callback.data == 'delete_item_basket':
        shopping_cart_delete = await shopping_delete_item(callback.from_user.id, shopping_cart_basket[count][2])
        if shopping_cart_delete == 0:
            count -= 1
            await callback.answer(
                text="Удален"
            )
        await callback.answer()
        shopping_cart_basket = await shopping_cart_get(callback.from_user.id)
        basket_str = await shopping_cart_basket_str(shopping_cart_basket, count)
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=FSInputFile(f"core/db/data_bases/images/{shopping_cart_basket[count][2]}.jpg"),
                caption=basket_str
            ),
            reply_markup=basket_keyboard.basket_carousel,
        )


@dp.callback_query(F.data == "sparkling_wine_back")
async def sparkling_wine_back(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        text=f"sparkling_wine",
        reply_markup=assortment_keyboard.sparking_wine
    )


@dp.callback_query(F.data == "basket")
async def basket(callback: CallbackQuery):
    global count
    global shopping_cart_basket
    shopping_cart_basket = await shopping_cart_get(callback.from_user.id)
    if len(shopping_cart_basket) != 0:
        await callback.message.delete()
        count = 0
        basket_str = await shopping_cart_basket_str(shopping_cart_basket, count)
        await bot.send_photo(
            callback.from_user.id,
            photo=FSInputFile(
                path=f"core/db/data_bases/images/{shopping_cart_basket[count][2]}.jpg",
            ),
            caption=basket_str,
            reply_markup=basket_keyboard.basket_carousel,
        )
    else:
        await callback.answer(
            text="Корзина пуста",
            show_alert=True
        )


@dp.callback_query(F.data == "сheckout")
async def сheckout(callback: CallbackQuery):
    await callback.message.delete()
    shopping = await shopping_cart_get(callback.from_user.id)
    your_profile = await profile_info(callback.from_user.id)
    shopping_str = await placing_an_order(shopping, your_profile)
    await callback.message.answer(
        text=f"{shopping_str}",
        reply_markup=assortment_keyboard.sparking_wine
    )


@dp.callback_query(F.data == "promo_code")
async def promo_code(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Введите промкод",
    )
    # Устанавливаем состояние ожидания ввода имени
    await state.set_state(FSMPromoCode.promo_code)
