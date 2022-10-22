'''
Created on 13 jun. 2022

@author: nestor.solis
'''
'''
Created on 13 jun. 2022
Escribir una función que pida un número entero entre 1 y 10, se deberá crear un archivo (tabla-numero.txt) 
que contendrá la tabla de multiplicar de ese número. 
Y crear otra función que muestre el contenido de ese archivo en pantalla.

Escribir un programa que pida los datos nombre, edad, correo y teléfono de una persona, 
y estos datos se deberán guardar en un archivo (datos-personas.txt). Cada vez que se ejecute el 
programa se deberá agregar los datos de una nueva persona a dicho archivo. 
(El archivo deberá contener los datos separados por “|” o “;”)

@author: nestor.solis
'''
def crear_tabla():
        #numero= int(input("De que numero quieres saber la tabla?: "))
        tabla ="La_Tabla_del_" +str(numero)+".txt"
        fichero=open(tabla,"w")
        cadena="Tabla del numero "+ str(numero)+"\n"
        fichero.write(cadena)
        for i in range(1,11):
            valor=numero*i
            fichero.write((str(numero)) +"x"+str(i)+"="+str(valor)+"\n")
        fichero.close()
        
def mostrar_tabla():
    #"C:/Users/nestor.solis/Documents/Java IDS/workspace/list/listas/La_Tabla_del_10.txt" print("Hello to the {} {}".format(var2,var1))
    archivo=open("La_Tabla_del_{}.txt".format(numero),"r")
    #f = open ('holamundo.txt','r') mensaje = f.read() print(mensaje) f.close()
    archivor=archivo.read()
    print("")
    print(archivor)
    archivo.close()

numero= int(input("De que numero quieres saber la tabla?: "))
crear_tabla()
mostrar_tabla()