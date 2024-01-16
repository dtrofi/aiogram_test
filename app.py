# Установка

# pip install aiogram
# или pip install aiogram==3.3.0
# pip install python-dotenv

# Документация
# https://docs.aiogram.dev/en/latest/

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token="6686401845:AAGrLAjqHkm1g98Is15PtxUZ1IFUbAIB0lc")
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Эта была команда старт!")


@dp.message()
async def echo(message: types.Message):
    text = message.text
    if text in ["Привет", "привет", "hi", "hello"]:
        await message.answer("И тебе привет!")
    elif text in ["Пока", "пока", "пакеда", "До свидания"]:
        await message.answer("Ну и хрен с тобой!")
    else:
        await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
