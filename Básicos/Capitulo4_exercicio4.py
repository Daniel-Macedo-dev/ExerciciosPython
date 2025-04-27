nome_completo = input("Digite seu nome completo: ").split()
if len(nome_completo) > 1:
    print(f"Seu primeiro sobrenome é: {nome_completo[1]}")
else:
    print("Você não digitou um nome completo.")