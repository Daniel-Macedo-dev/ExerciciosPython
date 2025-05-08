# Desafio 5
# Autor: Daniel Macedo Silva

from datetime import date

ano_nascimento  = int(input("Digite seu ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f"\nO atleta tem {idade} anos.")

if idade <= 9:
    print ("Categoria: Mirim")
elif idade <= 14:
    print("Categoria: INFANTIL")
elif idade <= 19:
    print("Categoria: JUNIOR")
elif idade <= 24:
    print("Categoria: SÊNIOR")
else:
    print("Categoria: MASTER")