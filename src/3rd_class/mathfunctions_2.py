import math

a = int(input("Defina o primeiro número\n > "))
b = int(input("Defina o segundo número\n > "))
y = int(input("Defina o terceiro número\n > "))

firstElement = 2 * b
secondElement = a + b

print("Calculando...")

x = y + math.sqrt(firstElement / secondElement)

print("O resultado da fórmula é ", y)