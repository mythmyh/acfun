import rsa
from binascii import b2a_hex,a2b_hex


class rsaCrpt():
    def __init__(self, publickey, prikey):
        self.publickey = publickey
        self.prikey = prikey

    def encrypt(self, text):
        self.ciphertext = rsa.encrypt(text.encode(), self.publickey)
        return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        decrypt_text = rsa.decrypt(a2b_hex(text), self.prikey)
        return decrypt_text
