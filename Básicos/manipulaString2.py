# Manipulação de String 2
# Autor: Daniel Macedo Silva

letra = input("Digite uma letra maiúscula: ")
minuscula = chr(ord(letra)+32) if 'A' <= letra <= 'Z' else letra
print("Letra minúscula:", minuscula)