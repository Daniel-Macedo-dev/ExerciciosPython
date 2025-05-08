# Desafio 3
# Autor: Daniel Macedo Silva

from datetime import date

nascimento = int(input("Ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - nascimento

print(f"\nNascidos em {nascimento} tem {idade} anos em {ano_atual}.")

if idade < 18:
    faltam = 18 - idade
    ano_alistamento = ano_atual + faltam
    print(f"Faltam {faltam} ano(s) para o alistamento.")
    print(f"Seu alistamento será em {ano_alistamento}.")
elif idade == 18:
    print("Pronto para alistamento.")
else: 
    passou = idade - 18
    ano_alistamento = ano_atual - passou
    print(f"Vocé deveria ter se alistado há {passou} ano(s).")
    print(f"Seu alistamento foi em {ano_alistamento}.")