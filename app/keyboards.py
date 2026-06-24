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


def clients_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='➕ إضافة عميل')],
            [KeyboardButton(text='📋 عرض العملاء')],
            [KeyboardButton(text='🗑 حذف عميل')],
            [KeyboardButton(text='⬅️ رجوع')],
        ],
        resize_keyboard=True,
    )
