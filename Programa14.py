"""
	manejo de Operadores ternarios ......
"""

sexos = ("hombre", "mujer")
posicion = True
sexo=sexos[posicion] #si le pasamos por argumento un valor de verdad True nos devuelve el 2do elemento
print(sexo)
sexo=sexos[not posicion] #si le pasamos por argumento un valor de verdad False nos devuelve el 2do elemento
print(sexo)
