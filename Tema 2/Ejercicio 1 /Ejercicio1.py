"""
Escribe una función en el lenguaje de programación Python llamada
rnd_word(fitxategi1, fitxategi2) que lea el primer archivo línea por línea, seleccione
una palabra aleatoria de cada línea y la escriba en el segundo archivo. Utiliza la
función choice del módulo random.
"""
import random
def rnd_word(archivo1, archivo2):
    palabrasSeleccionadas=[]
    ar1=open(archivo1,'r')
    lineas = ar1.readlines()

    for linea in lineas:
        palabras = linea.split()
        if palabras:
            palabra_aleatoria = random.choice(palabras)
            palabrasSeleccionadas.append(palabra_aleatoria)
    ar1.close()

    ar2=open(archivo2,'w')
    for palabra in palabrasSeleccionadas:
        ar2.write(palabra+"\n")
    ar2.close()
rnd_word('archivo1.txt','archivo2.txt')