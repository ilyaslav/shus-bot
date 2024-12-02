from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.repository import Repository
from datetime import date
from service.attachmentService import AttachmentService

class TaskService:

    @staticmethod
    async def getTaskKeyboard(level: str) -> InlineKeyboardMarkup:
        tasks = await Repository.getTasksByTypeAndDate(level, date=date.today())
        keyboard_x = []
        for task in tasks:
            keyboard_y  = [(InlineKeyboardButton(text=task.button_name, callback_data=task.key_word))]
            keyboard_x.append(keyboard_y)
        keyboard_y  = [(InlineKeyboardButton(text="Назад", callback_data="get_task"))]
        keyboard_x.append(keyboard_y)

        return InlineKeyboardMarkup(inline_keyboard = keyboard_x)

    @staticmethod
    async def getTask(key_word: str):
        task = await Repository.getTaskById(key_word)
        text = task.text
        type = task.attachment_type
        level = task.type
        attachments = None
        if type == "doc":
            attachments = AttachmentService.getDocuments(task.attachments)
        elif type == "img":
            attachments = AttachmentService.getMediagroup(task.attachments)
        return text, type, attachments, level
