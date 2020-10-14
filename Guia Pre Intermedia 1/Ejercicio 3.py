# Ejercicio 3
# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno
# (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media,
# la nota más alta que ha sacado y la menor.

notas=[0,0,0,0,0]
promedio=int(0)
mayor=int(0)
menor=int(0)

notas[0],notas[1],notas[2],notas[3],notas[4]=input("Ingrese las 5 notas, separadas por un espacio: ").split()
if (int(notas[0]) >= int(0)  and int(notas[1]) >= int(0)  and int(notas[2]) >= int(0)  and int(notas[3]) >= int(0)  and int(notas[4]) >= int(0)  and int(notas[0]) <= int(10) and int(notas[1]) <= int(10) and int(notas[2]) <= int(10) and int(notas[3]) <= int(10) and int(notas[4]) <= int(10)):
        print("Las notas ingresadas son: ")
        print(notas[0], notas[1], notas[2], notas[3], notas[4])
        promedio = round((int(notas[0]) + int(notas[1]) + int(notas[2]) + int(notas[3]) + int(notas[4])) / 5)
        # MEDIA
        print("La nota media es: " + str(promedio))
        # MAYOR
        if(int(notas[0]) > int(notas[1]) and int(notas[0]) > int(notas[2]) and int(notas[0]) > int(notas[3]) and int(notas[0]) > int(notas[4])):
                mayor= int(notas[0])
                print("La nota mayor es: " + str(mayor))
        elif(int(notas[1]) > int(notas[0]) and int(notas[1]) > int(notas[2]) and int(notas[1]) > int(notas[3]) and int(notas[1]) > int(notas[4])):
                mayor= int(notas[1])
                print("La nota mayor es: " + str(mayor))
        elif(int(notas[2]) > int(notas[0]) and int(notas[2]) > int(notas[1]) and int(notas[2]) > int(notas[3]) and int(notas[2]) > int(notas[4])):
            mayor= int(notas[2])
            print("La nota mayor es: " + str(mayor))
        elif(int(notas[3]) > int(notas[0]) and int(notas[3]) > int(notas[1]) and int(notas[3]) > int(notas[2]) and int(notas[3]) > int(notas[4])):
            mayor= int(notas[3])
            print("La nota mayor es: " + str(mayor))
        elif(int(notas[4]) > int(notas[0]) and int(notas[4]) > int(notas[1]) and int(notas[4]) > int(notas[2]) and int(notas[4]) > int(notas[3])):
            mayor= int(notas[4])
            print("La nota mayor es: " + str(mayor))
        # MENOR
        if(int(notas[0]) < int(notas[1]) and int(notas[0]) < int(notas[2]) and int(notas[0]) < int(notas[3]) and int(notas[0]) < int(notas[4])):
            menor= int(notas[0])
            print("La nota menor es: " + str(menor))
        elif(int(notas[1]) < int(notas[0]) and int(notas[1]) < int(notas[2]) and int(notas[1]) < int(notas[3]) and int(notas[1]) < int(notas[4])):
            menor= int(notas[1])
            print("La nota menor es: " + str(menor))
        elif(int(notas[2]) < int(notas[0]) and int(notas[2]) < int(notas[1]) and int(notas[2]) < int(notas[3]) and int(notas[2]) < int(notas[4])):
            menor= int(notas[2])
            print("La nota menor es: " + str(menor))
        elif(int(notas[3]) < int(notas[0]) and int(notas[3]) < int(notas[1]) and int(notas[3]) < int(notas[2]) and int(notas[3]) < int(notas[4])):
            menor= int(notas[3])
            print("La nota menor es: " + str(menor))
        elif(int(notas[4]) < int(notas[0]) and int(notas[4]) < int(notas[1]) and int(notas[4]) < int(notas[2]) and int(notas[4]) < int(notas[3])):
            menor= int(notas[4])
            print("La nota menor es: " + str(menor))   
else:
    print("Valores fuera de rango")