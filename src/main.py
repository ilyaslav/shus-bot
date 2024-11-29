import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
dp = Dispatcher()

from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram.types import Message, ContentType

from src.service.callback import *
from config import settings
from service.cryptService import CryptService

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    id = str(message.from_user.id)
    #user_exist
    if True: #check_name
        keyboard = getStartKeyboard()
        # text = "cryypt"
        text = CryptService.generate_key()
    else:
        keyboard = getMainKeyboard()
        text = "Пока"
    await message.answer(text, reply_markup=keyboard)


@dp.message()
async def test(message: Message):
    id = str(message.from_user.id)
    keyboard = getMainKeyboard()
    text = message.text
    await message.answer(text)
    crypt = CryptService.encrypt(text, settings.CRYPT_KEY)
    await message.answer(crypt)
    decrypt = CryptService.decrypt(crypt, settings.CRYPT_KEY)
    await message.answer(decrypt)

# @dp.message()
async def echo_handler(message: Message) -> None:
    id = str(message.from_user.id)
    #check rename_event
    #chech code_word
    keyboard = getMainKeyboard()
    await message.answer("Главная страница:", reply_markup=keyboard)


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=settings.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
