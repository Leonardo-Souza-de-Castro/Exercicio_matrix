from random import random

inteiros = []
reais = []
string = ["olá", "teste", "animais", "a", "b", "c", "d"]
complexos = [1+5j, 7+6j, 5+7j, 6+2j, 8+1j]

completa = []


for i in range(0,10):
    inteiros.append(int(random() * 100))
    reais.append(random() * 100)

completa.append(inteiros [:]),
completa.append(reais [:])
completa.append(string [:])
completa.append(complexos [:])

inteiros.clear()
reais.clear()
string.clear()
complexos.clear()

print(completa) #A lista completa é uma lista aninhada (uma lista de listas)