from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from service.taskService import TaskService

def getMainKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Задать вопрос", callback_data="question", url="https://t.me/shinshila_shus")],
            [InlineKeyboardButton(text="Выбрать и выпонить задание", callback_data="get_task")],
            [InlineKeyboardButton(text="Сдать задание", callback_data="submit_task")],
            [InlineKeyboardButton(text="Прокачать персонажа", callback_data="up_character")],
            [InlineKeyboardButton(text="Оценить состояние персонажа", callback_data="character_info")]
        ]
    )

def getStartKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Назвать персонажа", callback_data="set_name")]
        ]
    )

def getTaskLevelKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Простой", callback_data="easy")],
            [InlineKeyboardButton(text="Средний", callback_data="midle")],
            [InlineKeyboardButton(text="Сложный", callback_data="hard")],
            [InlineKeyboardButton(text="?", callback_data="?")],
            [InlineKeyboardButton(text="Назад", callback_data="main")],
        ]
    )

async def getTaskKeyboard(level: str):
    return await TaskService.getTaskKeyboard(level)

def getTaskInfoKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="get_task")],
        ]
    )

def getSubmitTaskKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Сдать задание", url="https://t.me/shinshila_shus")],
            [InlineKeyboardButton(text="Назад", callback_data="main")],
        ]
    )

def getUpCharacterKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Покормить", callback_data="feed")],
            [InlineKeyboardButton(text="Поиграть", callback_data="play")],
            [InlineKeyboardButton(text="Прокачать личные качества", callback_data="speack")],
            [InlineKeyboardButton(text="Уложить спать", callback_data="sleep")],
            [InlineKeyboardButton(text="Сменить имя", callback_data="set_name")],
            [InlineKeyboardButton(text="Назад", callback_data="main")],
        ]
    )

def getCharacterInfoKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="main")],
        ]
    )
