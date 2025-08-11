import os
import asyncio
from datetime import datetime
from telethon import TelegramClient, events

api_id = int(os.getenv('20211284'))
api_hash = os.getenv('50af57e706e5517aa5991b7ce7049c5d')

# Список для отслеживания — укажи username или id
watch_list = ['@Uuycycysuvydr', '@mifistori']

client = TelegramClient('userbot_session', api_id, api_hash)
last_status = {}

@client.on(events.UserUpdate)
async def user_update_handler(event):
    user_id = event.user_id
    if user_id is None:
        return
    entity = await client.get_entity(user_id)
    if (entity.username not in watch_list) and (str(entity.id) not in watch_list):
        return
    online = event.online
    prev = last_status.get(user_id)
    if prev != online:
        last_status[user_id] = online
        status_text = "в сети" if online else "не в сети"
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        msg = f"⚡ Пользователь {entity.first_name} (@{entity.username}) {status_text} — {now}"
        print(msg)
        await client.send_message('me', msg)

async def main():
    await client.start()
    print("Бот запущен и работает...")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
