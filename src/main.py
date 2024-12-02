import asyncio
import logging
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from aiogram.filters import CommandStart
from aiogram.types import Message, InputMediaPhoto

from service.callback import *
from config import settings, dp, bot
from service.cryptService import CryptService
from service.userService import UserService
from database.repository import Repository
from service.shedulerService import SchedulerService

HELLOW_TEXT = """Привет, участники лучшей команды ШУС в Вологодской области! Сейчас я расскажу вам правила нашей игры.

У вашей команды есть цель вырастить и максимально прокачать своего персонажа - активиста ШУС. Сделать это можно за баллы, которые вы получаете в течении игры.

<b>Начисление баллов происходит следующим образом:</b>
1. Каждый новый день вам начисляется минимальное количество баллов за прошедший день конкурса. Это количество будет фиксированным для всех команд (3 балла) вне зависимости от выполненных заданий.

2. Основные баллы начисляются за выполнение конкурсных заданий из чек-листа (таблицы). Каждое выполненное задание приносит определенное количество баллов — от 1 до 32, в зависимости от сложности. Вы всей командой можете самостоятельно выбирать, какие задания будете выполнять. Стоимость заданий указана в чек-листе и в критериях. Все конкурсные задания вы получаете через этот бот, а сдаете их в сообщения Шиншилле Сушке (@shinshila_shus).

<b>В игре имеются задания есть 2-х типов:</b>
1. Те, которые вы можете выполнить всего 1 раз за игру
2. Те, в которые можно выполнять каждый игровой день до 18:00 (кроме выходных)

<b>Прокачка персонажа:</b>
На полученные баллы от заданий команды должны прокачивать своего персонажа по следующим пунктам:
- Покормить (минимум 3 раза в день)
- Поиграть (повышается настроение) (минимум 3 раза в день)
- Прокачать личные качества (строка, чтобы они сами вписывали их за баллы) (за 1 слово - 5 баллов)
- Уложить спать (1 раз вечером)

За персонажем необходим постоянный уход. Если команда не будет заботиться о нем (например, не покормить, не уложить спать), то баллы начнут уменьшаться.

<b>Время для прокачки:</b>
- Команда может прокачивать персонажа на протяжении всей игры с 2 по 13 декабря Последняя прокачка пройдет в пятницу 13 декабря.

Победителем станет та команда, которая в конце конкурса прокачает своего персонажа до наивысшего уровня и качественно выполнит максимальное количество заданий.
"""

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    id = str(message.from_user.id)
    user = await Repository.getUserById(id)
    if user == None:
        await Repository.addUser(id)
        keyboard = getStartKeyboard()
        text = HELLOW_TEXT
        await message.answer(text, reply_markup=keyboard)
    elif user.name == None:
        keyboard = getStartKeyboard()
        text = HELLOW_TEXT
        await message.answer(text, reply_markup=keyboard)
    else:
        keyboard = getMainKeyboard()
        text = "Главная страница"
        await message.answer_photo(
            photo="AgACAgIAAxkBAAMTZ00ccDeMf_BT4x6Lfq9PXLSsqtwAAi3gMRucNWhKCE-1xazOQrIBAAMCAAN5AAM2BA",
             reply_markup=keyboard)


@dp.message(lambda message: message.photo)
async def get_file_id(message: Message):
    file_id = message.photo[-1].file_id
    await message.reply(f"File ID: {file_id}")
    await bot.send_photo(chat_id=message.from_user.id, photo=file_id)

@dp.message(lambda message: message.document)
async def get_file_id(message: Message):
    file_id = message.document.file_id
    await message.reply(f"File ID: {file_id}")
    await bot.send_document(chat_id=message.from_user.id, document=file_id)

@dp.message()
async def echo_handler(message: Message) -> None:
    id = str(message.from_user.id)
    user = await Repository.getUserById(id)
    text = ""
    if user.rename_event:
        await UserService.rename(user, message.text)
        text = f"Новое имя персонажа: {message.text}!"
        keyboard = getMainKeyboard()
    elif message.text[:7] == "encrypt":
        text = CryptService.encrypt(message.text[8:], settings.CRYPT_KEY)
        keyboard = None
    else:
        text = await UserService.checkCodeWord(
            user, CryptService.decrypt(message.text, settings.CRYPT_KEY))
        keyboard = None
    await message.answer(text, reply_markup=keyboard)

async def main() -> None:
    await SchedulerService.scheduleBroadcast()
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
