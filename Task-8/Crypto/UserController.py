import random

class User_Controller:
    private_key = ""
    public_key = ""

    def __init__(self):
        for i in range(0, random.randint(127, 255)):
            self.private_key += chr(random.randint(33,127))
        print(self.private_key)

    def code_text(self, simple_text) -> str:
        coded_text = ""
        index = 0
        for symbol in simple_text:
            coded_text += chr(ord(self.private_key[index]) + ord(symbol))
            index = index + 1 if (len(self.private_key) < index) else 0
        return coded_text

    def send_message(self, message):
        return (self.code_text(message), self.private_key)

    def encode_text(self, crypted_message: tuple):
        crypted_text = crypted_message[0]
        key = crypted_message[1]
        encrypted_text = ""
        index = 0

        for symbol in crypted_text:
            encrypted_text += chr(ord(symbol) - ord(key[index]))
            index = index + 1 if (len(self.private_key) < index) else 0

        return encrypted_text