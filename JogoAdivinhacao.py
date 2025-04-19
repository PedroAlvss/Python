import random
print("---JOGO DE ADIVINHAÇÃO---")

adivinha = random.randint(0, 10)

num = int(input("Chuta um número de 1 a 10: "))

if adivinha == num:
    print("UAU parabéns, você acertou")
else:
    print("VISH você errou, tente novamente :)")
    print("O número era", adivinha)
