# Desafio 7
# Autor: Daniel Macedo Silva

preco_normal = float(input("Digite o preço normal do produto: R$ "))
print("\nCondições de pagamento:")
print("1 - À vista em dinheiro (10% de desconto)")
print("2 - À vista no cartão (5% de desconto)")
print("3 - Em até 2x no cartão (Preço normal)")
print("4 - 3x ou mais no cartão (20% de juros)")

opcao = int(input("\nEscolha a opção de pagamento: "))

if opcao == 1:
    preco_final = preco_normal * 0.90
    print(f"\nPreço final: R$ {preco_final:.2f} (10% de desconto)")
elif opcao == 2:
    preco_final = preco_normal * 0.95
    print(f"\nPreço final: R$ {preco_final:.2f} (5% de desconto)")
elif opcao == 3:
    preco_final = preco_normal
    print(f"\nPreço final: R$ {preco_final:.2f} (Preço normal)")
elif opcao == 4:
    preco_final = preco_normal * 1.20
    print(f"\nPreço final: R$ {preco_final:.2f} (20% de juros)")
else:
    print("\nOpção inválida.")