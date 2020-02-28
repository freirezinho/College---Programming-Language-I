import math

print("Olá, vamos calcular a o dobro da área de um quadrado!")
side = float(input("> Qual o lado do quadrado que vamos calcular? \n> Lado: "))
area = math.pow(side, 2)
print("\n> O dobro da área é", area * 2)