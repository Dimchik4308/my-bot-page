import asyncio

from aiogram import Bot, Dispatcher, types,F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

async def main():
    bot = Bot('8273234981:AAGvc1fqhVngOjj8KQ0amwp_JKG80cov4tM')
    dp = Dispatcher()

    markup = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text='Сайт', web_app=WebAppInfo(url='https://dimchik4308.github.io/my-bot-page/index.html#'))

        ]

    ],resize_keyboard=True)

    @dp.message(CommandStart())
    async def start(message: types.Message):
        await message.reply(f'Здоров, {message.from_user.first_name}',reply_markup=markup)



    #
    # @dp.message()
    # async def info(message: types.Message):
    #
    #     await message.reply('Чекни сайт',reply_markup=markup)
    #
    # @dp.callback_query()
    # async def callback(call):
    #     if call.data=='hello':
    #         await call.message.answer('Бог в поміч')


    await dp.start_polling(bot)




if __name__=='__main__':
    asyncio.run(main())