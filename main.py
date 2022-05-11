import logging
import pytube
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5203623681:AAFZ2DC0-dBv1Ad_c5Wva45ffmJDj685wq0'
# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("You can download video or music from youtube")


@dp.message_handler()
async def echo(message: types.Message):
    try:
        if message.text[:5] =='https':


            await message.answer('ssilka')
        else:
            await message.answer('Бот принимает только ссылку')

    except TypeError:
        pass





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)