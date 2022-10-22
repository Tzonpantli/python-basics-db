'''
Created on 13 jun. 2022

@author: nestor.solis
'''
def mostrar_tabla():
    archivo=open("Datos_personas.txt","r")
    archivor=archivo.read()
    print("")
    print(archivor)
    archivo.close()