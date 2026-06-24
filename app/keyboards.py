from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='👥 العملاء')],
            [KeyboardButton(text='📝 منشور جديد')],
            [KeyboardButton(text='📅 المنشورات المجدولة')],
            [KeyboardButton(text='📊 سجل النشر')],
        ],
        resize_keyboard=True,
    )
