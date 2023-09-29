from random import random

# Matrizes são basicamente lista aninhadas porém todas as listas tem o mesmo tamanho

# A = [[1,2,3],
#     [4,5,6],
#     [7,8,9]]

# print(A[0][2]) # Neste caso o primeiro [] representa a linha e o segundo [] a coluna


# Aqui vamos mostrar o elementos de uma matriz um por um e para isso utilizamos dois for
# for l in range(0,len(A)):
#     for c in range(0, len(A[l])):
#         print(A[l][c])

m = []

for linha in range(10):
    linhas = []
    for coluna in range(15):
        linhas.append(random() * 100)
    m.append(linhas)

for l in range(0,len(m)):
    for c in range(0, len(m[l])):
        print(m[l][c], end=" ")
    print()

for linha in range(0,len(m)):
    print(m[linha][0])