"""
	Uso de la funcion range, la cual crea una tupla inmutable de numeros enteros en sucesion aritmetica.

"""
numeros = range(5) # Creando una lista de numeros del 1 al 4 

print(numeros)

numeros1 = range(4,10) # Creando una tupla de numeros del 4 al 9

numerosConSalto = range(0, 100, 5) #Creando tupla de numeros del 0 al 99 con salto de 5 en 5.

print(list(numerosConSalto)) #conviertiendo a list para poder visualizar los numeros en la impresión de los valores.
