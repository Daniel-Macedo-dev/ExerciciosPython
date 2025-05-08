# Desafio 1
# Autor: Daniel Macedo Silva

numero = int(input("Digite um número inteiro: "))

print("Escolha a base de conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

opcao = input("Sua opção: ")

if opcao == "1":
    print(f"{numero} em binário é {bin(numero)[2:]}")
elif opcao == "2":
    print(f"{numero} em octal é {oct(numero)[2:]}")
elif opcao == "3":
    print(f"{numero} em hexadecimal é {hex(numero)[2:]}")
else:
    print("Opção inválida.")
