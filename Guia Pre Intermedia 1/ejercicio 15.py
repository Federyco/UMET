# Ejercicio 15
# Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol.
# Para ello vamos a utilizar dos tablas:
# Equipos: Que es una tabla de cadenas donde guardamos en cada columna el
# nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
# Resultados: Es una tabla de enteros donde se indica el resultado.
# También tiene dos columnas, en la primera se guarda el número de goles del equipo que está
# guardado en la primera columna
# de la tabla anterior, y en la segunda los goles del otro equipo.
# El programa ira pidiendo los nombres de los equipos de cada partido y
# el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.
# ¿Qué modificación habría que hacer en las tablas para guardar todos los
# resultados de todas las jornadas de la temporada?
eq1=0
eq2=0
equipos=[]
eq1_res=0
eq2_res=0
resultados=[]
jornada_mensual=[]
n=int(0)    
for x in range(0,15):
    eq1,eq2=str(input("Ingrese los nombres de los equipos: ")).split()
    equipos.append([eq1 + " Vs " + eq2])
    eq1_res,eq2_res=input("Ingrese el resultado del partido: ").split()
    resultados.append([eq1_res + " a " + eq2_res])
print("Quiniela del día de la fecha: ")
for x in range(0,15):
    print("Los equipos " + str(equipos[n]) + " compitieron y el resultado fue: " + str(resultados[n]))
    n = n + 1

## para la jornada mensual decomentar el siguiente código
#jornada_mensual.append([equipos, resultados])
#print("La jornada mensual completa fue: " + str(jornada_mensual))