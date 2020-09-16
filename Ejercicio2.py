#variables
vueltas=float(0.0)
radio=float(0.0)
distancia=int(0)
pi=float(3.14)
coeficiente=float(100.0)
ingreso1=float(0.0)
ingreso2=float(0.0)
# funcion encargada de los cálculos
def calc_radio_vueltas(radio, vueltas):
    distancia = (float(vueltas) * (2*pi*float(radio)))
    distancia = distancia / coeficiente
    return distancia
#salida
print("Ingrese radio y vueltas separados por un espacio ")
#entrada
radio, vueltas=input("radio y vueltas: ").split()
# llamada a la función
calc_radio_vueltas(radio, vueltas)
#salida
print("La distancia recorrida es: " + str(calc_radio_vueltas(radio, vueltas)))