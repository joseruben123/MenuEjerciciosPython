"""
	Uso de los bucles, para crear un control de flujo que repite 1 o varias lineas de codigo en n veces posibles

"""

for num in range(1 ,13): #bucle que nos itera una tupla de 13 elementos desde el 0 al 12
	print("  {0} x {1}  =  {2}".format(5, num, (5*num))) #linea de codigo en la cual se puede imprimir una tabla de multiplicar

for name in ["Roberth", "Sofi", "Maria", "Romina", "Ximena", "Paul", "Estiven"]: # bucle que nos itera una lista de nombres
	print("La cantidad de letras que existen en el nombre ; {0}   es : {1} ".format(name, len(name)))
