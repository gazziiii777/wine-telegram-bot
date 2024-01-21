from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message

from core.FSM.FSM import FSMPromoCode, FSMUserRegister
from core.dispatcher import dp
from core.keyboards import main_menu_keyboard, promo_code_keyboard, profile_keyboard
from core.db.register_user import register_user, creating_a_shopping_cart, creating_user_promo_code, new_profile_info, \
    profile_info
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
            reply_markup=promo_code_keyboard.correct
        )
    else:
        await message.answer(
            text=f'Промокода <b>{promo.get('text')}</b> не не существует',
            reply_markup=promo_code_keyboard.incorrect
        )
    await state.clear()


@dp.message(StateFilter(FSMUserRegister.telegram_user_name))
async def process_question_to_support(message: Message, state: FSMContext):
    username = message.text.replace("@", "")
    await state.update_data(username=username)
    await message.answer(
        text='Введите ФИО',
    )
    await state.set_state(FSMUserRegister.full_name)


@dp.message(StateFilter(FSMUserRegister.full_name))
async def process_question_to_support(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer(
        text='Введите номер телефона',
    )
    await state.set_state(FSMUserRegister.phone_number)


@dp.message(StateFilter(FSMUserRegister.phone_number))
async def process_question_to_support(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await message.answer(
        text='Введите адрес доставки',
    )
    await state.set_state(FSMUserRegister.delivery_address)


@dp.message(StateFilter(FSMUserRegister.delivery_address))
async def process_question_to_support(message: Message, state: FSMContext):
    await state.update_data(delivery_address=message.text)
    await message.answer(
        text='Введите почту:',
    )
    await state.set_state(FSMUserRegister.mail)


@dp.message(StateFilter(FSMUserRegister.mail))
async def process_question_to_support(message: Message, state: FSMContext):
    await state.update_data(mail=message.text)
    profile_info_new = await state.get_data()
    your_profile = await profile_info(message.from_user.id)
    await new_profile_info(message.from_user.id, profile_info_new.get('username'), profile_info_new.get('full_name'), profile_info_new.get('phone_number'),profile_info_new.get('delivery_address'), profile_info_new.get('mail'))
    await message.answer(
        text=f"<b>Ваш профиль:</b>\n<b>ник в телеграмме:</b> @{your_profile[2]}\n<b>ФИО</b> {your_profile[3]}\n<b>номер телефона:</b> {your_profile[4]}\n<b>адрес доставки:</b> {your_profile[5]}\n<b>Почта:</b> {your_profile[6]}",
        reply_markup=profile_keyboard.profile
    )
    await state.clear()
