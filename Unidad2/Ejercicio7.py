#Puntos suspensivos
#variables
eleccion=int(0)

# función encargada de tomar el valor, y mediante un ciclo for imprimir los puntos
def puntos_suspensivos(eleccion):
    pack_puntos=str("...")
    for x in range (0, eleccion):
        print(pack_puntos + " ",  end = '')


#salida
print("ingrese el número de veces que se van a imprimir los '...' ")
#entrada
eleccion=int(input("su eleccion: "))
#llamada a la función con pase de parametro
puntos_suspensivos(eleccion)