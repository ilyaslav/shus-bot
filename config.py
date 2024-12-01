from pydantic_settings import BaseSettings, SettingsConfigDict
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    TOKEN: str
    CRYPT_KEY: str

    LEVEL1_PHOTO: str
    LEVEL2_PHOTO: str
    LEVEL3_PHOTO: str
    LEVEL4_PHOTO: str
    LEVEL5_PHOTO: str
    LEVEL6_PHOTO: str
    LEVEL7_PHOTO: str
    LEVEL8_PHOTO: str
    LEVEL9_PHOTO: str
    LEVEL10_PHOTO: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def TOKEN(self):
        return self.TOKEN

    @property
    def CRYPT_KEY(self):
        return self.CRYPT_KEY

    @property
    def LEVEL1_PHOTO(self):
        return self.LEVEL1_PHOTO
    @property
    def LEVEL2_PHOTO(self):
        return self.LEVEL2_PHOTO
    @property
    def LEVEL3_PHOTO(self):
        return self.LEVEL3_PHOTO
    @property
    def LEVEL4_PHOTO(self):
        return self.LEVEL4_PHOTO
    @property
    def LEVEL5_PHOTO(self):
        return self.LEVEL5_PHOTO
    @property
    def LEVEL6_PHOTO(self):
        return self.LEVEL6_PHOTO
    @property
    def LEVEL7_PHOTO(self):
        return self.LEVEL7_PHOTO
    @property
    def LEVEL8_PHOTO(self):
        return self.LEVEL8_PHOTO
    @property
    def LEVEL9_PHOTO(self):
        return self.LEVEL9_PHOTO
    @property
    def LEVEL10_PHOTO(self):
        return self.LEVEL10_PHOTO

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()
dp = Dispatcher()
bot = Bot(token=settings.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
