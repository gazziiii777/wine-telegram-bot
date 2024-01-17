from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from core.settings import settings

storage = MemoryStorage()
bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
dp = Dispatcher(storage=storage)