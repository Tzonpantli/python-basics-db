import mysql.connector
#Se crea la conexión
conn = mysql.connector.connect(
    host = "localhost",
    user = "Jorge",
    password = "1234",
    database = "ejemplo"
    )

curs = conn.cursor()
#Se crea la query que irá a buscar un dato específico mediante el where
values = "00000000000000000001"
sql = "SELECT * FROM T_GMCAP_001_NEW_CLIENT WHERE CLIENT_FOLIO_ID =" + values
#Se ejecuta la query
curs.execute(sql)
result = curs.fetchall()
print("-----Select con WHERE-----")
print(result)

###Se ejecuta la query que traera todos los campos de todos los registros
##sql = "SELECT * FROM T_GMCAP_001_NEW_CLIENT"
##curs.execute(sql)
##result = curs.fetchall()
##print("-----Select * -----")
##print(result)

###Query que trae los campos CLIENT_NAME y CLIENT_FOLIO_ID de todos los registros
##sql = "SELECT CLIENT_NAME, CLIENT_FOLIO_ID FROM T_GMCAP_001_NEW_CLIENT"
##curs.execute(sql)
##result = curs.fetchone()
##print("-----Select * con fetchone-----")
##print(result)

