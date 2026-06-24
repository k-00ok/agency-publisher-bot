from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from app.database.supabase import create_client, create_post, delete_client, get_clients
from app.keyboards import clients_menu_keyboard, main_menu_keyboard

router = Router()


class ClientStates(StatesGroup):
    adding_client = State()
    deleting_client = State()


class PostStates(StatesGroup):
    selecting_client = State()
    entering_caption = State()


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


@router.message(lambda m: m.text == '📝 منشور جديد')
async def new_post(message: Message, state: FSMContext) -> None:
    result = get_clients()
    clients = getattr(result, 'data', []) or []
    if not clients:
        await message.answer('لا يوجد عملاء.')
        return
    text = 'اختر العميل بإرسال الرقم:\n' + '\n'.join(f"{item['id']} - {item['name']}" for item in clients)
    await state.set_state(PostStates.selecting_client)
    await message.answer(text)


@router.message(PostStates.selecting_client)
async def select_post_client(message: Message, state: FSMContext) -> None:
    await state.update_data(client_id=int(message.text.strip()))
    await state.set_state(PostStates.entering_caption)
    await message.answer('أرسل الكابشن')


@router.message(PostStates.entering_caption)
async def save_post(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    create_post({
        'client_id': data['client_id'],
        'caption': message.text,
        'status': 'draft',
        'media_type': 'text',
        'media_paths': [],
    })
    await state.clear()
    await message.answer('تم حفظ المنشور كمسودة', reply_markup=main_menu_keyboard())