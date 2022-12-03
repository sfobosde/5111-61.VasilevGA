# Возведение числа в степеньЫ
def calculations():
    a = input()
    b = input()

    if (b == 0):
        print("Нельзя вводить 0")

    while b == 0:
        b = input()

    if (b == 1):
        c = a
    if (b == 2):
        c = a*a
    if (b == 3):
        c = a*a*a
    if (b == 4):
        c = a*a*a*a
    # И так до бесконечности

    print(c)

calculations()