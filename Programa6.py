"""
	En este programa tenemos las opciones que nos permite usar python
	para manipular caracteres es decir strings
	lower , upper, title, etc.
"""

texto = "Bienvenidos a mi curso aprenderemos python"

print(texto)
print(texto.lower()) # nos permite colocar todo a miniscula
print(texto.upper()) # nos permite colocar todo a mayuscula
print(texto.title()) # nos permite poner la primer letra de cada palabra en mayuscula
print(texto.find("e")) # nos arroja la posicion en cadena de la letra seleccionada
print(texto.count("i")) # cuenta el numero de repeticiones de una letra.

textofinal = texto.replace("dos","d@s") # Remplaza en la cadena el conjunto de letras por el otro conjunto.
print(textofinal) # imprime el valor de la variable textofinal

print(texto.isnumeric()) #arroja un valor bool dependiendo si la variable texto es o no de tipo numerico.