# Desafio 2
# Autor: Daniel Macedo Silva

valorCasa = float(input("Valor da casa: R$ "))
salario = float(input("Salário do comprador: R$ "))
anos = int(input("Quantos anos de financiamento? "))

meses = anos * 12
prestacao = valorCasa / meses
limite = salario * 0.30

print(f"\nPara pagar uma casa de R$ {valorCasa:.2f} em {anos} anos, a prestação será de R$ {prestacao:.2f}.")

if prestacao <= limite:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado! A prestação excede 30% do salário.")
