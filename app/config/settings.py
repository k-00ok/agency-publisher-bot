from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os
from dotenv import load_dotenv

ROOT=Path(__file__).resolve().parents[2]
env_file=ROOT/'.env'
if env_file.exists():
    load_dotenv(env_file)

@dataclass(frozen=True)
class Settings:
    BOT_TOKEN:str
    SUPABASE_URL:str
    SUPABASE_KEY:str
    DELETE_MEDIA_AFTER_DAYS:int

    @classmethod
    def load(cls)->'Settings':
        bt=os.getenv('BOT_TOKEN')
        su=os.getenv('SUPABASE_URL')
        sk=os.getenv('SUPABASE_KEY')
        if not bt:
            raise RuntimeError('BOT_TOKEN is required')
        if not su:
            raise RuntimeError('SUPABASE_URL is required')
        if not sk:
            raise RuntimeError('SUPABASE_KEY is required')
        return cls(bt,su,sk,int(os.getenv('DELETE_MEDIA_AFTER_DAYS','30')))

settings=Settings.load()
