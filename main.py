import logging
from aiogram import Bot, Dispatcher, executor, types
from Downloader import find_stream, download, get_file_name
from config import API_TOKEN
from aiogram.types import ContentType, File, Message
import speech_recognition as sr

recognizer = sr.Recognizer()

# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def handle_file(file: File, file_name: str, path: str):

    await bot.download_file(file_path=file.file_path, destination=f"{path}/{file_name}")

@dp.message_handler(content_types=[ContentType.VOICE])
async def voice_message_handler(message: Message):
    voice = await message.voice.get_file()
    path = "/Users/a_krut/Desktop/Download_video_bot/voices"
    file_format = 'wav'
    await handle_file(file=voice, file_name=f"{voice.file_id}.{file_format}", path=path)
    file = sr.AudioFile(f"/Users/a_krut/Desktop/Download_video_bot/voices/{voice.file_id}.{file_format}")
    with file as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)
    await message.reply(text)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("You can download video or music from youtube")


@dp.message_handler()
async def echo(message: types.Message):
    try:
        if message.text[:5] =='https':
            url = message.text
            try:
                stream = find_stream(url)
                await message.answer('Идет обработка видео')
                download(url, stream)

                file_name = get_file_name(url)
                file_name = str(file_name)+'.mp4'
                file_path = '/Users/a_krut/Desktop/Download_video_bot/videos/'+file_name
                with open(file_path,'rb') as file:
                    await message.answer_document(file, file_name)

                #await message.answer('Загрузка прошла успешно')
            except FileExistsError:
                pass


        else:
            await message.answer('Бот принимает только ссылку')

    except TypeError:
        pass





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)