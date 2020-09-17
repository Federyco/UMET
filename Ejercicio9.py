# Criptografía
# declararión de la función sin parametros
def calculo_por_angulos():
    # variables
    abecedario=("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    desgradificacion=[0,0,0,0]
    grados=[0,0,0,0]
    agrupacion=str(" ")
    #salida
    print("Ingrese hasta 4 valores")
    print("Para separarlos utilize el espacio ")
    #ingreso
    grados[0], grados[1], grados[2], grados[3]=input("ingrese el valor: ").split()
    # zona de calculos
    desgradificacion[0]= int(grados[0]) / 10 + desgradificacion[0]
    desgradificacion[1]= int(grados[1]) / 10 + desgradificacion[0]
    desgradificacion[2]= int(grados[2]) / 10 + desgradificacion[1]
    desgradificacion[3]= int(grados[3]) / 10 + desgradificacion[2]
    agrupacion= agrupacion + abecedario[int(desgradificacion[0])] + abecedario[int(desgradificacion[1])] + abecedario[int(desgradificacion[2])] + abecedario[int(desgradificacion[3])]
    # salida
    print(agrupacion)

# llamada a la función
calculo_por_angulos()