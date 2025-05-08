# Desafio 8
# Autor: Daniel Macedo Silva

import random

opcoes = ["Pedra", "Papel", "Tesoura"]

escolha_jogador = input("Escolha: Pedra, Papel ou Tesoura: ").strip().capitalize()

if escolha_jogador not in opcoes:
    print("Opção inválida. Escolha Pedra, Papel ou Tesoura.")
else:
    escolha_computador = random.choice(opcoes)

    print(f"\nVocê escolheu: {escolha_jogador}")
    print(f"O computador escolheu: {escolha_computador}")

    if escolha_jogador == escolha_computador:
        print("Empate!")
    elif (escolha_jogador == "Pedra" and escolha_computador == "Tesoura") or \
         (escolha_jogador == "Papel" and escolha_computador == "Pedra") or \
         (escolha_jogador == "Tesoura" and escolha_computador == "Papel"):
        print("Você venceu!")
    else:
        print("O computador venceu!")
