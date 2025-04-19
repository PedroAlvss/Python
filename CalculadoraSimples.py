print("Digite um valor para A")
a = int(input())
print("Digite um valor pra B>:")
b = int(input())
print("\n1- Soma")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")
print("Escolha uma operação:")
symbol = int(input())

if symbol == 1:
    print(a, "+", b, "=", a+b)
elif symbol == 2:
    print(a, "-", b, "=", a-b)
elif symbol == 3:
    print(a, "x", b, "=", a*b)
elif symbol == 4:
    print(a, "/", b, "=", a/b)
else:
    print("Escolha entre 1 e 4!")