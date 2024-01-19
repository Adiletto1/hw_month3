from aiogram import Router, types
from aiogram.filters import  Command
import os
import random

pic_router = Router()
IMAGES_FOLDER = ('images')


@pic_router.message(Command('pic'))
async def send_random_pic(message: types.Message):
    pic_files = [f for f in os.listdir(IMAGES_FOLDER) if os.path.isfile(os.path.join(IMAGES_FOLDER, f))]

    if pic_files:
        random_pic = random.choice(pic_files)
        pic_path = os.path.join(IMAGES_FOLDER, random_pic)


        await message.answer_photo(types.FSInputFile(pic_path), caption="Ваша случайная картинка")
    else:
        await message.reply("В папке images нет картинок.")