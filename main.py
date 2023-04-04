"""File with telebot methods."""
from telebot.types import Message
from telebot.async_telebot import AsyncTeleBot
from config import TEMP_PATH, NO_DATA, SEARCH_MSG, HELLOW_MSG
from audio_works import run_ffmpeg, choose_topic, recognise
from logger import init_logger
import logging
import uuid
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = AsyncTeleBot(TOKEN)
logger = logging.getLogger('speech.main.file')


async def save_files(message: Message) -> tuple:
    """Function controls file saving.

    Args:
        message (Message): audio message from telebot.

    Returns:
        (tuple): tuple of paths for audion files.
    """
    file_id = uuid.uuid4()
    side_file = f"{TEMP_PATH}{file_id}.ogg"
    audio_file = f"{TEMP_PATH}{file_id}.wav"
    file_info = await bot.get_file(message.voice.file_id)
    if not os.path.exists(TEMP_PATH):
        os.mkdir(TEMP_PATH)
    with open(side_file, "wb") as new_file:
        new_file.write(await bot.download_file(file_info.file_path))

    await run_ffmpeg(side_file, audio_file)
    return side_file, audio_file


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message: Message) -> None:
    """Method sends hellow message.

    Args:
        message (Message): command /start or /help
    """
    await bot.send_message(message.chat.id, HELLOW_MSG)


@bot.message_handler(content_types=["voice"])
async def voice_processing(message: Message) -> None:
    """Method gets voice message from telebot and replies topic message.

    Args:
        message (Message): telebot.types.Message object with voice.
    """
    await bot.send_message(message.chat.id, SEARCH_MSG)

    side_file, audio_file = await save_files(message)
    voice_text = recognise(audio_file)
    answer = NO_DATA if voice_text == NO_DATA else choose_topic(voice_text)
    logger.info(" | ".join([message.from_user.username, voice_text, answer]))

    await bot.send_message(message.chat.id, answer)

    await bot.delete_message(message.chat.id, message.message_id + 1)
    os.remove(side_file)
    os.remove(audio_file)


if __name__ == "__main__":
    init_logger('speech')
    asyncio.run(bot.polling())
