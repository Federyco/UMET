# Conexión de resistencias en paralelo
#variables
cant_de_resistencias=int(0)
valor_res_1=int(0)
valor_res_2=int(0)
continuar=bool(True)
ingreso=0
# funcion que maneja el cálculo de resistencias, recibe 2 valores devuelve el resultado
def calculo_de_resistencias(valor_res_1, valor_res_2):
    resultado = int(0)
    while(int(valor_res_1) >=0 and int(valor_res_1) <=10000 and int(valor_res_2) >=0 and int(valor_res_2) <=10000):
                    resultado = round(1/((1/int(valor_res_1))+(1/int(valor_res_2))))
                    return resultado
                    break
    else:
        #salida
        print("Valores fuera de rango, ingrese nuevamente."
while continuar:
    #salida
    print("Ingrese lo datos como el programa indica, los valores deben estar separados por un espacio.")
    print("Cantidad de resistencias, valor resistencia 1, valor resistencia 2")
    #entrada
    cant_de_resistencias, valor_res_1, valor_res_2 = input("Ingrese los datos: ").split()
    calculo_de_resistencias(valor_res_1, valor_res_2)
    #salida
    print(calculo_de_resistencias(valor_res_1, valor_res_2))
    #entrada
    ingreso=input("¿Desea ingresar otro cálculo? Ingrese 1 para SI, 2 para NO ")
    while not (ingreso.isdigit()):
        #salida
        print("Solo se permiten valores numéricos y positivos")
        #entrada
        ingreso=input("¿Desea ingresar otro cálculo? Ingrese 1 para SI, 2 para NO ")
    if(ingreso == 1):
        continuar = True
    else:
        #salida
        print("Saliendo del sistema")
        continuar=False