from aiogram import F
from aiogram.types import CallbackQuery

from database.repository import Repository
from service.taskService import TaskService
from service.keyboardBuilder import *
from service.userService import UserService
from main import dp, bot

@dp.callback_query(F.data == "main")
async def callback_button(callback_query):
    id = str(callback_query.from_user.id)
    keyboard = getMainKeyboard()
    await callback_query.message.answer_photo(photo="AgACAgIAAxkBAAMTZ00ccDeMf_BT4x6Lfq9PXLSsqtwAAi3gMRucNWhKCE-1xazOQrIBAAMCAAN5AAM2BA", reply_markup=keyboard)


@dp.callback_query(F.data == "set_name")
async def callback_button(callback_query):
    id = str(callback_query.from_user.id)
    user = await Repository.getUserById(id)
    await UserService.setRenameEvent(user, True)
    await callback_query.message.answer("Введите имя персонажа:")

@dp.callback_query(F.data == "get_task")
async def callback_button(callback_query):
    id = str(callback_query.from_user.id)
    keyboard = getTaskLevelKeyboard()
    await callback_query.message.answer("Выберите уровень сложности: ", reply_markup=keyboard)

@dp.callback_query(F.data == "submit_task")
async def callback_button(callback_query):
    id = str(callback_query.from_user.id)
    keyboard = getSubmitTaskKeyboard()
    await callback_query.message.answer("""Чтобы сдать задние напишите в личные сообщения Шиншиллы Сушки (@shinshila_shus): название своей школы, уровень, номер задания и отправьте файлы, видеосообщения и прочее, если это предусмотрено условиями задания.""", reply_markup=keyboard)

@dp.callback_query(F.data == "up_character")
async def callback_button(callback_query):
    id = str(callback_query.from_user.id)
    keyboard = getUpCharacterKeyboard()
    await callback_query.message.answer("Прокачать персонажа", reply_markup=keyboard)

@dp.callback_query(F.data == "character_info")
async def callback_button(callback_query):
    id = str(callback_query.from_user.id)
    user = await Repository.getUserById(id)
    text, photo = await UserService.getUserInfo(user)
    keyboard = getCharacterInfoKeyboard()
    await callback_query.message.answer_photo(caption = text, photo = photo, reply_markup=keyboard)


@dp.callback_query(F.data == "easy")
async def callback_button(callback_query):
    id = str(callback_query.from_user.id)
    keyboard = await getTaskKeyboard("easy")
    await callback_query.message.answer("Список заданий:", reply_markup=keyboard)

@dp.callback_query(F.data == "midle")
async def callback_button(callback_query):
    id = str(callback_query.from_user.id)
    keyboard = await getTaskKeyboard("midle")
    await callback_query.message.answer("Список заданий:", reply_markup=keyboard)

@dp.callback_query(F.data == "hard")
async def callback_button(callback_query):
    id = str(callback_query.from_user.id)
    keyboard = await getTaskKeyboard("hard")
    await callback_query.message.answer("Список заданий:", reply_markup=keyboard)

@dp.callback_query(F.data == "?")
async def callback_button(callback_query):
    id = str(callback_query.from_user.id)
    keyboard = await getTaskKeyboard("?")
    await callback_query.message.answer("Список заданий:", reply_markup=keyboard)


@dp.callback_query(F.data == "feed")
async def callback_button(callback_query):
    id = str(callback_query.from_user.id)
    user = await Repository.getUserById(id)
    text = await UserService.feed(user)
    keyboard = getUpCharacterKeyboard()
    await callback_query.message.answer(text, reply_markup=keyboard)

@dp.callback_query(F.data == "play")
async def callback_button(callback_query):
    id = str(callback_query.from_user.id)
    user = await Repository.getUserById(id)
    text = await UserService.play(user)
    keyboard = getUpCharacterKeyboard()
    await callback_query.message.answer(text, reply_markup=keyboard)

@dp.callback_query(F.data == "speack")
async def callback_button(callback_query):
    id = str(callback_query.from_user.id)
    user = await Repository.getUserById(id)
    text = await UserService.speak(user)
    keyboard = getUpCharacterKeyboard()
    await callback_query.message.answer(text, reply_markup=keyboard)

@dp.callback_query(F.data == "sleep")
async def callback_button(callback_query):
    id = str(callback_query.from_user.id)
    user = await Repository.getUserById(id)
    text = await UserService.sleep(user)
    keyboard = getUpCharacterKeyboard()
    await callback_query.message.answer(text, reply_markup=keyboard)

@dp.callback_query(F.data == "back_up_character")
async def callback_button(callback_query):
    id = str(callback_query.from_user.id)
    keyboard = getMainKeyboard()
    await callback_query.message.answer("Главная страница", reply_markup=keyboard)


@dp.callback_query(F.data == "back_character_info")
async def callback_button(callback_query):
    id = str(callback_query.from_user.id)
    keyboard = getMainKeyboard()
    await callback_query.message.answer("Главная страница", reply_markup=keyboard)

@dp.callback_query(F.data)
async def callback_button(callback_query):
    text, type, attachments , level = await TaskService.getTask(callback_query.data)
    keyboard = getTaskInfoKeyboard(level)
    if type == "img":
        await callback_query.message.answer_media_group(attachments)
        await callback_query.message.answer(text, reply_markup=keyboard)
    elif type == "doc":
        await callback_query.message.answer(text, reply_markup=keyboard)
        for doc in attachments:
            await callback_query.message.answer_document(document=doc)
    else:
        await callback_query.message.answer(text, reply_markup=keyboard)
