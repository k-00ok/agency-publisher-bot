import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN


def register_handlers(dp: Dispatcher) -> None:
    return


async def on_startup(bot: Bot) -> None:
    logging.info('Bot started')


async def on_shutdown(bot: Bot) -> None:
    logging.info('Bot stopped')
    await bot.session.close()


async def main() -> None:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    register_handlers(dp)
    await on_startup(bot)
    try:
        await dp.start_polling(bot)
    finally:
        await on_shutdown(bot)


if __name__ == '__main__':
    asyncio.run(main())
