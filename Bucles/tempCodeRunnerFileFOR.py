frutas = ["banana", "manzana", "mandarina", "pera", "uva", "kiwi"]
cadena = "hola Thiago"
numeros = [1, 3, 4 ,54, 123]

#evitando que se coma una manzana con la sentencia {continue}
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'me voy a comer una {fruta}')
    
print("bucle terminado")
    
print("---------------------------------")

#evitar que el bucle continue ejecutandose
for fruta in frutas:
    if fruta == 'pera':
        break
    print(f'me voy a comer una {fruta}')
    
print("bucle terminado")
    

#recorriendo una cadena de texto
for letra in cadena:
    print(letra)
    

#recorriendo {for} en un sola linea
numero_duplicados = [x*2 for x in numeros]
print(numero_duplicados)