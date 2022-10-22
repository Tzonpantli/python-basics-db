'''
Created on 17 jun. 2022
- Crear un proceso que cree la tabla que se describe en el ejemplo.
- Crear otro proceso que lea el archivo NUEVOS_CLIENTES.txt e inserte el contenido en la tabla creada.
El orden de los campos en el archivo es: NOMBRE, APELLIDO, DIRECCION, FOLIO, MONTO, FECHA.
- Mostrar un mensaje que diga que se insertaron los registros, deben insertarse todos en una sola ejecución.
- Mostrar que en la tabla sí se hayan insertado los registros

@author: nestor.solis
'''
import mysql.connector

ejecon = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "clientes"
    )
#sql = "CREATE TABLE CLIENTS (CLIENT_ID INT unsigned NOT NULL AUTO_INCREMENT, NAME VARCHAR(50), LAST_NAME VARCHAR(70),"+\
#"ADDRESS VARCHAR(70), FOLIO_ID VARCHAR(20), AMOUNT NUMERIC(10,2), START_DATE DATE, PRIMARY KEY (CLIENT_ID));"

ejecur = ejecon.cursor()
#ejecur.execute(sql)
ejecur.execute("SHOW TABLES")
for x in ejecur:
    print("Tabla: ",x)
    
def insertar_datos():
    archivo=open("NUEVOS_CLIENTES.txt","r")
    data = [tuple(line.split(";")) for line in archivo]
    query = ("INSERT INTO CLIENTS (NAME,LAST_NAME, " + \
        "ADDRESS,FOLIO_ID,AMOUNT,START_DATE)" + \
        "VALUES (%s, %s, %s, %s, %s, %s)")
    for i in range(len(data)):
        val=list(data[i])
        del val[6]
        print("Se ha subido esta informacion: ")
        print(val)
        ejecur.execute(query, val)
        ejecon.commit()
        print("")
        
insertar_datos()