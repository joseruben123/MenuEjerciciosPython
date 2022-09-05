"""
	While: Bucle repetitivo que nos permite realizar multiples repeticiones basados en el resultado de una condicion logico
	si esta condicion es positiva entonces el bucle se mantiene y con False se sale del bucle.	
"""
indice = 1

while indice < 10:
	print("Valor actual : {0} ".format(indice))
	indice=indice+1

num = 2
print("A continuacion numeros pares......")

while num < 100:

	print("Numero par : {0} ".format(num))

	num += 2

print("Hemos terminado el bucle while...")