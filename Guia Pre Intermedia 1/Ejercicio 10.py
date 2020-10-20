# Ejercicio 10
# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# Carga la tabla con valores numéricos enteros.
# Suma todos los elementos de cada fila y todos los elementos de cada columna
# visualizando los resultados en pantalla.
# Fuente -> https://www.youtube.com/watch?v=nQQcdFJ7Gqg
import random
def llenado_de_listas():
    n=int(0)
    numero_random=int(0)
    global lista1
    global lista2
    global lista3
    global lista4
    global lista5 
    global lista_tabla
    lista1=[]
    lista2=[]
    lista3=[]
    lista4=[]
    lista5=[]
    # fila1, fila2, fila3, fila4, fila5
    lista_tabla=[lista1, lista2, lista3, lista4, lista5]
    # filas
    resul_fila1=int(0)
    resul_fila2=int(0)
    resul_fila3=int(0)
    resul_fila4=int(0)
    resul_fila5=int(0)
    # columnas
    resul_col1=int(0)
    resul_col2=int(0)
    resul_col3=int(0)
    resul_col4=int(0)
    resul_col5=int(0)
    for x in range (0,5):
        numero_random = random.randint(0,50)
        lista1.append(numero_random)
    for x in range (0,5):
        numero_random = random.randint(0,75)
        lista2.append(numero_random)
    for x in range (0,5):
        numero_random = random.randint(0,100)
        lista3.append(numero_random)
    for x in range (0,5):
        numero_random = random.randint(0,125)
        lista4.append(numero_random)
    for x in range (0,5):
        numero_random = random.randint(0,150)
        lista5.append(numero_random)
    for x in range (0,5):
        # suma de filas
        resul_fila1 =  resul_fila1 + lista1[n]
        resul_fila2 =  resul_fila2 + lista2[n]
        resul_fila3 =  resul_fila3 + lista3[n]
        resul_fila4 =  resul_fila4 + lista4[n]
        resul_fila5 =  resul_fila5 + lista5[n]
        n = n+1
        # suma de columnas
        resul_col1 = lista1[0] + lista2[0] + lista3[0]  + lista4[0] + lista5[0]
        resul_col2 = lista1[1] + lista2[1] + lista3[1]  + lista4[1] + lista5[1]
        resul_col3 = lista1[2] + lista2[2] + lista3[2]  + lista4[2] + lista5[2]
        resul_col4 = lista1[3] + lista2[3] + lista3[3]  + lista4[3] + lista5[3]
        resul_col5 = lista1[4] + lista2[4] + lista3[4]  + lista4[4] + lista5[4]


    print("Resultados Obtenidos: ")
    print(" ****** Filas ****** ")
    print("Fila 1 = " + str(resul_fila1))
    print("Fila 2 = " + str(resul_fila2))
    print("Fila 3 = " + str(resul_fila3))
    print("Fila 4 = " + str(resul_fila4))
    print("Fila 5 = " + str(resul_fila5))
    print(" ****** Columnas ****** ")
    print("Columna 1 =" + str(resul_col1))
    print("Columna 2 =" + str(resul_col2))
    print("Columna 3 =" + str(resul_col3))
    print("Columna 4 =" + str(resul_col4))
    print("Columna 5 =" + str(resul_col5))
    ## Debug
    #print(lista_tabla)
llenado_de_listas()
    