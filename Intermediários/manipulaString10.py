# Manipulação de String 10
# Autor: Daniel Macedo Silva

texto = input("Digite uma frase para criptografar: ")
resultado = ""
for char in texto:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        resultado += chr((ord(char) - base + 3) % 26 + base)
    else:
        resultado += char
        
print("Criptografado:", resultado)