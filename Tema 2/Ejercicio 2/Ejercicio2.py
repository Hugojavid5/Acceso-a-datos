"""
Escribe una función en el lenguaje de programación Python que reciba una oración,
elija dos palabras aleatorias de ella y forme una nueva palabra usando esas dos
palabras. Para crear la nueva palabra, los caracteres se seleccionarán
aleatoriamente de cada una de las dos palabras, uno por uno. Ejemplo: si palabra1
= 'casa' y palabra2 = 'voy', el primer carácter de la nueva palabra se elegirá
aleatoriamente entre los caracteres de 'c' y 'v'. Supongamos que se elige 'v',
entonces el siguiente carácter se elegirá aleatoriamente entre 'c' y 'o'. Repetiendo
este procedimiento con todos los caracteres, el resultado podría ser una palabra como 'vcaoysa’
"""
import random
def palabrasRandom(oracion):
    palabras=oracion.split()

    if len(palabras)<2:
        print("La oracion debe tener minimo dos palabras")

    palabra1, palabra2 = random.sample(palabras, 2)
    longitud_minima = min(len(palabra1), len(palabra2))
    palabrasRandom = []
    for i in range(longitud_minima):
        palabrasRandom.append(random.choice([palabra1[i], palabra2[i]]))
    if len(palabra1) > longitud_minima:
        palabrasRandom.extend(palabra1[longitud_minima:])
    elif len(palabra2) > longitud_minima:
        palabrasRandom.extend(palabra2[longitud_minima:])
    return ''.join(palabrasRandom)

oracion = "La casa es grande y voy corriendo"
resultado = palabrasRandom(oracion)
print("Nueva palabra formada:", resultado)