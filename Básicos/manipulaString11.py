# Manipulação de String 8
# Autor: Daniel Macedo Silva

palavra = input("Digite uma algo: ")
limpa = ''.join(c.lower() for c in palavra if c.isalnum())
print("É palíndromo" if limpa == limpa[::-1] else "Não é palíndromo")