'''
Created on 15 jun. 2022

Ejercicio 1
Realizar una función que reciba una frase (Texto de caracteres) y una letra
Desplegar el número el número de veces que aparece la letra en la frase.
- Manejar excepciones y guardar en un archivo log.txt todos los errores 
que se hayan acumulado en el llamado de la función, es decir sobreescribir el archivo

@author: nestor.solis
'''
from src.inputs.Caracters import Caracters

intancia=Caracters()
intancia.inputs()
intancia.conteo()
intancia.imprimir()