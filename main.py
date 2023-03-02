import telegram
import time
import aiogram

# введите токен вашего бота
TOKEN = '5721038097:AAGlW6g4mA7a4YbESCs6FKXe-mTj5zBjXWs'

# создайте экземпляр клиента Telegram
bot = telegram.Bot(token=TOKEN)

# введите ID чата, в котором вы хотите собирать сообщения
CHAT_ID = '-1001491932389'

# установите интервал между сбором сообщений (в секундах)
INTERVAL = 60

# функция для получения всех сообщений из чата
def get_all_messages():
    all_messages = []
    last_message_id = None
    while True:
        messages = bot.get_chat_history(chat_id=CHAT_ID, limit=100, offset=last_message_id)
        if not messages:
            break
        all_messages.extend(messages)
        last_message_id = messages[-1].message_id
    return all_messages

# бесконечный цикл сбора сообщений с заданным интервалом
while True:
    all_messages = get_all_messages()
    # обработка собранных сообщений здесь
    time.sleep(INTERVAL)
