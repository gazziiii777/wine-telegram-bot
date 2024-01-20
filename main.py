import asyncio
import logging

from core.settings import settings
from core.dispatcher import bot, dp
from core.handlers import commands, callback
from core.admin_panel.headlers import command_admin

async def start_bot():
    await bot.send_message(chat_id=settings.bots.admin_id, text='Бот запущен')


async def stop_bot():
    await bot.send_message(chat_id=settings.bots.admin_id, text='Бот остановлен')


async def main():
    logging.basicConfig(level=logging.INFO, filename="bot_log.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")

    dp.startup.register(start_bot)  # Отправляет сообщение админу когда бот запускается
    dp.shutdown.register(stop_bot)  # Отправляет сообщение админу когда бот останавлявается
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
