#Variables
valor1=0
valor2=0
resultado=int(0)

#Definicion de la funcion SUMA
def suma(valor1,valor2):
    resultado= int(valor1) + int(valor2)
    return resultado

#input de valores entrada
valor1, valor2=input("Ingrese los valores que desea sumar, separados por un espacio").split()
#llamado a la funcion
suma(valor1,valor2)
#salida
print(suma(valor1,valor2))
