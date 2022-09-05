"""
		Este programa lo que va a realizar es una concatenacion de caracteres
		alojados en variables para formar cierta frase

"""

texto1 = "Hola"
texto2 = "Mundo"

textoFinal = texto1 +"  "+ texto2  # Esta es la primera forma de como concatenar strings

print(textoFinal)

		# A continuacion la segunda forma de como podemos concatenar al imprimir

print("Saludo: {} {}".format(texto1, texto2))

		# por ultimo la ultima forma de como concatenar es:

print("Saludo: %s %s "%(texto1,texto2))