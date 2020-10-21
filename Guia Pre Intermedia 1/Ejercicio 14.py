# Ejercicio 14
# Crear un programa que lea los precios de 5 artículos y las cantidades vendidas
# por una empresa en sus 4 sucursales.
#      Informar:
# * Las cantidades totales de cada articulo. x
# * La cantidad de artículos en la sucursal 2. x
# * La cantidad del articulo 3 en la sucursal 1. x
# * La recaudación total de cada sucursal. x
# * La recaudación total de la empresa. x
# * La sucursal de mayor recaudación. x

global articulos
articulos=["Leche", "Harina", "Aceite", "Manteca", "Queso"]
global sucursales
sucursales=["Lomas de Zamora", "Palermo", "Morón", "Mataderos"]



print("Ingrese precio = 0 para salir")


def lomas_de_zamora():
        global precios_lomas
        precios_lomas=[]
        global cantidad_lomas
        cantidad_lomas=[]
        pos_lom=int(0)
        ingreso_precio_lomas=[]
        ingreso_articulos_lomas=[]      
        print("Ingrese los precios y cantidades vendidos en la sucurdal de " + str(sucursales[0]))
        for x in range(0,5):
            ingreso_precio_lomas=input("Ingrese precio del artículo " + str(articulos[pos_lom]) + ": ")
            if(float(ingreso_precio_lomas[0]) == 0 or float(ingreso_precio_lomas[0]) == 0.0):
                print("Saliendo")
                break
            precios_lomas.append(ingreso_precio_lomas)
            ingreso_articulos_lomas=input("Ingrese la cantidad del artículo " + str(articulos[pos_lom]) + ": ")
            cantidad_lomas.append(ingreso_articulos_lomas)
            pos_lom = pos_lom +1

def palermo():
        global precios_palermo
        precios_palermo=[]
        global cantidad_palermo
        cantidad_palermo=[]
        pos_pal=int(0)
        ingreso_precio_palermo=[]
        ingreso_articulos_palermo=[]      
        print("Ingrese los precios y cantidades vendidos en la sucurdal de " + str(sucursales[1]))
        for x in range(0,5):
            ingreso_precio_palermo=input("Ingrese precio del artículo " + str(articulos[pos_pal]) + ": ")
            if(float(ingreso_precio_palermo[0]) == 0 or float(ingreso_precio_palermo[0]) == 0.0):
                print("Saliendo")
                break
            precios_palermo.append(ingreso_precio_palermo)
            ingreso_articulos_palermo=input("Ingrese la cantidad del artículo " + str(articulos[pos_pal]) + ": ")
            cantidad_palermo.append(ingreso_articulos_palermo)
            pos_pal = pos_pal +1

def moron():
        global precios_moron
        precios_moron=[]
        global cantidad_moron
        cantidad_moron=[]
        pos_mor=int(0)
        ingreso_precio_moron=[]
        ingreso_articulos_moron=[]      
        print("Ingrese los precios y cantidades vendidos en la sucurdal de " + str(sucursales[2]))
        for x in range(0,5):
            ingreso_precio_moron=input("Ingrese precio del artículo " + str(articulos[pos_mor]) + ": ")
            if(float(ingreso_precio_moron[0]) == 0 or float(ingreso_precio_moron[0]) == 0.0):
                print("Saliendo")
                break
            precios_moron.append(ingreso_precio_moron)
            ingreso_articulos_moron=input("Ingrese la cantidad del artículo " + str(articulos[pos_mor]) + ": ")
            cantidad_moron.append(ingreso_articulos_moron)
            pos_mor = pos_mor +1

def mataderos():
        global precios_mataderos
        precios_mataderos=[]
        global cantidad_mataderos
        cantidad_mataderos=[]
        pos_mat=int(0)
        ingreso_precio_mataderos=[]
        ingreso_articulos_mataderos=[]      
        print("Ingrese los precios y cantidades vendidos en la sucurdal de " + str(sucursales[3]))
        for x in range(0,5):
            ingreso_precio_mataderos=input("Ingrese precio del artículo " + str(articulos[pos_mat]) + ": ")
            if(float(ingreso_precio_mataderos[0]) == 0 or float(ingreso_precio_mataderos[0]) == 0.0):
                print("Saliendo")
                break
            precios_mataderos.append(ingreso_precio_mataderos)
            ingreso_articulos_mataderos=input("Ingrese la cantidad del artículo " + str(articulos[pos_mat]) + ": ")
            cantidad_mataderos.append(ingreso_articulos_mataderos)
            pos_mat = pos_mat +1
    
def total_article():
    total_art0=int(0)
    total_art1=int(0)
    total_art2=int(0)
    total_art3=int(0)
    total_art4=int(0)
    total_art0 = round(int(cantidad_lomas[0]) + int(cantidad_palermo[0]) + int(cantidad_moron[0]) + int(cantidad_mataderos[0]))
    total_art1 = round(int(cantidad_lomas[1]) + int(cantidad_palermo[1]) + int(cantidad_moron[1]) + int(cantidad_mataderos[1]))
    total_art2 = round(int(cantidad_lomas[2]) + int(cantidad_palermo[2]) + int(cantidad_moron[2]) + int(cantidad_mataderos[2]))
    total_art3 = round(int(cantidad_lomas[3]) + int(cantidad_palermo[3]) + int(cantidad_moron[3]) + int(cantidad_mataderos[3]))
    total_art4 = round(int(cantidad_lomas[4]) + int(cantidad_palermo[4]) + int(cantidad_moron[4]) + int(cantidad_mataderos[4]))
    print("En total, se vendieron:")
    print(str(total_art0) + " Leches")
    print(str(total_art1) + " Harinas")
    print(str(total_art2) + " Aceites")
    print(str(total_art3) + " Mantecas")
    print(str(total_art4) + " Quesos")
    

def suc2_sell():
    total_art_palermo=int(0)
    total_art_palermo = round(int(cantidad_palermo[0]) + int(cantidad_palermo[1])  + int(cantidad_palermo[2]) + int(cantidad_palermo[3]) + int(cantidad_palermo[4]))
    print("La cantidad de artículos vendidos en la sucursal 2 fueron: " + str(total_art_palermo))


def tres_en_1():
    print("La cantidad de artículos 3 vendidos en la sucursal 1 fueron: " + str(cantidad_lomas[3]))

def cuentas():
    global rec_total_cucursal_1
    global rec_total_cucursal_2
    global rec_total_cucursal_3
    global rec_total_cucursal_4
    rec_total_empresa=float(0)
    rec_total_cucursal_1=float(0)
    rec_total_cucursal_2=float(0)
    rec_total_cucursal_3=float(0)
    rec_total_cucursal_4=float(0)
    rec_total_cucursal_1 = round(((cantidad_lomas[0] * precios_lomas[0]) + (cantidad_lomas[1] * precios_lomas[1]) + (cantidad_lomas[2] * precios_lomas[2]) + (cantidad_lomas[3] * precios_lomas[3]) + (cantidad_lomas[4] * precios_lomas[4])))
    rec_total_cucursal_2 = round(((cantidad_palermo[0] * precios_palermo[0]) + (cantidad_palermo[1] * precios_palermo[1]) + (cantidad_palermo[2] * precios_palermo[2]) + (cantidad_palermo[3] * precios_palermo[3]) + (cantidad_palermo[4] * precios_palermo[4])))
    rec_total_cucursal_3 = round(((cantidad_moron[0] * precios_moron[0]) +  (cantidad_moron[1] * precios_moron[1]) + (cantidad_moron[2] * precios_moron[2]) + (cantidad_moron[3] * precios_moron[3]) + (cantidad_moron[4] * precios_moron[4])))
    rec_total_cucursal_4 = round(((cantidad_mataderos[0] * precios_mataderos[0]) + (cantidad_mataderos[1] * precios_mataderos[1]) + (cantidad_mataderos[2] * precios_mataderos[2]) + (cantidad_mataderos[3] * precios_mataderos[3]) + (cantidad_mataderos[4] * precios_mataderos[4])))
    rec_total_empresa= rec_total_cucursal_1 +  rec_total_cucursal_2 +  rec_total_cucursal_3 +  rec_total_cucursal_4
    print("Ventas totales por sucursal: ")
    print("La sucursal 1 vendió un total de: " + str(rec_total_cucursal_1) + " $")
    print("La sucursal 2 vendió un total de: " + str(rec_total_cucursal_2) + " $")
    print("La sucursal 3 vendió un total de: " + str(rec_total_cucursal_3) + " $")
    print("La sucursal 4 vendió un total de: " + str(rec_total_cucursal_4) + " $")
    print("La recaudación total de la empresa fue: " + str(rec_total_empresa) + " $")
    if(rec_total_cucursal_1 > rec_total_cucursal_2 and rec_total_cucursal_1 > rec_total_cucursal_3 and rec_total_cucursal_1 > rec_total_cucursal_4):
        print("La sucursal con mayor recaudación fue: " + str(sucursales[0]) + " con un total de " + str(rec_total_cucursal_1))
    elif(rec_total_cucursal_2 > rec_total_cucursal_1 and rec_total_cucursal_2 > rec_total_cucursal_3 and rec_total_cucursal_2 > rec_total_cucursal_4):
        print("La sucursal con mayor recaudación fue: " + str(sucursales[1]) + " con un total de " + str(rec_total_cucursal_2))
    elif(rec_total_cucursal_3 > rec_total_cucursal_1 and rec_total_cucursal_3 > rec_total_cucursal_2 and rec_total_cucursal_3 > rec_total_cucursal_4):
        print("La sucursal con mayor recaudación fue: " + str(sucursales[2]) + " con un total de " + str(rec_total_cucursal_3))
    elif(rec_total_cucursal_4 > rec_total_cucursal_1 and rec_total_cucursal_4 > rec_total_cucursal_2 and rec_total_cucursal_4 > rec_total_cucursal_3):
        print("La sucursal con mayor recaudación fue: " + str(sucursales[3]) + " con un total de " + str(rec_total_cucursal_4))

lomas_de_zamora()
palermo()
moron()
mataderos()
total_article()
suc2_sell()
tres_en_1()
cuentas()


###DEBUG
##print("    **** DEBUG    ****    ")
##print("Lomas")
##print(precios_lomas)
##print(cantidad_lomas)
##print("Palermo")
##print(precios_palermo)
##print(cantidad_palermo)
##print("Morón")
##print(precios_moron)
##print(cantidad_moron)
##print("Mataderos")
##print(precios_mataderos)
##print(cantidad_mataderos)

