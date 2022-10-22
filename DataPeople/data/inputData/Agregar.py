'''
Created on 13 jun. 2022

@author: nestor.solis
'''
def agregar():
    tabla1="Datos_personas.txt"
    fichero=open(tabla1,"a")
    nombre= input("agregar nombre: ")
    edad= int(input("agregue su edad: "))
    correo= input("agregar correo electronico: ")
    telefono= int(input("aregaar telefono: "))
    fichero.write(nombre+";"+str(edad)+";"+str(correo)+";"+str(telefono)+"\n")
    fichero.close()