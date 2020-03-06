import math

a = int(input("Defina o primeiro número\n > "))
b = int(input("Defina o segundo número\n > "))
x = int(input("Defina o terceiro número\n > "))

firstElement = a ** 2
secondElement = 3 * b
thirdElement = x ** 3

print("Calculando...")

y = (firstElement + math.sqrt(secondElement)) / 5 * thirdElement

print("O resultado da fórmula é ", round(y, 2))