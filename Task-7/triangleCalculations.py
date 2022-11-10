import math

leg_a = int(input("Введите значение катета:"))
leg_b = int(input("Введите значение катета:"))

hypotenuse = lambda a,b: math.sqrt(leg_a ** 2 + leg_b ** 2)

print(hypotenuse(leg_a, leg_b))