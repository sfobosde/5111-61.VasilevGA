# Функция генерации паролей.

import random

def generate_random_password() -> str:
    
    # Левая граница используемых кодов.
    left_limit_code = 33

    # Правая граница используемых кодов.
    right_limit_code = 126

    # Длина пароля от 7 до 10 символов.
    password_lenght = random.randint(7, 10)

    # Пароль из символов.
    password_char = ""

    # Генерация кодов символов.
    for i in range(0, password_lenght):
        password_char += chr(random.randint(left_limit_code, right_limit_code))

    return password_char

print(generate_random_password())