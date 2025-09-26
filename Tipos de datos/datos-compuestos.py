#Listas
lista = ["Thiago Campagnaro", "River Plate", True, 22] #la lista se puede modificar (en un futuro se le puede agregar/quitar algo)

print(lista[0])

#Tuplas
tupla = ("Thiago Campagnaro", "River Plate", True, 22) #la tupla no se puede modificar

print(tupla[1], tupla[3])

#Conjunto (set)
conjunto = {"Thiago Campaganro", "River Plate", True, 22} #los conjuntos se pueden modificar

print(conjunto) #no se puede acceder por el indice, ni repetir valores

#Diccionario
diccionario = {
    'nombre' : "Thiago Campagnaro",
    'club' : "River Plate",
    'estado' : True,
    'edad' : 22
}

print(diccionario)
print(diccionario['estado'], diccionario['nombre'])