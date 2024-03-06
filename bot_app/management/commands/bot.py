import asyncio

from aiogram import F, types
from aiogram.enums import ChatAction
from aiogram.filters.command import Command as AioCommand
from asgiref.sync import sync_to_async
from django.core.management.base import BaseCommand

from bot_app.models import User, Img
from loader import URL, bot, dp


class Command(BaseCommand):
    help = 'RUN COMMAND: python manage.py bot'

    def handle(self, *args, **options):
        asyncio.run(main())


@dp.message(AioCommand("start"))
async def start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Грузить собаку")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
    )
    user = await sync_to_async(User.objects.get_or_create)(
        user_id=message.from_user.id,
        defaults={
            'username': message.from_user.username
        }
    )
    print(user)
    await message.reply(
        f"Привет {message.from_user.username}! Я отправляю изображения собак.",
        reply_markup=keyboard
    )


@dp.message(F.text == "Грузить собаку")
async def image(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    user, created = await sync_to_async(User.objects.get_or_create)(
        user_id=message.from_user.id,
        defaults={
            'username': message.from_user.username
        }
    )
    image = types.URLInputFile(URL)
    sent_message = await message.reply_photo(
        photo=image
    )
    image_id = sent_message.photo[-1].file_id
    await sync_to_async(Img.objects.create)(
        user=user,
        image_id=image_id
    )


async def main():
    await dp.start_polling(bot)
