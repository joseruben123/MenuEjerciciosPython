"""
	En este programa se va hacer uso de operadores logicos
	AND : equivale a Y si ademas ....
	OR : Equivale a o si no....
	NOT : negacion .............
"""
distancia = 1200
numeroHermanos = 3
salarioPadres = 1100
tieneBeneficio = False 

if (distancia > 1000 and numeroHermanos >2 ) or salarioPadres< 2000: #Evaluamos dos condiciones a la ves con un OR, lo cual para que entre en el condicional tiene que cumplirse lo uno o lo otro.
	tieneBeneficio = True

print(tieneBeneficio)

print(not(tieneBeneficio)) #Uso del operador logico NOT para negar el valor de verdad de esa variable

if (100>40) and (19<21): #Condicional con un AND donde la logica es que ambas condiciones se cumplan para que entre al condicional.
	print("Verdad")
