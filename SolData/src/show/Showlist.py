'''
Created on 15 jun. 2022

@author: nestor.solis
'''

def lista(self):
    print("Lista de contactos".title().center(85, "#"))
    try:
        archivo = open("palabras.txt", "r")
        datos   = archivo.read()
        datos   = datos.split("\n")
        print("1.-Mostrar de 5 en 5 \npresionar cualquier tecla.-salir")
        opcion=int(input("Introduzca la opción: "))        
        if opcion==1:
            for i in range(0,len(datos),5):
                print("datos: ",datos[i:i+5])
        else :
            self.mainmenu()        
    except OSError:
        print("OSError. No se puede abrir. No existe")
        print("")
    else:
        print("El archivo existe")  
        print("")
    finally:
        archivo.close()
    