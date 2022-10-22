'''
Created on 17 jun. 2022

@author: nestor.solis
'''
def Descargar_registro():
    import mysql.connector
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234",
        database = "clientes"
        )
    curs = conn.cursor()
    values = input("seleccione el value")
    sql = "SELECT * FROM CLIENTS  WHERE CLIENT_ID =" + str(values)
    curs.execute(sql)
    result = curs.fetchall()#lista
    print(result)
    try:
        if int(values) in result[0]:
            for row in result:
                cliente_id= row[0]
                name=row[1]
                last_name=row[2]
                addres=row[3]
                folio=row[4]
                amount=row[5]
                star=str(row[6])
            archivo=open("CLIENTES_IVA.txt","w")
            archivo.write ("{:<5}|{:<7}|{:<12}|{:<22}|{:<15}|{:<10}|{:<15}\n".format("Id","name", "lastname", "addres","folio","amount","star" +"\n"))
            archivo.write(f"{cliente_id:<5}|{name:<7}|{last_name:<7}|{addres:<15}|{folio:<10}|{amount:<10}|{star:<15}" )
            print("Se descargo exitosamente")
    except:
        print("")
        print("no hay un usuario con ese ID")
        archivo=open("CLIENTES_IVA.txt","w")
        archivo.write("No existe el usuario")