'''
Created on 13 jun. 2022

@author: nestor.solis
'''
def eliminar_contactos():
    print("Editarcontactos".title().center(85, "#"))
    try:
        nombre=str(input("escriba el nombre de la persona que desea eliminar"))
    except ValueError:
        print("Error. nombre debe de ser string")
    else:
        archivo=open("Datos_personas.txt","r")
        lines= archivo.readlines()
        newList=[]
        for linea in lines:
            lista = linea.split(";")
            if(nombre != lista[0].strip("")):
                newList.append(linea)
        archivo.close()
        archivo=open("Datos_personas.txt","w")
        for i in newList:
            archivo.write(i)
        archivo.close()