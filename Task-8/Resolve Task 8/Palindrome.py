# Check is string a palindrome

string = input("Введите слово:").upper()
if string == string[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")