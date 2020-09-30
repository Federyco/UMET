# min 3 max 5
cantDeLados=0
def tres_lados(cantDeLados):
    angulo1=0
    angulo2=0
    angulo3=0
    if(cantDeLados == 3):
        angulo1, angulo2, angulo3= input("Para el Póligono con " + str(cantDeLados) + " lados, ingrese sus ángulos separando con espacios: ").split()
        if (int(angulo1) <= 1000 and int(angulo1) >= 1 and int(angulo2) <= 1000 and int(angulo2) >= 1 and int(angulo3) <= 1000 and int(angulo3) >= 1 ):
            if(int(angulo1) == int(angulo2) and int(angulo1) == int(angulo3)):
                print("Es Regular")
            else:
                print("Es Irregular")
        else:
            print("Angulos fuera de rango")
        
    
def cuatro_lados(cantDeLados):
    angulo1=0
    angulo2=0
    angulo3=0
    angulo4=0
    if(cantDeLados == 4):
        angulo1, angulo2, angulo3, angulo4= input("Para el Póligono con " + str(cantDeLados) + " lados, ingrese sus ángulos separando con espacios: ").split()
        if (int(angulo1) <= 1000 and int(angulo1) >= 1 and int(angulo2) <= 1000 and int(angulo2) >= 1 and int(angulo3) <= 1000 and int(angulo3) >= 1 and int(angulo4) <= 1000 and int(angulo4) >= 1 ):
             if(int(angulo1) == int(angulo2) and int(angulo1) == int(angulo3) and  int(angulo1) == int(angulo4)):
                print("Es Regular")
             else:
                print("Es Irregular")
        else:
            print("Angulos fuera de rango")
def cinco_lados(cantDeLados):
    angulo1=0
    angulo2=0
    angulo3=0
    angulo4=0
    angulo5=0
    if(cantDeLados == 5): 
        angulo1, angulo2, angulo3, angulo4, angulo5= input("Para el Póligono con " + str(cantDeLados) + " lados, ingrese sus ángulos separando con espacios: ").split()
        if (int(angulo1) <= 1000 and int(angulo1) >= 1 and int(angulo2) <= 1000 and int(angulo2) >= 1 and int(angulo3) <= 1000 and int(angulo3) >= 1 and int(angulo4) <= 1000 and int(angulo4) >= 1 and int(angulo5) <= 1000 and int(angulo5) >= 1 ):
            if(int(angulo1) == int(angulo2) and int(angulo1) == int(angulo3) and  int(angulo1) == int(angulo4) and  int(angulo1) == int(angulo5)):
                print("Es Regular")
            else:
                print("Es Irregular")
        else:
            print("Angulos fuera de rango")
    
cantDeLados = int(input("Indique cuántos lados posee el Polígono: "))
if (cantDeLados <= 5 and cantDeLados >= 3):
    if(cantDeLados == 3):
        tres_lados(cantDeLados)
    if(cantDeLados == 4):
        cuatro_lados(cantDeLados)
    if(cantDeLados == 5):
        cinco_lados(cantDeLados)
else:
    print("Lados fuera de rango")

#  NOTA IMPORTANTE
# ¿Qué son los poligonos irregulares?
# Los Polígonos Irregulares son aquellos en los que sus lados no son todos iguales o en los que sus ángulos no miden todos lo mismo.
# el objeto de prueba 2, donde tiene 3 lados pero todos miden lo mismo está coinsiderado como un polígono regular