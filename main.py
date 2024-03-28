from aiogram import Dispatcher, types, Bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
import asyncio

token = ''
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    try:
        await message.answer('Hello')
    except TypeError:
        await message.answer('Error')


async def main():
    bot = Bot(token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt as ek:
        print('Exit', ek)
