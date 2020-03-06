celsius = int(input("Qual a temperatura para converter? \n > Temperatura: "))

def farenheitConversion(temperature: int) -> int:
    return (temperature * 9/5) + 32

print("A temperatura é: ", farenheitConversion(celsius))
input("Pressione o enter para terminar o programa...")