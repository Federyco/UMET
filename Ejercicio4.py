#Suma los números pares e impares
#variables
continuar=bool(True)

def calculos_varios():
    #variables
    error=int(0)
    numero=[0,0,0,0,0,0,0,0,0,0]
    holder_par=int(0)
    holder_impar=int(0)
    pos=int(0)
    #entrada de datos
    numero[0], numero[1], numero[2], numero[3], numero[4], numero[5], numero[6], numero[7], numero[8], numero[9]=input("Ingrese un numero: ").split()
    for x in range (0,10):
        # validación, se requiere que los números ingresados previamente
        # estén dentro del rango 0 - 100
        if(int(numero[pos]) >= 0 and int(numero[pos]) <=100):
            if (int(numero[pos]) % 2 == 0):
                    holder_par= holder_par+int(numero[pos])
                    pos = pos + 1
            else:
                    holder_impar = holder_impar + int(numero[pos])
                    pos = pos + 1
        else:
            print("valor fuera de rango " + str(numero[pos]) + " no es aceptado")
            error = 1
            break
    if(error == 0):
        # salida de datos
        print("La suma total de los números pares es: " + str(holder_par))
        print("La suma total de los números impares es : " + str(holder_impar))
    else:
        print("Saliendo del sistema, ingrese nuevamente")


def vaciado_de_variables():
        pos=0
        holder_par=0
        holder_impar=0
        
#logica
while continuar:
        calculos_varios()
        vaciado_de_variables()
        continuar=False