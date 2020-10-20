# Ejercicio 12
# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
# Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones
# o elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los
# elementos contendrán el valor 0.
 # 111111111111111
 # 100000000000001
 # 100000000000001
 # 100000000000001
 # 111111111111111
#Visualiza el contenido de la matriz en pantalla.
def construccion_matriz_visual():
    marco=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    visual=" "
    for i in range(5):
        for j in range(15):
            visual += str(marco[i][j]) + '\t'
        print(visual)
        visual=" "
construccion_matriz_visual()
