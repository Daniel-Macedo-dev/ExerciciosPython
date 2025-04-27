notas = [float(input("Digite as nota: ")) for _ in range(3)]
media = sum(notas) / 3
print("Aprovado" if media >= 7 else "Reprovado")