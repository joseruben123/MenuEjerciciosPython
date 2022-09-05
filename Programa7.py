"""
	Uso de tuplas. Que son arreglos que son inmutables.
"""

tupla = ( 1 , 2 , 3 , 4 )

tupla1= ( 5 , 6 , 7 , 8 , 9 , 10)

tupla2 = ( 8, 9, "Felipe","Raul",False,True,12.50,23+2j)

tupla3 = ( tupla , tupla2)

tuplaFinal= tupla + tupla1

a, b, c, d = tupla

"""
		En esta seccion del codigo se imprimiran las tuplas creadas anteriormente
		tal como fueron definidas, por tramos o elementos de ellas.
"""
print("primer tupla: ", tupla)
print("segunda tupla creada: ",tupla1)
print("tercer tupla creada on valores de muchos tipos: ",tupla2)
print("cuarta tupla creada, contiene las dos primeras tuplas en sus elementos: ",tupla3)
print(" ")
print("Ultimo elemento de la primer tupla: ",tupla[-1])

print("Elemento en el indice 2 de la primer tupla: ",tupla[2])

print(tupla2[2:5])

print(tuplaFinal)

print("estos son los valores de la primer tupla creada almacenados en variables: \n {} {} {} {}".format(a,b,c,d))

print("numero de veces que se repite el 8 en la tupla1: ",tupla1.count(8))

print("Este es el indice donde se encuentra el nombre Raul en la tupla2: ",tupla2.index("Raul"))
