# Cоздаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
from aiogram.fsm.state import StatesGroup, State


class FSMPromoCode(StatesGroup):
    promo_code = State()  # Состояние ожидания ввода промокода
