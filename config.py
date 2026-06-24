from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv('BOT_TOKEN', '')
SUPABASE_URL = getenv('SUPABASE_URL', '')
SUPABASE_KEY = getenv('SUPABASE_KEY', '')
DELETE_MEDIA_AFTER_DAYS = int(getenv('DELETE_MEDIA_AFTER_DAYS', '30'))
