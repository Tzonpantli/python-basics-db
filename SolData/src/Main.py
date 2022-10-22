'''
Created on 15 jun. 2022
Realizar un menú con las siguientes opciones:
[1] – Solicitar palabras Data
[2] – Ver palabras Data
[0] – Exit
Realizar una función carga_() que lea un archivo llamado palabras.txt:
El fichero tendrá una(s) palabra(s) Data por línea.
No hay que separar las palabras Data con ningún carácter, solo enter.
El fichero se leerá línea a línea, guardando la palabra Data correspondiente como un nuevo elemento de una lista.
La función devolverá una lista de palabras Data.
Cuando se introduzca la opción de menú [1], se invocará a la función carga_() 
La lista resultante se asignará a una variable del programa llamada  palabras.
Cuando se introduzca la opción de menú [2], se mostrará el listado de palabras Data de 5 en 5, 
es decir, una vez mostradas 5 palabras Data, el usuario deberá pulsar la tecla enter para ver las siguientes 
(realizar con un while y count del total e ir barriendo hasta mostrar todo)
Cuando se introduzca la opción de menú [0], el programa finalizará.
@author: nestor.solis
'''
from src.data_input.input import carga
from src.show.Showlist import lista
class Data_recurso: 
    def mainmenu(self):
        print(" agenda ".title().center(85, "#"))
        menu=[["1. Solicitar palabras"],["2. Lista de palabras"],["3. Salir"]]
        for i in range(3):
            print(menu[i])
        opcion=int(input("Introduzca la opción: "))
        if opcion==1:
            carga()
        elif opcion==2:
            lista(self)
        elif opcion==3:
            exit()
        self.mainmenu()

  
agenda1=Data_recurso()
agenda1.mainmenu()
