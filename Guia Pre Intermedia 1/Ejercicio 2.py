# Ejercicio 2
# Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado.
# Copia los elementos de la lista en otra lista pero en orden inverso,
# y muestra sus elementos por la pantalla.

give=[" ", " ", " ", " ", " "]
give[0],give[1],give[2],give[3],give[4]=input("Ingrese 5 cadenas de texto separadas por espacios: ").split()
take=[give[4], give[3], give[2], give[1], give[0]]
print(take[0],take[1],take[2],take[3],take[4])