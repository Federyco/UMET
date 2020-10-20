# Ejercicio 9
# Queremos guardar la temperatura mínima y máxima de 5 días.
# Realiza un programa que de la siguiente información:
#* La temperatura media de cada día
#* Los días con menos temperatura
#* Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella.
#        si no existe ningún día se muestra un mensaje de información.


# durante los 5 dias se ingresaran 2 datos por día temp min y max luego se mostrara la temperatura media entre estas

dias=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
temp_min=[]
temp_max=[]
x=int(1)
pos = int(0)


continuar=bool(True)
ingreso=int(0)


#pos=int(0)


def media_max_y_min():
    lista_result=[]
    resultado=int(0)
    n=int(0)
    pos_lista=int(0)
    # calculo de la media de cada valor de las listas
    for x in range (0,5):
        resultado = round(((int(temp_min[n]) + int(temp_max[n])) / 2))
        lista_result.append(resultado)
        n = n +1
    # recorro el array en busca de valores menores a los ultimos 3
    # para probar utilize la secuencia 5,10 15,20 25,30 35,40 45,50
    # y con esta secuencia logre que imprima los valores en pos 0 y 1
    for x in range (0,5):       
        if(lista_result[pos_lista] < lista_result[-1] and lista_result[pos_lista] < lista_result[-2] and lista_result[pos_lista] < lista_result[-3] ):
            print("Dia/as de menor temperatura")
            print(dias[pos_lista])
            pos_lista = pos_lista + 1
        

def buscando_temperaturas():
    x2=int(0)
    pos_buscando=int(0)
    buscando=int(0)
    buscando=int(input("Ingrese una temperatura max, el sistema buscará si existen coincidencias: "))
    for x2 in range(1,6):
        if(int(temp_max[pos_buscando]) == buscando):
            print("Hemos hallado una coincidencia: ")
            print("El día " + str(dias[pos_buscando]) + " hizo " + str(temp_max[pos_buscando]) + " grados de temperatura máxima")
            pos_buscando = pos_buscando + 1
        else:
            print("No se hallo ningún valor coincidente para el día " + str(dias[pos_buscando]))
            pos_buscando = pos_buscando + 1


        
print("Hoy es " + str(dias[pos]) + " Ingrese las temperaturas min y máx")
ingreso_min=input("Ingreso temp minima: ")
temp_min.append(ingreso_min)
ingreso_max=input("Ingreso temp máxima: ")
temp_max.append(ingreso_max)
for x in range(1,5):
    pos = pos + 1
    print("Hoy es " + str(dias[pos]) + " Ingrese las temperaturas min y máx")   
    ingreso_min=input("Ingreso temp minima: ")
    temp_min.append(ingreso_min)
    ingreso_max=input("Ingreso temp máxima: ")
    temp_max.append(ingreso_max)
media_max_y_min()
buscando_temperaturas()