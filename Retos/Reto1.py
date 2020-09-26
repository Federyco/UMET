# Reto 1: Números positivos o negativos
#variables
numero=int(0)
# definición función que revisa los números positivos
def es_positivo(numero):
    while (numero <= 10 and numero >= -10):
        if(int(numero) >= 0):
            #salida
            print("Es positivo")
            break
    else:
        #salida
        print("Valor fuera de rango")



# definición función que revisa los números negativos
def es_negativo(numero):
    while (numero <= 10 and numero >= -10):
        if(int(numero) <0):
            #salida
            print("-")
            break
    else:
        #salida
        print("Valor fuera de rango")

# ingreso
numero=int(input("Ingrese un número: "))
if(int(numero) < 0):
    es_negativo(numero)
else:
    es_positivo(numero)