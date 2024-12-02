from aiogram.types import InputMediaPhoto

class AttachmentService:

    @staticmethod
    def getMediagroup(attachments: str):
        files = attachments.split(" ")
        mediagroup = []
        for file in files:
            mediagroup.append(InputMediaPhoto(media=file))
        return mediagroup

    @staticmethod
    def getDocuments(attachments: str):
        files = attachments.split(" ")
        return files
