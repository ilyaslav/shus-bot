from aiogram import F
from aiogram.types import CallbackQuery

from src.service.keyboardBuilder import *
from main import dp

@dp.callback_query(F.data == "main")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getMainKeyboard()
    await callback_query.message.answer("Главная страница", reply_markup=keyboard)


@dp.callback_query(F.data == "set_name")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    #rename_event
    await callback_query.message.answer("Введите имя персонажа:")


@dp.callback_query(F.data == "question")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getSendQuestionKeyboard()
    await callback_query.message.answer("Задать вопрос", reply_markup=keyboard)

@dp.callback_query(F.data == "get_task")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getTaskLevelKeyboard()
    await callback_query.message.answer("Выбрать и выпонить задание", reply_markup=keyboard)

@dp.callback_query(F.data == "back_task")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getTaskLevelKeyboard()
    await callback_query.message.answer("Главная страница", reply_markup=keyboard)

@dp.callback_query(F.data == "submit_task")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getSubmitTaskKeyboard()
    await callback_query.message.answer("Сдать задание", reply_markup=keyboard)

@dp.callback_query(F.data == "up_character")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getUpCharacterKeyboard()
    await callback_query.message.answer("Прокачать персонажа", reply_markup=keyboard)

@dp.callback_query(F.data == "character_info")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getCharacterInfoKeyboard()
    await callback_query.message.answer("Оценить состояние персонажа", reply_markup=keyboard)


@dp.callback_query(F.data == "easy")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getTaskKeyboard()
    await callback_query.message.answer("Простой", reply_markup=keyboard)

@dp.callback_query(F.data == "midle")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getTaskKeyboard()
    await callback_query.message.answer("Средний", reply_markup=keyboard)

@dp.callback_query(F.data == "hard")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getTaskKeyboard()
    await callback_query.message.answer("Сложный", reply_markup=keyboard)

@dp.callback_query(F.data == "back_task_level")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getMainKeyboard()
    await callback_query.message.answer("Главная страница", reply_markup=keyboard)


@dp.callback_query(F.data == "back_task_info")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getTaskInfoKeyboard()
    await callback_query.message.answer("Выбрать и выпонить задание", reply_markup=keyboard)


@dp.callback_query(F.data == "back_send_question")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getMainKeyboard()
    await callback_query.message.answer("Главная страница", reply_markup=keyboard)

@dp.callback_query(F.data == "back_submit_task")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getMainKeyboard()
    await callback_query.message.answer("Главная страница", reply_markup=keyboard)


@dp.callback_query(F.data == "feed")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getUpCharacterKeyboard()
    await callback_query.message.answer("Покормить", reply_markup=keyboard)

@dp.callback_query(F.data == "play")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getUpCharacterKeyboard()
    await callback_query.message.answer("Поиграть", reply_markup=keyboard)

@dp.callback_query(F.data == "speack")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getUpCharacterKeyboard()
    await callback_query.message.answer("Прокачать личные качества", reply_markup=keyboard)

@dp.callback_query(F.data == "sleep")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getUpCharacterKeyboard()
    await callback_query.message.answer("Уложить спать", reply_markup=keyboard)

@dp.callback_query(F.data == "back_up_chracter")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getMainKeyboard()
    await callback_query.message.answer("Главная страница", reply_markup=keyboard)


@dp.callback_query(F.data == "back_character_info")
async def callback_button(callback_query):
    id = str(callback_query.message.from_user.id)
    keyboard = getMainKeyboard()
    await callback_query.message.answer("Главная страница", reply_markup=keyboard)
