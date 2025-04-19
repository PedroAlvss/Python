cont = 0
word = input("Digite uma palavra: ")

vogais = "aeiouAEIOU"

for letra in word:
    if letra in vogais:
        cont += 1

print("A palavra",word,"possui",cont,"vogais")