# Ejercicio 6
# Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y
# diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas.
# Para simplificarlo vamos a suponer que febrero tiene 28 días.
global meses
global dias
global ingreso
meses=["No existe el mes 0", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias=[28,30,31]
ingreso=int(0)

def who_i_am(ingreso):
    if(ingreso == 1 or ingreso == 3 or ingreso == 5 or ingreso == 7 or ingreso == 8 or ingreso == 10 or ingreso == 12):
        print("El mes consultado es " + str(meses[ingreso] + " y este tiene " + str(dias[2]) + " días"))
    elif(ingreso == 4 or ingreso == 6 or ingreso == 9 or ingreso == 11):
        print("El mes consultado es " + str(meses[ingreso] + " y este tiene " + str(dias[1]) + " días"))
    elif(ingreso == 2):
        print("El mes consultado es " + str(meses[ingreso] + " y este tiene " + str(dias[0]) + " días"))
    else:
        if(ingreso == 0):
            print(meses[0])
ingreso=int(input("Ingrese un numero de mes: "))
who_i_am(ingreso)