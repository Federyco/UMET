#variables
base=float(0.0)
altura=float(0.0)
# funcion encargada de la validación y cálculos
def is_a_triangle(base, altura):
    #logica
    while((float(base) >= 0 and float(base) <= 100) and float(altura) >= 0 and float(altura) <=100):
        if(base == altura):
            #salida
            print("El cuadrilátero ingresado es un: Cuadrado")
            break
        else:
            #salida
            print("El cuadrilátero ingresado es un: Rectángulo")
            break
#salida
print("No utilice valores mayores a 100 y menores a 0")
#entrada
base,altura=input("Ingrese primero la base, y dejando un espacio, ingrese la altura del Cuadrilátero: ").split()

#llamada a la función
is_a_triangle(base, altura)
#salida
print("Saliendo")