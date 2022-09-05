"""
	*	En este programa vamos hacer uso de diccionarios
		y sus funciones como tal.
	*	los diccionarios son estructuras de datos que nos permiten almacenar distintos valores 
	*	los datos se almacenan asociados a una clave, es decir clave: valor
	* 	para crearlos se usa el simbolo {}
	* 	los valores dentro de un diccionario estan desordenados y se los llama mediante la clave
"""

diccionario1 = { "Pichincha":"Quito", "Azuay":"Cuenca" , "Bolívar":"Guaranda", "Cañar":"Azogues", "Carchi":"Tulcan", "Chimborazo":"Riobamba", "Cotopaxi":"Latacunga", "El Oro":"Machala", "Esmeraldas":"Ciudad Esmeraldas", "Galápagos":"Puerto Baquerizo Moreno", "Guayas":"Guayaquil", "Imbabura":"Ibarra", "Loja":"Loja", "Los Rios":"Babahoyo", "Manabí":"Portoviejo", "Morona Santiago":"Macas", "Napo":"Tena", "Orellana":"Francisco de Orellana", "Pastaza":"Puyo", "Santa Elena":"Santa Elena", "Santo Domingo de los Tsáchilas":"Santo Domingo", "Sucumbíos":"Nueva Loja", "Tungurahua":"Ambato", "Zamora Chinchipe":"Zamora"}

print(diccionario1)
print("")

print("La capital de la provincia de Guayas es: ",diccionario1["Guayas"])

diccionario1["Pichincha"]="Quito_capitalDelEcuador" #Aqui remplazamos el valor de la llave Pichincha por otro valor

diccionario1["Ecuador"]="Quito" #Esta linea nos permite sobreescribir el valor de la llave o crear una nueva llave con dicho valor.

print(diccionario1)

del diccionario1["Ecuador"] #Esta funcion del nos sirve para eliminar el elemento señalado del diccionario

print("\n",diccionario1)

dicionarioEdades = {"Roberto":18 ,"Joselin":22, "Esther":35, "Marcos":51}

print("Edad de Roberto :",dicionarioEdades["Roberto"]) #imprimimos la edad de Roberto del diccionario
print("")

llaves = ("Pichincha", "Azuay", "Loja") #Creamos una tupla con las llaves del nuevo diccionario que vamos a crear

diccProvincias = {llaves[0]:"Quito" , llaves[1]:"Cuenca", llaves[2]:"Loja"} #Creacion de un diccionario con llaves extraidas de la tupla anterior
print(diccProvincias)

print("") #Esto colocamos para que imprima un espacion entre impresiones y no quede todo mezclado

datosPersonales = {"Jose":23, "Años":{1:2010, 2:2011, 3:2012, 4:2013, 5:2014, 6:2015}}
print(datosPersonales["Años"]) # Devuelve el valor de la llave Años que seria otro diccionario

print(datosPersonales.get("Jose","Humberto")) #Esta funcion get, nos sirve para devolver el valor de la llave colocada como primer parametro y si no la encuentra devuelve el segundo parametro.

print(datosPersonales.keys()) # Imprime las llaves del diccionario datosPersonales

valores = list(datosPersonales.values()) #Esta linea de codigo nos permite convertir en lista a los valores del diccionario datosPersonales
print(valores)
