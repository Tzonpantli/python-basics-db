'''
Created on 15 jun. 2022

@author: nestor.solis
'''

def anadir_contacto(self):
    print(" Añadir nuevo contacto ".title().center(85, "#"))
    try:
        tabla1="agendaTelefonos.txt"
        fichero=open(tabla1,"a+")
        nombre= input("agregar nombre: ")
        telefono= int(input("aregaar telefono: "))
        #linea=fichero.readline()
        try:
            archivo=open("agendaTelefonos.txt","r")        
            linea=archivo.readline()
            alumno=""
            while(linea!= ""):
                lista=linea.split("|")
                if(str(telefono)+"\n"== lista[1].strip("")):
                    alumno= linea
                linea=archivo.readline()
                #print(lista)
            if(alumno!= ""):
                print("el numero telefonico ya estaba registrado para este cliente")
                print(alumno)
                archivo.close()
            else:
                print("el numero no esta registrado")
                archivo.close()
        except KeyError:
            print("La palabra no se encuentra en el diccionario")
        ##
    except ValueError:
        print("Error. No se puede meter strings en el numero telefonico")
    else:
        print("Todo ha ido correctamente") 
        
        try:
            fichero.write(nombre+"|"+str(telefono)+ "\n")
            fichero.close()
        except TypeError:
            print("alguna cosa que se intenta meter en el fichero no es string")    