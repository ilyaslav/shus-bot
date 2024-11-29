from cryptography.fernet import Fernet

class CryptService:

    @staticmethod
    def encrypt(message: str, key) -> str:
        fernet = Fernet(key)
        encMessage = fernet.encrypt(message.encode())
        return encMessage

    @staticmethod
    def decrypt(message: str, key) -> str:
        fernet = Fernet(key)
        decMessage = fernet.decrypt(message).decode()
        return decMessage

    @staticmethod
    def generate_key() -> str:
        key = Fernet.generate_key()
        return key
