print("Digite um valor para A: ")
a = int(input())
print("Digite um valor para B: ")
b = int(input())

if a > b:
    print("O número A:", a, "é maior do que B:", b)
elif a == b:
    print("Os números são iguais!")
else:
    print("O número B:", b, "é maior do que A:", a)