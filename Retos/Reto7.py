#variables
#numero mayor
numero1=0
#numero menor
numero2=0
#numero multiplo
numero3=0

def es_mayor(numero1, numero2, numero3):
      resto=int(0)
      quien_es_N = int(1)
      # si N es mayor al numero 1 ingresado devuelve el número que fue mayor
      # si N es menor al numero2 ingresado devuelve el número que cumple con ambas condiciones
      # y por ultimo chequea si este es un multiplo
      for quien_es_N in range(1, 101):
            resto = quien_es_N % int(numero3)
            while (quien_es_N > int(numero1) and quien_es_N  < int(numero2) and resto == 0):
                  return (int(quien_es_N))

      
print("Tenga en cuenta que las posiciones son: Mayor, Menor y Multiplo.")
numero1, numero2, numero3=input("Ingrese 3 valores, separados por espacios: ").split()
if(int(numero1) <= 100 and int(numero1) >= 1 and int(numero2) <= 100 and int(numero2) >= 1 and int(numero3) <= 100 and int(numero3) >= 1):
      es_mayor(numero1, numero2, numero3)
      if(es_mayor(numero1, numero2, numero3) == None):
            print("0")
      else:
            print("me devolvio " + str(es_mayor(numero1, numero2, numero3)))
else:
      print("Valor fuera de rango")
