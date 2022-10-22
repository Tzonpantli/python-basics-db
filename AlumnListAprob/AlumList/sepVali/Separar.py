'''
Created on 13 jun. 2022

@author: nestor.solis
'''
def separar_alum():
    archivo_alum=open("Datos_alumno.txt","r")
    alumnos_aprobados=open("Alumnos_apro.txt","w")
    alumnos_reprobados=open("Alumnos_reprobados.txt","w")
    for linea in archivo_alum:
        alumno=linea.rstrip("\n").split(";")
        promedio= alumno[3]
        if(float(promedio) <6.0):
            alumnos_reprobados.write(alumno[0]+";" + alumno[1]+";" +alumno[2]+";" + alumno[3]+"\n")
        else:
            alumnos_aprobados.write(alumno[0]+";" + alumno[1]+";" +alumno[2]+";" + alumno[3]+"\n")  
        
    archivor=archivo_alum.read()
    print("")
    print(archivor)
    archivo_alum.close()
    alumnos_aprobados.close()
    alumnos_reprobados.close()