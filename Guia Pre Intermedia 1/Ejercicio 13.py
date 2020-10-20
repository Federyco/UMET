# Ejercicio 13
# De una empresa de transporte se quiere guardar el nombre de los conductores que tiene,
# y los kilómetros que conducen cada día de la semana.
# Para guardar esta información se van a utilizar dos arreglos:
            # Nombre: Lista para guardar los nombres de los conductores.
            # kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
# Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.
# Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.
def nombre_y_kms():
    global nombre
    global ingreso_nombre
    global kms
    global ingreso_kms
    global total_kms
    global resultado_kms
    global pos_kms
    nombre=[]
    ingreso_nombre=str(" ")
    kms=[]
    ingreso_kms=int(0)
    total_kms=[]
    resultado_kms=int(0)
    pos_kms=int(0)
    paso=int(0)
    print("Para salir ingrese * cuando el sistema le pida un nombre.")
    while (ingreso_nombre != "*"):
        ingreso_nombre=input("Ingrese el nombre de conductor: ")
        if (str(ingreso_nombre) == "*"):
            print("Saliendo")
            print("Realizando los cálculos pertinentes, aguarde por favor....")
            break
        nombre.append(ingreso_nombre)
        print("Ingrese los kmts recorridos por el chofer, separados por un espacio.")
        print("Se requieren 7 valores.")
        ingreso_kms=input("Ingrese los Kms recorridos: ").split()
        kms.append(ingreso_kms)
        # bucle for para calcular el total de cada chofer
        # sumando cada uno de los valores de la lista
        for x in range(7):
            resultado_kms = resultado_kms + int(ingreso_kms[pos_kms])
            pos_kms = pos_kms + 1
            paso = resultado_kms
        total_kms.append(paso)
        pos_kms = 0
        resultado_kms=0


def impresiones_en_pantalla():
    pos_nombre=int(0)
    # recorre la integridad de la tabla nombre, con len() me aseguro de chequear todos los valores de la misma
    for x in range(0, len(nombre)):
       print("El Chofer " + str(nombre[pos_nombre]) + " realizó " + str(total_kms[pos_nombre]) + " Kilometros en total.")
       pos_nombre = pos_nombre + 1
            

nombre_y_kms()
impresiones_en_pantalla()