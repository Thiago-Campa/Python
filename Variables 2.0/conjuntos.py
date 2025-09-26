#creando un conjunto con "set"
conjunto = set({"dato1", "dato2"}) #no se pude modificar

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato2", "dato3"])
conjunto2 = {conjunto1, "dato4"}

conjunto3 = {1,3,5,7,9}
conjunto4 = {1,5,7}

#verifica si es un subconjunto con funcion
resultado = conjunto4.issubset(conjunto3)

#verifica si es un subconjunto con <=
resultado2 = conjunto4 <= conjunto3

#verifica si es un superconjunto
resultado3 = conjunto3 > conjunto4

#verifcica si son distitnos
conjunto5 = {2,4,6,8}
resultado4 = conjunto5.isdisjoint(conjunto3) #si hay un solo elemento que coincide, lo toma como que es igual

print(conjunto2)
print(resultado)
print(resultado2)
print("el conjunto3 es un superconjunto de conjunto4 ?: ", resultado3)
print("el conjunto3 es distinto al conjunto5?: ", resultado4)