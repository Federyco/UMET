# Ejercicio 18
# Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:
#   *   Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
#   *    Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones
#                   de la primera por la segunda en la lista.
#   *    Eliminar: Me pide una cadena, y la elimina de la lista.
#   *    Mostrar: Muestra la lista de cadenas
#   *    Terminar
ingreso=int(1)
continuar=bool(True)
global lista_de_palabras
lista_de_palabras=["perro",
                                        "gato",
                                        "vaca",
                                        "cerdo",
                                        "caballo",
                                        "yegua",
                                        "oveja",
                                        "mono",
                                        "ratón",
                                        "rata",
                                        "tigre",
                                        "conejo",
                                        "dragón",
                                        "ciervo",
                                        "rana",
                                        "león",
                                        "jirafa",
                                        "elefante",
                                        "pájaro",
                                        "gallina",
                                        "gorrión",
                                        "cuervo",
                                        "aguila",
                                        "halcón",
                                        "pez",
                                        "camarón",
                                        "serpiente",
                                        "sardina",
                                        "atún",
                                        "calamar",
                                        "pulpo",
                                        "serpiente",
                                        "bicho",
                                        "mariposa",
                                        "polilla",
                                        "saltamontes",
                                        "araña",
                                        "mosca",
                                        "mosquito",
                                        "cucaracha",
                                        "caracol",
                                        "babosa",
                                        "lombriz",
                                        "marisco",
                                        "molusco",
                                        "lagarto",
                                        "serpiente",
                                        "cocodrilo"]
def contame():
    global ingreso_lista_palabras
    ingreso_lista_palabras=str(" ")
    ingreso_lista_palabras=str(input("Ingrese un animal: "))
    print("El animal " + str(ingreso_lista_palabras) + " aparece " + str(lista_de_palabras.count(str(ingreso_lista_palabras))) + " ves/veces en la lista")

def switching():
    global new_key_word
    new_key_word=str(" ")
    ingreso_lista_palabras=str(input("Ingrese un animal: "))
    # en holder guardo la pos de la palabra que deseo encontrar para cambiar
    holder=lista_de_palabras.index(str(ingreso_lista_palabras))
    new_key_word=str(input("Ingrese el nuevo animal: "))
    # insert pide (pos, y nuevo valor)
    lista_de_palabras.insert(holder, new_key_word)
    
    

def delete_me():
        ingreso_lista_palabras=str(input("Ingrese un animal: "))
        lista2 =[i for i in range(len(lista_de_palabras)) if lista_de_palabras[i] == str(ingreso_lista_palabras)]
        for x in range (0,len(lista2)):
            lista_de_palabras.remove(ingreso_lista_palabras)
        print(str(ingreso_lista_palabras) + " ha sido eliminado de la lista satisfactoriamente.")
        
        
    
def show_them_to_me():
    n= int(0)
    lista_de_palabras.sort()
    for x in range(0, len(lista_de_palabras)):
        print(lista_de_palabras[n])
        n = n+ 1

while (continuar):
    print("Sistema de strings 1.0")
    print("Ingrese 1 para ingresar una cadena, y compararla con la lista creada previamente.")
    print("Ingrese 2 para intercambiar cadenas, por una nueva ingresada por teclado.")
    print("Ingrese 3 para borrar un animal de la lista.")
    print("Ingrese 4 para mostrar la lista completa de animales.")
    print("Ingrese 0 para Salir")
    ingreso=int(input("Su elección: "))
    if(ingreso == 0):
        print("Saliendo del sistema")
        continuar=False
        break
    elif(ingreso == 1):
        contame()
    elif(ingreso == 2):
        switching()
    elif(ingreso == 3):
        delete_me()
    elif(ingreso == 4):
        show_them_to_me()