from base64 import b64encode, b64decode
from simplecrypt import encrypt, decrypt


<<<<<<< Updated upstream
class Converter():
    def __init__(self, password):
        self.password = password

    def encrypt(self, plain_text):
        return encrypt(self.password, b64encode(plain_text[::-1]))
=======
class Converter:

    @staticmethod
    def encrypt(plain_text, password):
        return encrypt(password, b64encode(plain_text[::-1]))
>>>>>>> Stashed changes

    @staticmethod
    def decrypt(cyfred_text, password):
        return b64decode(decrypt(password, cyfred_text))[::-1]


