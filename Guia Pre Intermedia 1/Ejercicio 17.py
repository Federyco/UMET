# Ejercicio 17
# Crear un programa que añada números a una lista hasta que introducimos un número negativo.
# A continuación debe crear una nueva lista igual que la anterior pero eliminando los números
# duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.
# Fuente -> https://www.youtube.com/watch?v=dQnO4hOPbTw

lista1=[]
lista2=[]
ingreso_lista1=int(0)


while (int(ingreso_lista1) >= int(0)):
    ingreso_lista1=input("Ingrese un valor positivo: ")
    if(int(ingreso_lista1) >= int(0)):
        lista1.append(ingreso_lista1)    
    else:
        print("Ha ingresado un valor negativo")
        print("Saliendo del sistema")
        dup_items = set()
        for x in lista1:
            if x not in dup_items:
                lista2.append(x)
                dup_items.add(x)
        print(lista1)
        print(dup_items)