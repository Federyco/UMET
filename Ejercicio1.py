#variables
medida_1=float(0.0)
medida_2=float(0.0)
medida_3=float(0.0)
ingreso_de_datos=int(0)

# funcion para el ingreso de 1 medida
def one_enter():
    medida_1=input("Ingrese la primer medida: ")
    while not(medida_1.isdigit()):
            print("Solo se permiten ingresos numéricos y positivos")
            medida_1=input("Ingrese la primer medida: ")
    print("La medida cúbica mayor es la 1 la cual vale: " + str(medida_1))
# funcion para el ingreso de 2 medidas
def two_enter():
    medida_1, medida_2=input("Ingrese la primer medida y la segunda separadas por un espacio: ").split()                 
    if(float(medida_2) > float(medida_1)):
            print("La medida cúbica mayor es la 2 la cual vale: " + str(medida_2))
    else:
            print("La medida cúbica mayor es la 1 la cual vale: " + str(medida_1))
# funcion para el ingreso de 3 medidas
def three_enter():
     print("Ingrese la primer medida, la segunda y la tercera ")
     medida_1,medida_2,  medida_3 = input("Siempre separando con un espacio: ").split()
     if(float(medida_1) > float(medida_2) and float(medida_1) > float(medida_3)):
            print("La medida cúbica mayor es la 1 la cual vale: " + str(medida_1))
     if(float(medida_2) > float(medida_1) and float(medida_2) > float(medida_3)):
            print("La medida cúbica mayor es la 2 la cual vale: " + str(medida_2))
     if(float(medida_3) > float(medida_1) and float(medida_3) > float(medida_2)):
            print("La medida cúbica mayor es la 3 la cual vale: " + str(medida_3))

# # funcion para el vaciado de variables
def vaciado_de_variables():
    medida_1=0
    medida_2=0
    medida_3=0
    
# salida de datos
print("Cuantos datos va a ingresar, máximo 3")
# entrada de datos
ingreso_de_datos=int(input("Ingreso: "))
#lógica
while (ingreso_de_datos < 4):
    if(ingreso_de_datos == 1):
        one_enter()            
    if(ingreso_de_datos == 2):
        two_enter()
    if(ingreso_de_datos == 3):
        three_enter()
    vaciado_de_variables()
    #interrupción del proceso
    break
# salida de datos
print("Saliendo del sistema")