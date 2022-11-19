# Find cyrillic symbols

string = input("Введите текст:")

print(string)
for symbol in string.upper():
    if (symbol >= 'А') and (symbol <= 'Я'):
        print('-', end='')
    else:
        print(' ', end='')
