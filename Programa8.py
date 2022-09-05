"""
	En este programa se va a trabajar con listas, que son arreglos que son mutables
	es decir se pueden añadir nuevos elementos o cambiar elementos por otros, etc.
"""

lista1 = ["Juan", "Gabriel", 25, 23, "EEUU", 25.45, 2+3j]

print(lista1)

print(lista1[:]) # imprimimos la lista1 desde el primer al ultimo elemento

print(lista1[2]) # imprimimos el elemento de la lista1 que se encuentra en la posicion 2

print(lista1[0:4]) # imprimimos un rango de [0,4) de los elementos de la lista 1

print(lista1[3:]) # imprimimos la lista1 con un rango de elementos de [3,ultimo elemento]

lista1.append("Jose") #Funcion que nos permite agregar elementos a una lista, se agregaran al final

print(lista1)

lista1.insert(2, "María") #Funcion que nos permite insertar elementos en una posicion señalada

print(lista1)

lista1.extend([True, False, 100, 20]) # esta funcion agrega mas elementos al final de una lista

print(lista1)

lista1.remove("EEUU") # Esta funcion elimina un elemento de una lista

print(lista1) 

lista1.pop() # Este funcion elimina el ultimo elemento en una lista

print(lista1) 

lista2 = ["Marco", 1] # creacion de lista 2

lista3 = lista1 + lista2  # Creacion de nueva lista con la union de lista 1 y 2

print(lista2*3) # Multiplicamos la lista 2 por 3, lo cual nos dara la lista con los elementos repetidos 3 veces.

print(lista3) # imprimimos lista 3 que es la union de la lista 1 y 2 

print("Jose" in lista1) #Esta linea nos imprime True si el valor esta dentro de la lista y de lo contrario False

