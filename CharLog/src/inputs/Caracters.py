'''
Created on 15 jun. 2022

@author: nestor.solis
'''
class Caracters:
    def inputs(self):
        self.frase=input("Introduzca la frase: ")
        self.letra=input("introduzca la letra: ")
        if(len(self.letra) > 1):
            tabla1="log.txt"
            fichero=open(tabla1,"a")
            fichero.write("ValueError. pedi una sola letra \n")
            print("Error. Solo pedi una letra, el programa se cerrara")
            exit()

    
    def conteo(self):
        conteo=self.frase.count(self.letra)
        print("las veces que aparecees: " + str(conteo))
        
    def imprimir(self):
            try:
                tabla1="log.txt"
                fichero=open(tabla1,"a")
                try:
                    fichero.write("Ok. Sin errores \n")
                    fichero.close()
                except TypeError:
                    fichero.write("TypeError. alguna cosa que se intenta meter en el fichero no es string \n")
                    fichero.close()    
            except FileExistsError:
                fichero.write("FileExistError. el fichero no puede crear uno existente \n")
                fichero.close()
            else:
                print("Todo ha ido correctamente \n")