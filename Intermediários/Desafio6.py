# Desafio 6
# Autor: Daniel Macedo Silva

import math

print("Escolha o tipo de triângulo:")
print("1 - Equilátero")
print("2 - Isósceles")
print("3 - Escaleno")

opcao = int(input("Digite a opção: "))

if opcao == 1:
    lado = float(input("Digite o comprimento do lado: "))
    area = (lado ** 2) * math.sqrt(3) / 4
    print(f"A área do triângulo equilátero é: {area:.2f}")
elif opcao == 2:
    base = float(input("Digite o comprimento da base: "))
    altura = float(input("Digite o comprimento da altura: "))
    area = (base * altura) / 2
    print(f"A área do triângulo isósceles é: {area:.2f}")
elif opcao == 3:
    a = float(input("Digite o comprimento do lado a: "))
    b = float(input("Digite o comprimento do lado b: "))
    c = float(input("Digite o comprimento do lado c: "))
    semi_perimetro = (a + b + c) / 2
    area = math.sqrt(semi_perimetro * (semi_perimetro - a) * (semi_perimetro - b) * (semi_perimetro - c))
    print(f"A área do triângulo escaleno é: {area:.2f}")
else:
    print("Opção inválida.")