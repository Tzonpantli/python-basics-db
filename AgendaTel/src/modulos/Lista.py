'''
Created on 15 jun. 2022

@author: nestor.solis
'''
def lista_contactos():
    print("Lista de contactos".title().center(85, "#"))
    try:
        archivo=open("agendaTelefonos.txt","r")
        archivor=archivo.read()
        print("")
        print(archivor)
        #archivo.close()
    except OSError:
        print("OSError. No se puede abrir. No existe")
        print("")
    else:
        print("El archivo existe")  
        print("")
    finally:
        archivo.close()