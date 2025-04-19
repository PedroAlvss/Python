print("Digite a primeira nota:")
a = int(input())
print("Digite a segunda nota:")
b = int(input())
print("Digite a terceira nota:")
c = int(input())

media = (a + b + c) / 3

if media < 6:
    print("Aluno reprovado!! HAHA animal tirou", media)
else:
    print("Aluno aprovado!, com a media", media)