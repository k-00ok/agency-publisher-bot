from __future__ import annotations

from aiogram import Dispatcher, Router

_registered=False
_start_router=Router(name="start")


def register_handlers(dp: Dispatcher) -> None:
    global _registered
    if _registered:
        return
    dp.include_router(_start_router)
    # additional routers are included here through the same pattern
    _registered=True
