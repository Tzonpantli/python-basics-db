'''
Created on 15 jun. 2022

@author: nestor.solis
'''
def buscar_contactos():
    print("Buscador de contactos".title().center(85, "#"))
    try:
        nombre=input("Que contacto desea buscar? ")
        archivo=open("agendaTelefonos.txt","r")        
        linea=archivo.readline()
        alumno=""
        while(linea!= ""):
            lista=linea.split("|")
            if(nombre== lista[0].strip("")):
                alumno= linea
            linea=archivo.readline()
        if(alumno!= ""):
            print("alumno encontrado")
            print(alumno)
            archivo.close()
        else:
            print("el alumno no esta registrado")
            archivo.close()
    except KeyError:
        print("La palabra no se encuentra en el diccionario")
    else:
        print("Ha introducido la palabra satisfactoriamente")