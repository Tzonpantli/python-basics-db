'''
Created on 16 jun. 2022

@author: nestor.solis
'''
import mysql.connector
mcapdb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "animales"
    )
mcapcursor = mcapdb.cursor()
sql = "INSERT INTO felinos_001 (NOMBRE, ESPECIE, " + \
    "POBLACION, LUGAR_ORIGEN, PESO_PROMEDIO, ESPERANZA_VIDA)" + \
    "VALUES (%s, %s, %s, %s, %s, %s)"
    
class Felino:
    def __init__(self):
        self.nombre= input("ingrese el nombre: ")
        self.especie=input("ingrese la especie: ")
        self.poblacion=int(input("que poblacion tiene: "))
        self.lugarOrigen=input("ingrese su lugar de origen: ")
        self.pesoProm=int(input("ingrese su peso promedio: "))
        self.esperanzaVida= int(input("ingrese su esperanza de vida: "))
        if(self.especie=="gato"):
            val = ("{}".format(self.nombre), "Gato", self.poblacion, self.lugarOrigen, self.pesoProm, self.esperanzaVida)
            mcapcursor.execute(sql, val)
            mcapdb.commit()
            print("Se inserto registro de un gato")
        elif(self.especie=="leon"):
            val2 = ("{}".format(self.nombre), "Leon", self.poblacion, self.lugarOrigen, self.pesoProm, self.esperanzaVida)
            mcapcursor.execute(sql, val2)
            mcapdb.commit()
            print("Se inserto registro de un leon")
        elif(self.especie=="pantera"):
            val3 = ("{}".format(self.nombre), "Pantera", self.poblacion, self.lugarOrigen, self.pesoProm, self.esperanzaVida)
            mcapcursor.execute(sql, val3)
            mcapdb.commit()
            print("Se inserto registro de una Pantera")
        elif(self.especie=="jaguar"):
            val4 = ("{}".format(self.nombre), "Jaguar", self.poblacion, self.lugarOrigen, self.pesoProm, self.esperanzaVida)
            mcapcursor.execute(sql, val4)
            mcapdb.commit()
            print("Se inserto registro de un Jaguar")
        else:
            print("no hay registros para almacenar a esa especie, solo se pueden almacenar gatos, leones, panteras y jaguares")
            

intancia= Felino
intancia()
