from telethon.sync import TelegramClient
from telethon.tl import functions, types
import time

api_id = '21202416'
api_hash = 'b70404d0fe911e638a187c81d3a8a28f'
phone_number = '+79151768207'

with TelegramClient('session_name', api_id, api_hash) as client:
    while True:
        # Отправка сообщения в чат
        chat_id = '5633724545'
        message = '🧀 Получить карту'
        client.send_message(chat_id, message)
        
        # Задержка перед следующей отправкой (в секундах)
        #time.sleep(4 * 60 * 60)  # 4 часа
        time.sleep(10)