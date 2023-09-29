m = []

linha1 = []
linha2 = []
linha3 = []

for i in range(3):
    a = int(input("Digite um número: "))
    linha1.append(a)
    b = int(input("Digite um número: "))
    linha2.append(b)
    c = int(input("Digite um número: "))
    linha3.append(c)

m.append(linha1)
m.append(linha2)
m.append(linha3)

diagonal = linha1[0] + linha2[1] + linha3[2]

print(m)
print(diagonal)