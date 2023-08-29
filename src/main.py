import config
import asyncio
import datetime
import os

from pyrogram import Client
from pyrogram.handlers import MessageHandler


GREETING_TIME = datetime.timedelta(minutes=10)
SEND_PHOTO_TIME = datetime.timedelta(minutes=90)
GOODBYU_TIME = datetime.timedelta(minutes=120)
GREETING_MESSAGE = "Добрый день!"
SEND_PHOTO_MESSAGE = "Подготовила для вас материал"
GOODBYU_MESSAGE = "Скоро вернусь с новым материалом!"


async def send_scheduled_messages(client, message):
    if message.outgoing is True:
        return

    user_id = message.from_user.id
    message_date = message.date

    await client.send_message(
        chat_id=user_id,
        text=GREETING_MESSAGE,
        schedule_date=message_date + GREETING_TIME,
    )
    await client.send_message(
        chat_id=user_id,
        text=SEND_PHOTO_MESSAGE,
        schedule_date=message_date + SEND_PHOTO_TIME,
    )
    await client.send_photo(
        chat_id=user_id,
        photo="pyrogram.png",
        schedule_date=message_date + SEND_PHOTO_TIME,
    )

    async for message in app.search_messages(
        chat_id=user_id, query="Хорошего дня", from_user="me"
    ):
        return

    await client.send_message(
        chat_id=user_id, text=GOODBYU_MESSAGE, schedule_date=message_date + GOODBYU_TIME
    )


app = Client("my_account", config.API_ID, config.API_HASH)
app.add_handler(MessageHandler(send_scheduled_messages))
app.run()
