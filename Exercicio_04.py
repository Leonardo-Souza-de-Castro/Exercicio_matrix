m = []

linha1 = []
linha2 = []
linha3 = []

soma = 0

for i in range(4):
    a = int(input("Digite um número: "))
    linha1.append(a)
    b = int(input("Digite um número: "))
    linha2.append(b)
    c = int(input("Digite um número: "))
    linha3.append(c)

m.append(linha1)
m.append(linha2)
m.append(linha3)

for i in range(len(linha1)):
    if linha1[i] % 2 !=0:
        soma = soma + linha1[i]
        
for i in range(len(linha2)):
    if linha1[i] % 2 !=0:
        soma = soma + linha2[i]

for i in range(len(linha3)):
    if linha1[i] % 2 !=0:
        soma = soma + linha3[i]

print(m)
print(soma)