from telethon.sync import TelegramClient
from telethon.tl import functions, types
import time

api_id = '0000'
api_hash = '0000'
phone_number = '0000'

with TelegramClient('session_name', api_id, api_hash) as client:
    while True:
        # Отправка сообщения в чат
        chat_id = '0000'
        message = '🧀 Получить карту'
        client.send_message(chat_id, message)
        
        # Задержка перед следующей отправкой (в секундах)
        #time.sleep(4 * 60 * 60)  # 4 часа
        time.sleep(10)
