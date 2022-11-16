# Find cyrillic symbols

string = input("Введите текст:")

print(string)
for symbol in string:
    if (symbol.upper() >= 'А' ) and (symbol.upper() <= 'Я'):
        print('-', end ='')
    else:
        print(' ', end ='')