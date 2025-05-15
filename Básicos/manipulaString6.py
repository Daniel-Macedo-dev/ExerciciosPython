# Manipulação de String 6
# Autor: Daniel Macedo Silva

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (M/F): ").upper()
idade = int(input("Digite sua idade: "))

if sexo == "F" and idade < 25:
    print(nome, "- ACEITA")
else:
    print("NÃO ACEITA")