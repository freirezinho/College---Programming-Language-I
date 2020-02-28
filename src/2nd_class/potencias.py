import math

num = int(input('> Qual número vamos utilizar? \n> Número: '))
double_num = num * 2
triple_num = num * 3
sq_num = int(math.pow(num, 2))

print("\n> O dobro de", num, "é", double_num)
print("> O triplo de", num, "é", triple_num)
print("> O quadro de", num, "é", sq_num)

input("\nAperte enter para encerrar o programa...")