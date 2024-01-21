import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
import logging
from handlers.start import start_router
from handlers.info import info_router
from handlers.pic import pic_router
from handlers.opros import opros_router

logging.basicConfig(level=logging.INFO)


load_dotenv()
TOKEN = getenv("TOKEN_BOT")
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    (dp.include_router(start_router),
     dp.include_router(info_router),
     dp.include_router(pic_router),
     dp.include_router(opros_router),
     await dp.start_polling(bot),)


if __name__ == '__main__':
    asyncio.run(main())