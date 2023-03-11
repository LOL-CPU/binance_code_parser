from telethon.sync import TelegramClient, events

api_id = 27019282
api_hash = 'd335785b2641e327c30ca20d56cab317'
chat_name = '-1001491932389'
file_name = 'messages.txt'

client = TelegramClient('session_name', api_id, api_hash)
client.start()


@client.on(events.NewMessage(chats=chat_name))
async def handler(event):
    with open(file_name, 'a') as f:
        f.write(event.message.message + '\n')

client.run_until_disconnected()