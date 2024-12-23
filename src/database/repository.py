import asyncio
import datetime
from sqlalchemy.future import select
from sqlalchemy.sql.expression import update
from sqlalchemy import or_

from database.database import session_factory
from database.models import *

INC = 3
NEED_FEED = 3
NEED_PALY = 3
NEED_SLEEP = 1

class Repository:

    @staticmethod
    async def addUser(user_id: str):
        user = UserBase(
            id = user_id
        )
        async with session_factory() as sf:
            sf.add(user)
            await sf.commit()

    @staticmethod
    async def getUserById(id: str) -> UserBase:
        async with session_factory() as sf:
            user = await sf.get(UserBase, id)
            return user

    @staticmethod
    async def getAllUsers() -> list[UserBase]:
        async with session_factory() as sf:
            users = await sf.execute(
                select(UserBase)
            )
            return users.scalars().all()

    @staticmethod
    async def updateUser(user: UserBase):
        async with session_factory() as sf:
            db_user = await sf.get(UserBase, user.id)
            if user:
                db_user.name = user.name
                db_user.rename_event = user.rename_event
                db_user.score = user.score
                db_user.feed = user.feed
                db_user.play = user.play
                db_user.speak = user.speak
                db_user.sleep = user.sleep
                db_user.level = user.level
                db_user.upgrades = user.upgrades
                await sf.commit()

    @staticmethod
    async def updateScore():
        async with session_factory() as sf:
            await sf.execute(
                update(UserBase)
                .values(score = UserBase.score + INC)
            )
            await sf.commit()

    @staticmethod
    async def updateFeed():
        async with session_factory() as sf:
            await sf.execute(
                update(UserBase)
                .values(feed = 0)
            )
            await sf.commit()

    @staticmethod
    async def updatePlay():
        async with session_factory() as sf:
            await sf.execute(
                update(UserBase)
                .values(play = 0)
            )
            await sf.commit()

    @staticmethod
    async def updateSleep():
        async with session_factory() as sf:
            await sf.execute(
                update(UserBase)
                .values(sleep = 0)
            )
            await sf.commit()

    @staticmethod
    async def checkFeed():
        async with session_factory() as sf:
            await sf.execute(
                update(UserBase)
                .values(score = UserBase.score - INC)
                .filter(UserBase.feed < NEED_FEED)
            )

    @staticmethod
    async def checkPlay():
        async with session_factory() as sf:
            await sf.execute(
                update(UserBase)
                .values(score = UserBase.score - INC)
                .filter(UserBase.play < NEED_PALY)
            )

    @staticmethod
    async def checkSleep():
        async with session_factory() as sf:
            await sf.execute(
                update(UserBase)
                .values(score = UserBase.score - INC)
                .filter(UserBase.sleep < NEED_SLEEP)
            )


    @staticmethod
    async def addTask(key_word: str, type: str, button_name: str, reward: int,
                      attachments: str = None, date: datetime.date = None):
        task = TaskBase(
            key_word = key_word,
            type = type,
            button_name = button_name,
            reward = reward,
            attachments = attachments,
            date = date
        )
        async with session_factory() as sf:
            sf.add(task)
            await sf.commit()

    @staticmethod
    async def getTaskById(key_word: str) -> TaskBase:
        async with session_factory() as sf:
            task = await sf.get(TaskBase, key_word)
            return task

    @staticmethod
    async def getTasksByType(type: str) -> list[TaskBase]:
        async with session_factory() as sf:
            tasks = await sf.execute(
                select(TaskBase)
                .filter(TaskBase.type == type)
            )
            return tasks.scalars().all()

    @staticmethod
    async def getTasksByTypeAndDate(type: str, date: datetime.date) -> list[TaskBase]:
        async with session_factory() as sf:
            tasks = await sf.execute(
                select(TaskBase)
                .filter(TaskBase.type == type)
                .filter(or_(
                    TaskBase.date == date,
                    TaskBase.date == None
                ))
            )
            return tasks.scalars().all()


    @staticmethod
    async def addUserTask(user_id: str, key_word: str, reward: int = 0):
        user_task = UserTaskBase(
            user_id = user_id,
            key_word = key_word,
            reward = reward
        )
        async with session_factory() as sf:
            sf.add(user_task)
            await sf.commit()

    @staticmethod
    async def getAllUserTasks() -> list[UserTaskBase]:
        async with session_factory() as sf:
            user_tasks = await sf.execute(
                select(UserTaskBase)
            )
            return user_tasks.scalars().all()

    @staticmethod
    async def getUserTaskByKeyWordAndUserId(key_word: str, user_id: str) -> UserTaskBase:
        async with session_factory() as sf:
            user_task = await sf.execute(
                select(UserTaskBase)
                .filter(UserTaskBase.user_id == user_id)
                .filter(UserTaskBase.key_word == key_word)
            )
            return user_task.scalars().all()
