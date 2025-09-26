nombre = "Thiago"
apellido = 'Campagnaro'

NombreCompleto = nombre + " " +  apellido

print("nombre completo:",NombreCompleto)

edad = 22
dni = 45266015
peso = 69.3

datos = edad, dni, peso


print(f"datos de {NombreCompleto}:", datos)

bienvenida = "hola " + NombreCompleto + " como estas?"

print(bienvenida)

print("hola " + NombreCompleto + " como estas????")

print("Thiago" in bienvenida)
print("campagnaro" not in NombreCompleto)