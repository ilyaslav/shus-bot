from database.repository import Repository
from database.models import UserBase
from config import settings

MAX_FEED = 10
MAX_PLAY = 10
MAX_SLEEP = 1
SPEAK_COST = 5

class UserService:

    @staticmethod
    async def checkCodeWord(user: UserBase, text: str) -> str:
        key_word, reward = text.split(":")
        if not bool(await Repository.getTaskById(key_word)):
            return "Неверный код"

        if not bool(await Repository.getUserTaskByKeyWordAndUserId(key_word, user.id)):
            await Repository.addUserTask(user.id, key_word, int(reward))
            user.score += int(reward)
            await Repository.updateUser(user)
            return "Код принят"
        else:
            return "Баллы за этот код уже начислены"

    @staticmethod
    async def rename(user: UserBase, new_name: str):
        user.name = new_name
        user.rename_event = False
        await Repository.updateUser(user)

    @staticmethod
    async def setRenameEvent(user: UserBase, event: bool):
        user.rename_event = event
        await Repository.updateUser(user)

    @staticmethod
    def checkLevel(user: UserBase) -> int:
        levels = [0, 6, 12, 24, 60, 100, 160, 240, 370, 500]
        i = 0
        for level in levels:
            if user.upgrades >= level:
                i+=1
        return i

    @staticmethod
    async def feed(user: UserBase) -> str:
        if user.feed == MAX_FEED:
            return "Ваш активист сыт!"
        if user.score > user.feed:
            user.feed += 1
            user.score -= user.feed
            user.upgrades += user.feed
            user.level = UserService.checkLevel(user)
            await Repository.updateUser(user)
            return "«Спасибо, большое! Было очень вкусно!»"
        return "Не хватает баллов для выполнения действия"

    @staticmethod
    async def play(user: UserBase) -> str:
        if user.play == MAX_PLAY:
            return "Ваш активист устал и пока не хочет играть!"
        if user.score > user.play:
            user.play += 1
            user.score -= user.play
            user.upgrades += user.play
            user.level = UserService.checkLevel(user)
            await Repository.updateUser(user)
            return "Уровень счастья увеличился"
        return "Не хватает баллов для выполнения действия"

    @staticmethod
    async def sleep(user: UserBase) -> str:
        if user.sleep == MAX_SLEEP:
            return "Ваш активист пока не хочет спать!"
        if user.score > user.sleep:
            user.sleep += 1
            user.score -= user.sleep
            user.upgrades += user.sleep
            user.level = UserService.checkLevel(user)
            await Repository.updateUser(user)
            return "Ваш активист уснул"
        return "Не хватает баллов для выполнения действия"

    @staticmethod
    async def speak(user: UserBase) -> str:
        if user.score > SPEAK_COST:
            user.speak += 1
            user.score -= SPEAK_COST
            user.upgrades += SPEAK_COST
            user.level = UserService.checkLevel(user)
            await Repository.updateUser(user)
            return "Личные качества активист успешно прокачены!"
        return "Не хватает баллов для выполнения действия"

    @staticmethod
    async def getUserInfo(user: UserBase) -> list[str]:
        match user.level:
            case 1:
                photo = settings.LEVEL1_PHOTO
            case 2:
                photo = settings.LEVEL2_PHOTO
            case 3:
                photo = settings.LEVEL3_PHOTO
            case 4:
                photo = settings.LEVEL4_PHOTO
            case 5:
                photo = settings.LEVEL5_PHOTO
            case 6:
                photo = settings.LEVEL6_PHOTO
            case 7:
                photo = settings.LEVEL7_PHOTO
            case 8:
                photo = settings.LEVEL8_PHOTO
            case 9:
                photo = settings.LEVEL9_PHOTO
            case 10:
                photo = settings.LEVEL10_PHOTO

        text = """Данные персонажа {name}:

<b>Уровень:</b> {level}
<b>Сытость:</b> {feed}
<b>Счастье:</b> {play}
<b>Личные качества:</b> {speak}
<b>Бодрость:</b> {sleep}""".format(
    name=user.name,
    level=user.level,
    feed=user.feed,
    play=user.play,
    speak=user.speak,
    sleep=user.sleep
    )
        return text, photo
