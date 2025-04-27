idade = int(input("Digite sua idade: "))
if idade <= 11:
    print("Criança")
elif idade <= 18:
    print("Adolescente")
elif idade <= 24:
    print("Jovem")
elif idade <= 40:
    print("Adulto")
elif idade <= 60:
    print("Meia Idade")
else:
    print("Idoso")