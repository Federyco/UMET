# Ejercicio 11
# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
# Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen
# el valor 1 y el resto el valor 0.
# Muestra el contenido de la tabla en pantalla.
# Fuente -> https://www.youtube.com/watch?v=uYQaAvZlKbs
def construccion_matriz_visual():
    diagonal = [[1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]]
    visual=" "
    for i in range(5):
        for j in range(5):
            visual += str(diagonal[i][j]) + '\t'
        print(visual)
        visual=" "
construccion_matriz_visual()