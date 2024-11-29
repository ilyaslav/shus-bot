from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

def getMainKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Задать вопрос", callback_data="question")],
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
            [InlineKeyboardButton(text="Назад", callback_data="back_task_level")],
        ]
    )

def getTaskKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="question1", callback_data="question1")],
            [InlineKeyboardButton(text="question2", callback_data="question2")],
            [InlineKeyboardButton(text="question3", callback_data="question3")],
            [InlineKeyboardButton(text="Назад", callback_data="back_task")],
        ]
    )

def getTaskInfoKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Главное меню", callback_data="main")],
            [InlineKeyboardButton(text="Назад", callback_data="back_task_info")],
        ]
    )


def getSendQuestionKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="back_send_question"),
             InlineKeyboardButton(text="Главное меню", callback_data="main")],
        ]
    )

def getSubmitTaskKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Главное меню", callback_data="main")],
            [InlineKeyboardButton(text="Назад", callback_data="back_submit_task")],
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
            [InlineKeyboardButton(text="Назад", callback_data="back_up_chracter")],
        ]
    )

def getCharacterInfoKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Главное меню", callback_data="main")],
            [InlineKeyboardButton(text="Назад", callback_data="back_character_info")],
        ]
    )
