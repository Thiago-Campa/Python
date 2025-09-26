diccionario = {
    "nombre" : 'thiago',
    "apellido" : 'campagnaro',
    "seguidores" : '1248'
}

#devuelve las claves
claves = diccionario.keys()
print(claves)

#devuelve los valores por indice
valores = diccionario.get("nombre")
print(valores)

#elimina un elemento del diccionario
eliminar_elemento = diccionario.pop("seguidores")
print(diccionario)

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

#elimina todos los elementos del diccionario
#eliminar = diccionario.clear()
#print(diccionario)

