import asyncio

from app.bot import get_bot, get_dispatcher
from app.config.logging import setup_logging
from app.router import register_handlers


async def on_startup() -> None:
    setup_logging().info("Bot started")


async def on_shutdown() -> None:
    bot = get_bot()
    setup_logging().info("Bot stopped")
    await bot.session.close()


async def main() -> None:
    logger = setup_logging()
    bot = get_bot()
    dp = get_dispatcher()

    register_handlers(dp)

    await on_startup()

    try:
        logger.info("Starting polling")
        await dp.start_polling(bot)
    finally:
        await on_shutdown()


if __name__ == "__main__":
    asyncio.run(main())