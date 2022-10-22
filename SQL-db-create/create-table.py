import mysql.connector

ejecon = mysql.connector.connect(
    host = "localhost",
    user = "Jorge",
    password = "1234",
    database = "ejemplo"
    )

#Se crea la query para crear la tabla
sql = "CREATE TABLE CLIENTS (CLIENT_ID INT unsigned NOT NULL AUTO_INCREMENT, NAME VARCHAR(50), LAST_NAME VARCHAR(70),"+\
"ADDRESS VARCHAR(70), FOLIO_ID VARCHAR(20), AMOUNT NUMERIC(10,2), START_DATE DATE, PRIMARY KEY (CLIENT_ID));"

ejecur = ejecon.cursor()
ejecur.execute(sql)
#Se ejecuta el método para mostrar que la tabla se haya creado
ejecur.execute("SHOW TABLES")

for x in ejecur:
    print(x)
