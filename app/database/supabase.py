from __future__ import annotations

from supabase import Client, create_client

from app.config.logging import setup_logging
from app.config.settings import settings

_logger = setup_logging()
_client: Client | None = None


def get_supabase() -> Client:
    global _client
    if _client is not None:
        return _client
    try:
        _client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        return _client
    except Exception as exc:
        _logger.exception('Failed to initialize Supabase client')
        raise RuntimeError('Unable to initialize Supabase client') from exc


def create_client(name: str):
    return get_supabase().table('clients').insert({'name': name}).execute()


def get_clients():
    return get_supabase().table('clients').select('*').order('id').execute()


def delete_client(client_id: int):
    return get_supabase().table('clients').delete().eq('id', client_id).execute()
