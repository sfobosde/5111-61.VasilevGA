simple_text = "Составить программу, которая проверяет является ли введенное с клавиатуры слово «палиндромом» (пример, «казак»)."

code_key = "ergfgds"

coded_text = ""
index = 0

for symbol in simple_text:
    coded_text += chr(ord(code_key[index]) + ord(symbol))
    print(ord(symbol), end = ' ')
    index = index + 1 if (len(code_key) < index) else 0

print(coded_text)