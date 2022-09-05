"""
	cuando indicamos un adelante del parametros de una funcion, lo que estamos es indicando que se va
	a recibir un numero indeterminado de parametros. Ademas, esos parametros se recibiran en forma de tupla
"""

def devuelveLenguajes(*lenguajes):
	for leng in lenguajes:
		yield from leng       #Esta linea de codigo nos permite hacer una iteracion de los caracteres de cada elemento iterado con el for

lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "Javascript")

print(next(lenguajesObtenidos)) # Devuelve primer caracter del primer elemento

print(next(lenguajesObtenidos)) # Devuelve segundo caracter del segundo elemento



