#Listas
nombre =["harry", "ron","hermione"]
print(nombre)

#Para acceder a un elemento se hace de la siguiente manera
print(nombre[2])

#Para agregar elementos
nombre.append("draco")
print(nombre)

#Para ordenarlas
nombre.sort
print(nombre)

#Sets
conjunto = set()#Se crea el conjunto vacio
#Para agregar un elemento al cojunto
conjunto.add("Damian")
conjunto.add("Pilar")
conjunto.add("Melanie")
conjunto.add("Santiago")

print(conjunto)

#Para eliminar un elemento de un conjunto
conjunto.remove("Santiago")
print(conjunto)

#Para averiguar la longitud del conjunto
print(len(conjunto))

#Diccionarios
casas = {"Harry" : "Grifindor", "Draco" : "Slytherin"}# con el : indicamos que PERTENECE A
print(casas)
#Para consulta a que casa pertenece Harry
print(casas["Harry"])
#Para agregar datos al diccionario
casas["Hermione"] = "Grifindor"
print(casas)