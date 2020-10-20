# Ejercicio 1
# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y
# posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
import random
def make_me_random():
  global aleatorio
  global lista_de_paso
  for x in range(1):
    aleatorio= [(random.randint(1,10)),(random.randint(1,10)),(random.randint(1,10)),(random.randint(1,10)),(random.randint(1,10)),(random.randint(1,10)),(random.randint(1,10)),(random.randint(1,10)),(random.randint(1,10)),(random.randint(1,10)),(random.randint(1,10))]
    print ("En esta oportunidad los números aleatorios son: ")
    print(aleatorio[0], aleatorio[1], aleatorio[2], aleatorio[3], aleatorio[4], aleatorio[5], aleatorio[6], aleatorio[7], aleatorio[8], aleatorio[9])
    #utilizo una lista de paso ya que al realizar el primer cambio de valor en las variables, encuentro con que estas mismas son modificadas, por lo tanto
    # decidí utiliar una variable para almacenar los valores que fueron generados originalmente
  lista_de_paso=[aleatorio[0], aleatorio[1], aleatorio[2], aleatorio[3], aleatorio[4], aleatorio[5], aleatorio[6], aleatorio[7], aleatorio[8], aleatorio[9]]

def make_me_double():
  # elevo al cuadrado
  print ("En esta oportunidad los cuadrado de los números aleatorios son: ")
  print(pow(aleatorio[0],2), pow(aleatorio[1],2), pow(aleatorio[2],2), pow(aleatorio[3],2), pow(aleatorio[4],2), pow(aleatorio[5],2), pow(aleatorio[6],2), pow(aleatorio[7],2), pow(aleatorio[8],2), pow(aleatorio[9],2))

def make_me_a_cube():  
  # elevo al cubo
  print ("En esta oportunidad los cubos de los números aleatorios son: ")
  print(pow(lista_de_paso[0],3), pow(lista_de_paso[1],3), pow(lista_de_paso[2],3), pow(lista_de_paso[3],3), pow(lista_de_paso[4],3), pow(lista_de_paso[5],3), pow(lista_de_paso[6],3), pow(lista_de_paso[7],3), pow(lista_de_paso[8],3), pow(lista_de_paso[9],3))


make_me_random()
make_me_double()
make_me_a_cube()