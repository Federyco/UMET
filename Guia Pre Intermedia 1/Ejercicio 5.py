# Ejercicio 5
# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores),
# y posterior ordene los elementos de menor a mayor.
import random
x=int(0)
lista=[]
def make_me_random():
    x=random.randint(0,500)
    lista.append(x)
    for x in range(0,9):
        x=random.randint(0,500)
        lista.append(x)
    lista.sort()
    print(lista)


make_me_random()
