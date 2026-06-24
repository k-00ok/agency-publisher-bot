from __future__ import annotations

from aiogram import Dispatcher

from app.handlers import router as start_router

_registered = False


def register_handlers(dp: Dispatcher) -> None:
    global _registered
    if _registered:
        return

    dp.include_router(start_router)
    _registered = True
