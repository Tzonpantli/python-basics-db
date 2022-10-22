'''
Created on 15 jun. 2022

@author: nestor.solis
'''

def carga():
        print(" Añadir nuevas palabras Data ".title().center(85, "#"))
        try:
            palabras="palabras.txt"
            fichero=open(palabras,"a")
            palabra= input("agregar nombre: ")
            try:
                fichero.write(palabra + "\n")
                fichero.close()
            except TypeError:
                print("alguna cosa que se intenta meter en el fichero no es string")    
        except FileExistsError:
            print("FileExistError. el fichero no puede crear uno existente")
        else:
            print("Todo ha ido correctamente ")
        