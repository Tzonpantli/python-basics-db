#Se hace el import del conector de sql
import mysql.connector

#Se crea la conexión mediante el método connect
mcapdb = mysql.connector.connect(
    host = "localhost",
    user = "Jorge",
    password = "1234",
    database = "ejemplo"
    )

#Se crea el cursor
mcapcursor = mcapdb.cursor()

#Se almacena la query SQL en una variable como un String
sql = "INSERT INTO T_GMCAP_001_NEW_CLIENT (CLIENT_NAME, CLIENT_LAST_NAME, " + \
      "CLIENT_ADDRESS, CLIENT_FOLIO_ID, ACCOUNT_AMOUNT, ACCOUNT_START_DATE)" + \
"VALUES (%s, %s, %s, %s, %s, %s)"

#Se crea una tupla que contiene los valores a insertar en la tabla
val = ("Jorge", "Salinas", "San Jorge", "00000000000000000001", 12345.89, "2022-01-01")

#Se llama al método execute del cursor y se pasan como parámetros la query y los valores
mcapcursor.execute(sql, val)

#Se hace el commit para que se guarde lo que se insertó
mcapdb.commit()

#Llamamos al atributo rowcount del cursor para mostrar el número de elementos que se insertaron
print(mcapcursor.rowcount, "Se inserto registro")


#Para insertar varios valores se crea una lista de tuplas, cada una con los valores que se deben insertar
val2 = [("Daniel", "Castillo", "Zaragoza 23", "00000000000000000002", 23148.89, "2021-01-01"),
("Andrea", "Juarez", "Insurgentes 23", "00000000000000000003", 1204897.02, "2022-03-14"),
("Susana", "Flores", "Chapultepec", "00000000000000000004", 5014.78, "2019-10-08")]

#Se llama al método executemany para indicar que serán varios registros los que se insertarán, y recibe también
#dos parámetros, la query y la lista de tuplas a insertar
mcapcursor.executemany(sql, val2)
mcapdb.commit()

print(mcapcursor.rowcount, "Se insertaron datos")
