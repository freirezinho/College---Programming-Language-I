print("Olá, vamos calcular sua média!")
print("\nVamos começar com as suas Atividades Contínuas.")
print("\nUtilizaremos suas quatro melhores notas...")

ac_1 = float(input("\nQual foi sua nota na primeira AC ? \n> AC 1: "))
ac_2 = float(input("Qual foi sua nota na segunda AC ? \n> AC 2: "))
ac_3 = float(input("Qual foi sua nota na terceira AC ? \n> AC 3: "))
ac_4 = float(input("Qual foi sua nota na quarta AC ? \n> AC 4: "))
# ac_5 = float(input("Qual foi sua nota na primeira AC ? \n> AC 5: "))

print("\nAgora, qual foi sua nota da prova?")
prova = float(input("Quanto você atingiu na prova ? \n> Nota da prova: ")) / 2
print("\nCalculando a média...")

media_acs = ((ac_1 + ac_2 + ac_3 + ac_4) / 4) / 2
# print(media_acs)
media_final = media_acs + prova
print("\nSua média final será...", media_final)