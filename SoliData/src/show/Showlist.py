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
        print("1.-Mostrar de 5 en 5 \n2.-salir")
        opcion=int(input("Introduzca la opción: "))        
        if opcion==1:
            #for i in range(0,len(datos),5):
            #   print("datos: ",datos[i:i+5])
            if(len(datos)>0):
                inicio=0
                final=0
                if(len(datos)<5):
                    final=len(datos)
                else:
                    final+=5
                while(True):
                    for i in range(inicio,final):
                        print(datos[i])
                    inicio=final
                    if((final +5)<len(datos)):
                        final+=5
                        input("Mostrar 5 más")
                    else:
                        final= len(datos)
                        if(inicio==final):
                            break
                        else:
                            print("")
                        input("Presione para mostrar mas")
                        print("")
            else:
                print("")
                print("no hay mas palabras")
        elif opcion==2:
            self.mainmenu()        
    except OSError:
        print("OSError. No se puede abrir. No existe")
        print("")
    else:
        print("")
        print("El archivo existe")  
        print("")
    finally:
        archivo.close()
    