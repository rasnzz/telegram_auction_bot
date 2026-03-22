# config.py - с поддержкой SOCKS5 прокси
import os
import re
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    
    # Настройка прокси
    PROXY_URL = os.getenv("PROXY_URL", "")
    
    # Обработка CHANNEL_ID
    CHANNEL_ID_STR = os.getenv("CHANNEL_ID", "").strip()
    CHANNEL_ID = None
    
    if CHANNEL_ID_STR:
        if CHANNEL_ID_STR.lstrip('-').replace('.', '').isdigit():
            CHANNEL_ID = int(CHANNEL_ID_STR)
        elif CHANNEL_ID_STR.startswith('@'):
            CHANNEL_ID = CHANNEL_ID_STR
        else:
            match = re.search(r'(-?\d+)', CHANNEL_ID_STR)
            if match:
                CHANNEL_ID = int(match.group(1))
            else:
                CHANNEL_ID = CHANNEL_ID_STR
    
    admin_ids_str = os.getenv("ADMIN_IDS", "")
    if admin_ids_str:
        ADMIN_IDS = [int(id.strip()) for id in admin_ids_str.split(",") if id.strip()]
    else:
        ADMIN_IDS = []
    
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///auctions.db")
    
    BID_TIMEOUT_MINUTES = int(os.getenv("BID_TIMEOUT_MINUTES", "180"))  # 3 часа
    BID_STEP_PERCENT = int(os.getenv("BID_STEP_PERCENT", "10"))
    
    DATABASE_TIMEOUT = int(os.getenv("DATABASE_TIMEOUT", "60"))
    BID_RETRY_ATTEMPTS = int(os.getenv("BID_RETRY_ATTEMPTS", "3"))
    
    if not BOT_TOKEN:
        print("⚠️  ВНИМАНИЕ: BOT_TOKEN не установлен!")
        print("Создайте файл .env с токеном вашего бота")
