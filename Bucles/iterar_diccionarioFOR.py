diccionario = {
    "nombre" : "thiago",
    "apellido" : "campagnaro",
    "segudores" : 1200
}

#muestras el diccionario completo
for key in diccionario.items():
    print(key)
    
    
#recorre el diccionario por el indice
for datos in diccionario.items():
    clave = datos[0]
    valor = datos[1]
    
    print(f'el indice es: {clave} | el valor es: {valor}')
