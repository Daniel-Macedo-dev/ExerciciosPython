nomes = []
for _ in range(5):
    nome = input("Digite um nome: ")
    nomes.append(nome)
print(nomes)

indice = int(input("Digite um número entre 0 e 4 para remover um nome: "))
if 0 <= indice < len(nomes):
    removido = nomes.pop(indice)
    print(f"Nome removido: {removido}")
else:
    print("Índice inválido.")