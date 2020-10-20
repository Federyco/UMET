# Ejercicio 4
# Programa que declare una lista y la vaya llenando de números hasta que
# introduzcamos un número negativo. Entonces se debe imprimir el vector
# (sólo los elementos introducidos).
# FUENTE -> https://www.youtube.com/watch?v=3r2XFtLZCF4
lista=[]
ingreso=int(input("Ingrese un valor: "))
while ingreso > 0:
        lista.append(ingreso)
        ingreso=int(input("Ingrese un valor: "))
print(lista)

