'''
Created on 17 jun. 2022
Se generará un archivo de texto con los datos que se insertaron en la tabla en el ejercicio 2.
- Crear un proceso que pregunte al usuario si desea generar el archivo con todos los registros de la tabla o quiere generarlo con un único registro.
- Si es un único registro, deberá solicitar al usuario un número de folio para buscar en la tabla (FOLIO_ID).
En caso de que el folio no exista, mostrar un mensaje en pantalla que diga que no existe y generar archivo sólo con la cabecera.
Si quiere todos los registros entonces no se le pedirá el folio.

- El archivo deberá tener el siguiente layout (con cabecera):
@author: nestor.solis
'''
#from src.registros.SoloUno import Descargar_registro
from src.registros.Todos import Descargar_todos
from src.registros.SoloUno import Descargar_registro
class Info: 
    def mainmenu(self):
        print(" Banco de datos ".title().center(85, "#"))
        menu=[["1. Descargar todos lo datos"],["2. descargar inico registro por cliente_ID"], ["3. Cerrar agenda"]]
        for i in range(3):
            print(menu[i])
            print("")
        opcion=int(input("Introduzca la opción: "))
        if opcion==1:
            Descargar_todos()
        elif opcion==2:
            Descargar_registro()
        else :
            exit()
        self.mainmenu()


agenda1=Info()
agenda1.mainmenu()