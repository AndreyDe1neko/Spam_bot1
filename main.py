import time
from telethon import TelegramClient
from telethon.errors import PeerIdInvalidError
from api import API_KEY, API_HASH

api_id = API_KEY   # api id
api_hash = API_HASH

client = TelegramClient("bot", api_id, api_hash)

try:
    timer = int(input("Insert your time in minutes (default it's 1 hour): "))
except ValueError:
    timer = 60*60
user_text = input("Insert your text: ")


async def handler_all(timer, user_text="default text"):
    line = ''
    with open("chat_list.txt", 'r') as r:
        line = r.read().splitlines()
    while True:
        for i in line:
            try:
                await client.send_message(int(i), user_text)
            except PeerIdInvalidError:
                print(f"Chat № {i} error")
        time.sleep(timer*60)


with client:
    client.loop.run_until_complete(handler_all(timer, user_text))