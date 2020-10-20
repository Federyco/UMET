# Ejercicio 16
# Vamos a crear un programa que tenga el siguiente menú:
# *    Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista. x
# *    Añadir número de la lista en una posición: Me pide un número y una posición, x
#          y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
# *    Longitud de la lista: te muestra el número de elementos de la lista. x
# *    Eliminar el último número: Muestra el último número de la lista y lo borra. x
# *    Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella x
#           (la posición se pide a partir de 1).
# *    Contar números: Te pide un número y te dice cuantas apariciones hay en la lista. x
# *    Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
# *    Mostrar números: Muestra los números de la lista
# *    Salir
# Fuente -> https://www.youtube.com/watch?v=LUoKlnK5wcc

global lista
lista=[0, 1, 3, 5, 7, 8, 15, 45,15]
global add_to_lista
add_to_lista=int(0)
ingreso=int(0)
location=int(0)
continuar=bool(True)

def add_to_last():
    add_to_lista=input("Ingrese el número que desea agregar al final de la lista: ")
    lista.append(add_to_lista)

def add_to_position():
    print("En este caso el sistema requerira de una posición y un valor. Ingreselos separados por un espacio")
    print("Ejemplo 5 48 -> Esto agrega en la pos 5 el valor 48")
    location, add_to_lista=input("Ingrese el número que desea agregar al final de la lista: ").split()
    lista.insert(int(location), int(add_to_lista))

def show_it_to_me():
    # le resto 1 porque contabiliza el espacio del 0, y de esta forma no lo hace
    print(len(lista) - 1)
    
def delete_last_one():
    print(lista[-1])
    x = lista[-1]
    lista.remove(x)

def delete_in_this_position():
    print("Lista Actual  " + str(lista[1:len(lista)]))
    print("En este caso el sistema requerira de una posición.")
    print("Si existe un valor en esa posición, este sera eliminado.")
    location=input("Ingrese la posición que desea eliminar: ")
    lista.remove(lista[int(location)])

def im_on_the_list():
      print("Lista Actual  " + str(lista[1:len(lista)]))
      location=input("Ingrese el valor que desea buscar: ")
      print("El número " + str(location) + " aparece " + str(lista.count(int(location))) + " ves/veces, en la lista.")
    
def where_am_i():
      # Fuente - > https://www.youtube.com/watch?v=8a9wwsUT-o4
      x=int(0)
      print("Lista Actual  " + str(lista[1:len(lista)]))
      location=input("Ingrese el valor que desea buscar: ")
      lista2 =[i for i in range(len(lista)) if lista[i] == int(location)]
      print(lista2)

def show_me_my_list():
    print("Lista Actual  " + str(lista[1:len(lista)]))

while continuar:
        print("Menu paleozoico")
        print("Ingrese 1 para añadir un número al final de la lista.")
        print("Ingrese 2 para añadir un número en una posición deseada.")
        print("Ingrese 3 para visualizar la longitud actual de la lista.")
        print("Ingrese 4 para mostrar el último valor de la lista, y borrarlo.")
        print("Ingrese 5 para eliminar un valor alojado en una pos x de la lista.")
        print("Ingrese 6 para chequear cuantas veces aparece un número en la lista.")
        print("Ingrese 7 para chequear en que posiciones aparece el número ingresado en la lista.")
        print("Ingrese 8 para mostrar los valores de la lista.")
        print("Ingrese 0 para salir.")
        ingreso = int(input("Su elección: "))
        if(ingreso == 0 or ingreso > 8):
            print("Saliendo del sistema")
            continuar = False
            break
        elif(ingreso == 1):
            add_to_last()
        elif(ingreso == 2):
            add_to_position()
        elif(ingreso == 3):
            show_it_to_me()
        elif(ingreso == 4):
            delete_last_one()
        elif(ingreso == 5):
            delete_in_this_position()
        elif(ingreso == 6):
            im_on_the_list()
        elif(ingreso == 7):
            where_am_i()
        elif(ingreso == 8):
            show_me_my_list()
