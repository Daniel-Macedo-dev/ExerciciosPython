numeros_modificados = []
for _ in range(10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        num += 1
    numeros_modificados.append(num)
print(numeros_modificados)