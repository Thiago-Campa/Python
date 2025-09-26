lista = list([22, True])

#devuelve cantidad de elementos de la lista
resultado = len(lista)
print("cantidad de elementos de la lista: ", resultado)

#agregando un elemento a la lista (al final)
lista.append("2033")
print(lista)

#agregar un elemento en un indice especifico
lista.insert(1, "Francia")
print(lista)

#agregar varios elementos a la lista
lista.extend([False, 2333, ])
print(lista)

#elimando un elemento de una lista por su indice
lista.pop(1) #-1 para eliminar el ultimo elemento, -2 para eliminar el anteultimo y asi...
print(lista)

#remueve un elemento de la lista por su valor
lista.remove("2033")
print(lista)

#ordena los elementos de forma ascendente (mayor a menor); -> lista.sort(reverse=True) para ordenar de menor a mayor
lista.sort()
print(lista)

#invierte los elementos de la lista
lista.reverse()
print(lista)

#elimina todo los elementos de la lista
#lista.clear()
#print(lista)