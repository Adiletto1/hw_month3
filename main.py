import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import random
import os
import logging
logging.basicConfig(level=logging.INFO)


load_dotenv()
TOKEN = getenv("TOKEN_BOT")
bot = Bot(token=TOKEN)
dp = Dispatcher()
IMAGES_FOLDER = ('images')


@dp.message(Command('pic'))
async def send_random_pic(message: types.Message):
    pic_files = [f for f in os.listdir(IMAGES_FOLDER) if os.path.isfile(os.path.join(IMAGES_FOLDER, f))]

    if pic_files:
        random_pic = random.choice(pic_files)
        pic_path = os.path.join(IMAGES_FOLDER, random_pic)


        await message.answer_photo(types.FSInputFile(pic_path), caption="Ваша случайная картинка")
    else:
        await message.reply("В папке images нет картинок.")

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f'Привет {message.from_user.username}')


@dp.message(Command("info"))
async def start(message: types.Message):
    await message.answer(f'Твое имя: {message.from_user.username}\nТвой id: {message.from_user.id}\nТвое полное имя: {message.from_user.full_name}')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())