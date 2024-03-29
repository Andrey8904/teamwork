from aiogram import Dispatcher, types, Bot, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
import asyncio
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from keys import bot_token


token = bot_token
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    try:
        builder = InlineKeyboardBuilder()
        first_btn = InlineKeyboardButton(text='Кнопка 1', callback_data='first_button')
        builder.row(first_btn)
        await message.answer('Hello! I am Bot.\n\nHow i can help?', reply_markup=builder.as_markup())

    except TypeError:
        await message.answer('Error')


@dp.callback_query(F.data == 'first_button')
async def btn_1(callback: types.CallbackQuery):
    try:
        builder = InlineKeyboardBuilder()
        second_btn = InlineKeyboardButton(text='Кнопка 2', callback_data='second_button')
        builder.row(second_btn)
        await callback.message.answer('Button one', reply_markup=builder.as_markup())
    except TypeError:
        await callback.message.answer('Error btn one')


async def main():
    bot = Bot(token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt as ek:
        print('Exit', ek)


