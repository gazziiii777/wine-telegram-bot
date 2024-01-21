# Cоздаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
from aiogram.fsm.state import StatesGroup, State


class FSMPromoCode(StatesGroup):
    promo_code = State()  # Состояние ожидания ввода промокода


class FSMPromoCodeAdd(StatesGroup):
    promo_code_name = State()  # Состояние ожидания ввода промокода
    promo_code_value = State()


class FSMPromoCodeDelete(StatesGroup):
    promo_code_name = State()  # Состояние ожидания ввода промокода


class FSMUserRegister(StatesGroup):
    telegram_user_name = State()  # Состояние ожидания ввода промокода
    full_name = State()
    phone_number = State()
    delivery_address = State()
    mail = State()


