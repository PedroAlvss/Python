i = 1
cont = 0
print("Digite um número:")
num = int(input())

while i <= num:
    if num % i == 0:
        cont += 1
    i += 1

if cont == 2:
    print("O numero", num, "é primo!")
else:
    print("O numero", num, "não é primo!")