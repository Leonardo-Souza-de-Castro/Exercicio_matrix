from random import random

m = []


for linha in range(12):
    linhas = []
    for coluna in range(12):
        linhas.append(int(random() * 10))
    m.append(linhas)

for i in range(0,12):
    linhas = []
    c = i
    while(True):
        c =+ 1
        linhas.append(m[i][c])

        if c == 11:
            break
    m.append(linhas)

print(m)