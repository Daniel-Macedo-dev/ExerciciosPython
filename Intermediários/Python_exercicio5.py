def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    numero = int(input("Digite um número: "))
    idade = int(input("Digite sua idade: "))
    print(idade >= 18)
    print("É primo" if eh_primo(numero) else "Não é primo")
    opcao = input("Deseja continuar? (s/n): ")
    if opcao.lower() != 's':
        break