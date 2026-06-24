from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from app.database.supabase import create_client, delete_client, get_clients
from app.keyboards import clients_menu_keyboard, main_menu_keyboard

router = Router()


class ClientStates(StatesGroup):
    adding_client = State()
    deleting_client = State()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer('Agency Publisher Bot', reply_markup=main_menu_keyboard())


@router.message(lambda m: m.text == '👥 العملاء')
async def clients_menu(message: Message) -> None:
    await message.answer('إدارة العملاء', reply_markup=clients_menu_keyboard())


@router.message(lambda m: m.text == '⬅️ رجوع')
async def back_to_main(message: Message) -> None:
    await message.answer('القائمة الرئيسية', reply_markup=main_menu_keyboard())


@router.message(lambda m: m.text == '➕ إضافة عميل')
async def add_client_prompt(message: Message, state: FSMContext) -> None:
    await state.set_state(ClientStates.adding_client)
    await message.answer('أرسل اسم العميل')


@router.message(ClientStates.adding_client)
async def add_client(message: Message, state: FSMContext) -> None:
    create_client(message.text.strip())
    await state.clear()
    await message.answer('تمت إضافة العميل', reply_markup=clients_menu_keyboard())


@router.message(lambda m: m.text == '📋 عرض العملاء')
async def show_clients(message: Message) -> None:
    result = get_clients()
    clients = getattr(result, 'data', []) or []
    if not clients:
        await message.answer('لا يوجد عملاء.')
        return
    text = '\n'.join(f"{item['id']} - {item['name']}" for item in clients)
    await message.answer(text)


@router.message(lambda m: m.text == '🗑 حذف عميل')
async def delete_client_prompt(message: Message, state: FSMContext) -> None:
    result = get_clients()
    clients = getattr(result, 'data', []) or []
    if not clients:
        await message.answer('لا يوجد عملاء للحذف.')
        return
    text = 'أرسل رقم العميل للحذف:\n' + '\n'.join(f"{item['id']} - {item['name']}" for item in clients)
    await state.set_state(ClientStates.deleting_client)
    await message.answer(text)


@router.message(ClientStates.deleting_client)
async def delete_client_handler(message: Message, state: FSMContext) -> None:
    delete_client(int(message.text.strip()))
    await state.clear()
    await message.answer('تم حذف العميل', reply_markup=clients_menu_keyboard())
