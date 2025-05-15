# Manipulação de String 8
# Autor: Daniel Macedo Silva

palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
substituto = input("Digite um caractere para substituir as vogais: ")
cont = sum(1 for c in palavra if c in vogais)
nova_palavra = ''.join([substituto if c in vogais else c for c in palavra])

print("Número de vogais:", cont)
print("Nova palavra:", nova_palavra)