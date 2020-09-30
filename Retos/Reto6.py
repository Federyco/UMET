#Variables
poligonos=["Triángulo", "Cuadrilátero", "Pentágono", "Hexágono", "Heptágono"]
equivalente=int(0)
#definición de la función
def que_poligono_es(equivalente):
    while (equivalente <= 7 and equivalente >= 3):
        if(equivalente == 3):
            #salida
            print("El polígono es un " + str(poligonos[0]))
            break
        else:
            if(equivalente == 4):
                #salida
                print("El polígono es un " + str(poligonos[1]))
                break
            else:
                if(equivalente == 5):
                    #salida
                    print("El polígono es un " + str(poligonos[2]))
                    break
                else:
                    if(equivalente == 6):
                        #salida
                        print("El polígono es un " + str(poligonos[3]))
                        break
                    else:
                        if(equivalente == 7):
                            #salida
                            print("El polígono es un " + str(poligonos[4]))
                            break
        print("Valor fuera de rango")
#entrada
equivalente=int(input("Ingrese un número entre 3 y 7, indicando la cantidad de lados: "))
#llamado a la función
que_poligono_es(equivalente)