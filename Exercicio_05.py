from random import random

m = []

m_transposta = []

for linha in range(10):
    linhas = []
    for coluna in range(5):
        linhas.append(int(random() * 10))
    m.append(linhas)


count = 0
count_2 = 0
linha = []
while(True):
    linha.append(m[count][count_2])
    count += 1
    
    if count > 9:
        m_transposta.append(linha [:])
        count = 0
        count_2 += 1
        linha.clear()

    if count_2 > 4:
        break


print(m)
print(m_transposta)