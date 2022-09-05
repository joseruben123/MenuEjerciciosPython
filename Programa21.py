"""
	En este programa se va a topar el tema de generadores
	Los generadores permiten extrear valores de una funcion y almacenarlo
	(de uno en uno) en onjetops iterables (que se pueden recorrer)
	Sin la necesidad de almacenar todos a la vez
"""

def generarMultiplosDe7(limite): # Esta funcion nos permite crear una lista de numeros que son multiplos del numero 7
	numero = 1
	listaNumeros = []

	while numero <= limite:
		listaNumeros.append( numero*7 )
		numero = numero + 1
	return listaNumeros #Esta funcion retorna la lista de Numeros

	# A continuacion creamos una funcion usando yield que nos permitira obtener un valor a la ves y se consume menos memoria

def GeneradorMult7(limite):
	numero = 1

	while numero <= limite:
		yield numero*7 # Al usar esta funcion nos genera un objeto iterable
		numero = numero + 1

multiplosDe7 = GeneradorMult7(10)

#Usamos la funcion next cuya funcion es de retornar el siguiente elemento de la funcion yield

print(next(multiplosDe7))
print(next(multiplosDe7))

