# Ejercicio 7
# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno,
# pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.
x=int(0)
y=int(0)
lista=[]
lista1=[]
lista2=[]
ingreso_lista=int(0)
ingreso_lista1=int(0)


# funcion que se encarga de pedir al usuario los valores que seran parte de las listas
# utilizo un contador para limitar el bucle de cada lista
# finalmente devuelve los valores de las listas
def make_me_random():
    limit=int(1)
    limit2=int(1)
    while limit <=5:
        ingreso_lista=int(input("Ingrese un valor, y presiona enter: "))
        lista.append(ingreso_lista)
        limit = limit +1
    while limit2 <=5:
        ingreso_lista1=int(input("Ingrese un valor, y presiona enter: "))
        limit2 = limit2 + 1
        lista1.append(ingreso_lista1)
    return(lista, lista1)

# esta funcion toma los valores generados en la funcion anterior
# y los suma entre si dando como resultado la lista2
# como extra la lista se entrega ordenada de forma ascendente.
def suma(lista, lista1):
    lista2=lista + lista1
    lista2.sort()
    return print(lista2)
    


make_me_random()
suma(lista, lista1)