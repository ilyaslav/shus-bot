from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    TOKEN: str
    CRYPT_KEY: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def TOKEN(self):
        return self.TOKEN

    @property
    def CRYPT_KEY(self):
        return self.CRYPT_KEY

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()
