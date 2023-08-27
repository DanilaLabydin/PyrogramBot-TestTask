import config
import asyncio

from pyrogram import Client
from pyrogram.handlers import MessageHandler


async def send_scheduled_messages(client, message):
    print(message)
    # await message.forward("me")


app = Client("my_account", config.API_ID, config.API_HASH)
app.add_handler(MessageHandler(send_scheduled_messages))
app.run()
