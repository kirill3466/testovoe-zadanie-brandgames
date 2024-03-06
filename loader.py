from aiogram import Bot, Dispatcher
from django.conf import settings

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

URL = "http://thedogapi.com/api/images/get?format=src&type=jpg"
