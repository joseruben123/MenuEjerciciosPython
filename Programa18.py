"""
	EJERCICIO PARA PODER CREAR EL FACTORIAL DE UN NUMERO....
	USAREMOS BUCLE, LA FUNCION RANGE Y CONDICIONAL
"""

numero = int (input("Ingrese el numero que desea sacarle el factoria.................. "))

resultado = 1

for indice in range(1 , (numero+1)):  # Bucle que itera un rango de numeros desde 1 hasta el numero ingresado + 1

	resultado = resultado*indice



print("El resultado del factorial del numero {}  es :  {} ".format(numero, resultado))