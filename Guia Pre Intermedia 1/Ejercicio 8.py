# Ejercicio 8
# Queremos guardar los nombres y la edades de los alumnos de un curso.
# Realiza un programa que introduzca el nombre y la edad de cada alumno.
# El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*)
# Al finalizar se mostrará los siguientes datos:
#*          Todos lo alumnos mayores de edad.
#*          Los alumnos mayores (los que tienen más edad)
nombre=str("")
edad=int(0)
alumnos=[]
edades=[]


def new_alumno_y_edad():
    n=int(0)
    mayor_edad =int(18)
    edad_unica=int(21)
    for x  in range (0,5000):
        nombre=input("Ingrese el nombre del alumno: ")
        if(nombre == "*"):
            # con len() reviso la cantidad de espacios dentro del array
            for x in range (0, len(edades)):
                if(int(edades[n]) >= mayor_edad and int(edades[n]) < edad_unica):
                        print(str(alumnos[n]) + " Es mayor de edad")
                        n = n + 1
                elif(int(edades[n]) >= edad_unica):
                        print(str(alumnos[n]) + " Posee la mayoria de edad")
                        n = n + 1
                else:
                        print(str(alumnos[n]) + " Es menor de edad")
                        n = n + 1    
            break
        alumnos.append(nombre)
        edad=input("Ingrese la edad del alumno: ")
        edades.append(edad)        
new_alumno_y_edad()