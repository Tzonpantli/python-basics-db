'''
Created on 13 jun. 2022

@author: nestor.solis
'''
def agregar():
    tabla1="Datos_alumno.txt"
    fichero=open(tabla1,"w")
    cantidad_alumnos= int(input("ingrese la cantidad de alumnos"))
    for i in range(1,cantidad_alumnos+1):
        nombre= input("agregar nombre completo: ")
        id_alumno= i
        carrera= input("agregue su carrera: ")
        promedio= float(input("ingresar promedio: "))
        fichero.write(str(id_alumno)+";"+nombre+";"+carrera+";"+str(promedio)+"\n")
        i+=i