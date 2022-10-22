'''
Created on 15 jun. 2022
Ejercicio 3
Escribir un programa para una agenda  telefónica con los nombres y los teléfonos de los clientes 
de una empresa dedicada a los deportes. Incorporar funciones 
1.- Crear el fichero si no existe,
2.- Consultar el teléfono de un cliente, 
3.- Añadir el teléfono de un nuevo cliente, verifica que el número no pertenezca 
a otro cliente existente (validar que solo sean números)
4.- Eliminar el teléfono de un cliente, al eliminar deberá llamar generar un mensaje de cliente 
sin teléfono y le indicará si desea agregar uno nuevo, si desea agregar llamar a la función Añadir el teléfono .
La agenda debe estar guardado en un fichero de texto agendaTelefonos.txt donde el nombre del cliente 
y su teléfono deben aparecer separados por “|” y cada cliente en una línea distinta.
@author: nestor.solis
'''
from src.modulos.Añadir import anadir_contacto
from src.modulos.Lista import lista_contactos
from src.modulos.Buscar import buscar_contactos
from src.modulos.Eliminar import eliminar_contactos
class Agenda_telefono: 
    def mainmenu(self):
        print(" agenda telefono ".title().center(85, "#"))
        menu=[["1. Añadir contactos"],["2. Lista de contactos"],["3. Buscar contactos por telefono"], \
            ["4. Eliminar Telefono"], ["5. Cerrar agenda"]]
        for i in range(5):
            print(menu[i])
            print("")
        opcion=int(input("Introduzca la opción: "))
        if opcion==1:
            anadir_contacto(self)#aqui tambien se crea el fichero
        elif opcion==2:
            lista_contactos()
        elif opcion==3:
            buscar_contactos()
        elif opcion==4:
            eliminar_contactos(self)
        elif opcion==5:
            exit()
        self.mainmenu()

  
agenda1=Agenda_telefono()
agenda1.mainmenu()