'''
Created on 15 jun. 2022

@author: nestor.solis
'''
from src.modulos.Añadir import anadir_contacto
def eliminar_contactos(self):
    print("Eliminar contactos".title().center(85, "#"))
    try:
        nombre=str(input("escriba el nombre de la persona que desea eliminar"))
    except ValueError:
        print("Error. nombre debe de ser string")
    else:
        archivo=open("agendaTelefonos.txt","r")
        lines= archivo.readlines()
        newList=[]
        for linea in lines:
            lista = linea.split("|")
            if(nombre != lista[0].strip("")):
                newList.append(linea)
        archivo.close()
        archivo=open("agendaTelefonos.txt","w")
        for i in newList:
            archivo.write(i)
        archivo.close()
        choose=int(input("desea añadir un contacto nuevo? 1.-Si 2.-No"))
        if choose==1:
            anadir_contacto(self)
        elif choose==2:
            self.mainmenu()