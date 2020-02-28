import math

print("Olá, vamos calcular a área de um círculo!")
radius = float(input("> Qual o raio do círculo que vamos calcular? \n> Raio: "))
area = 3.14 * math.pow(radius, 2)
print("\n> A área é", area)