'''
Created on 13 jun. 2022
NameError+, IndexError+,KeyError+,TypeError+,ValueError+,ZeroDivisionError,FileExistsError+,FileNotFoundError+
@author: nestor.solis
'''
from src.manejo.añadir import anadir_contacto
from src.manejo.buscar import buscar_contactos
from src.manejo.eliminar import eliminar_contactos
from src.manejo.lista import lista_contactos

class Agenda: 
    def mainmenu(self):
        print(" agenda ".title().center(85, "#"))
        menu=[["1. Añadir contactos"],["2. Lista de contactos"],["3. Buscar contactos"], \
            ["4. Eliminar contactos"], ["5. Cerrar agenda"]]
        numeroindice=int(input("intrduzca hasta donde quiere imprimir el menu"))
        try:
            for i in range(numeroindice):
                print(menu[i])
                print("")
        except IndexError:
            print("IndexError. Menu vacio")
        else:
            print("Ha introducido el indice satisfacoriamente")
        opcion=int(input("Introduzca la opción: "))
        if opcion==1:
            anadir_contacto()
        elif opcion==2:
            lista_contactos()
        elif opcion==3:
            buscar_contactos()
        elif opcion==4:
            eliminar_contactos()
        elif opcion==5:
            exit()
        self.mainmenu()

try:    
    agenda1=Agenda()
    agenda1.mainmenu()
except NameError:
    print("ha introducido mal el nombre de una funcion o intancia")
finally:
    print("todo ocurrio perfectamente")
    