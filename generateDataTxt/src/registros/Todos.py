'''
Created on 17 jun. 2022

@author: nestor.solis
'''
def Descargar_todos():
    import mysql.connector
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234",
        database = "clientes"
        )
    curs = conn.cursor()
    sql = "SELECT * FROM CLIENTS"
    curs.execute(sql)
    result = curs.fetchall()#traera todos los registros asi sean 1 millon
    archivo=open("CLIENTES2_IVA.txt","a")
    archivo.write ("{:<5}|{:<7}|{:<12}|{:<22}|{:<15}|{:<10}|{:<15}\n".format("Id","name", "lastname", "addres","folio","amount","star" +"\n"))
    for row in result:
            cliente_id= row[0]
            name=row[1]
            last_name=row[2]
            addres=row[3]
            folio=row[4]
            amount=row[5]
            star=str(row[6])
            archivo.write(f"{cliente_id:<5}|{name:<7}|{last_name:<12}|{addres:<22}|{folio:<15}|{amount:<10}|{star:<15}" +"\n")
    print("Se  han descargado los datos satisfactoriamente")