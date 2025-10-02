animales = ["gato", "perro", "loro", "cocodrilo"]

#recorriendo lista animales
for animal in animales:
    print(f'ahopora la variable animal es igual a: {animal}')
    
    
numeros = [32, 233, 434, 54]

#recorriendo lista numeros y multiplicando cada numero
for numero in numeros:
    resultado = numero * 10
    print("resultado de la multiplicacion:",resultado)
    

#recorriendo dos listas
for numero, animal in zip(animales, numeros):
    print(f'recorriendo lista 1: {numero}')
    print(f'recorriendo lista 2: {animal}')
    

#recorrer una lista con rango 
for num in range(5,11):
    print(num)
    

#forma correcta de recorrer una lista con indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    
    print(f'el indice es: {indice} y el valor es: {valor}')
    
    
#usando else en for
for numero in numeros:
    print(f'ejecutando el ultimo bloque, valor actual: {numero}')
else:
    print("el bucle termino")
