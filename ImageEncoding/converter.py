from base64 import b64encode, b64decode
from simplecrypt import encrypt, decrypt

class Converter:

    @staticmethod
    def encrypt(plain_text, password):
        return encrypt(password, b64encode(plain_text[::-1]))
        return encrypt(self.__password, b64encode(plain_text[::-1]))

    @staticmethod
    def decrypt(cyfred_text, password):
        return b64decode(decrypt(password, cyfred_text))[::-1]
