numero=int(0)
x=int(1)

#declaro la funcion
def calculo_vectorial(numero):
    resultado=int(1)
    for x in range(1, numero+1):
        resultado = resultado * x
    return resultado
    

#entrada
numero=int(input("Ingrese el número al que desea calcular su factorial: "))
#solo ejecuta si el ingreso fue mayor o igual a 1 y menor o igual a 100
while (numero >= 1 and numero<=100):
    #corro la función dentro del bucle que chequea el valor ingresado
    calculo_vectorial(numero)
    #salida
    print("El Factorial de el número !" + str(numero) +", es " + str(calculo_vectorial(numero)))
    break
else:
    #salida
    print("Valor fuera de rango")
