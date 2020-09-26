#Clasificación de los triángulos según sus lados
#variables
ladoA=float(0.0)
ladoB=float(0.0)
ladoC=float(0.0)
def is_a_triangle(ladoA, ladoB,ladoC):
    #logica
    while((float(ladoA) >= 0 and float(ladoA) <= 100) and float(ladoB) >= 0 and float(ladoB) <=100 and float(ladoC) >= 0 and float(ladoC) <=100):
        if(ladoA == ladoB and ladoB == ladoC and ladoA == ladoC):
            #salida
            print("El triángulo ingresado es Equilátero")
            break
        else:
            if(ladoA == ladoC and ladoB != ladoC and ladoB != ladoA):
                #salida
                print("El triángulo ingresado es Isósceles")
                break
            else:
                #salida
                print("El triángulo ingresado es Escaleno")
                break               
#salida
print("No utilice valores mayores a 100 y menores a 0")
#entrada
ladoA,ladoB,ladoC=input("Ingrese los 3 lados del triángulo dejando un espacio entre cada valor: ").split()
is_a_triangle(ladoA, ladoB, ladoC)
#salida
print("Recuerde utilizar valores menores a 100 y mayores a 0")