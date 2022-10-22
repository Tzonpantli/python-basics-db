'''
Created on 13 jun. 2022

@author: nestor.solis
'''
def anadir_contacto():
    print(" Añadir nuevo contacto ".title().center(85, "#"))
    try:
        tabla1="Datos_personas.txt"
        fichero=open(tabla1,"a")
        nombre= input("agregar nombre: ")
        edad= int(input("agregue su edad: "))
        correo= input("agregar correo electronico: ")
        telefono= int(input("aregaar telefono: "))
        try:
            fichero.write(nombre+";"+str(edad)+";"+str(correo)+";"+str(telefono)+"\n")
            fichero.close()
        except TypeError:
            print("alguna cosa que se intenta meter en el fichero no es string")    
    except FileExistsError:
        print("FileExistError. el fichero no puede crear uno existente")
    else:
        print("Todo ha ido correctamente")
        