#Palabras plurales
# variables
cadena=0
# declaración de la función con parametro
def plural_singular(cadena):
    if(cadena[-1] == str("s")):
        print("Es plural")
    else:
        print("Es singular")


# ingreso
cadena = input("Ingrese una palabra: ")
#llamada a la función con parametro
plural_singular(cadena)