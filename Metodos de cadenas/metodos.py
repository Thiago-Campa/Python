cadena1 = "Hola soy Thiago"
cadena2 = "BIENVENIDO"
cadena3 = "hola"

mayusculas = cadena1.upper()
minusculas = cadena2.lower()
primeraLetraMayuscula = cadena3.capitalize()

#buscamos una cadena en otra cadena
busqueda = cadena1.find("j")

#contar cantidad de caracteres
longitud = len(cadena1)

#verifica si una cadena empieza con un caracter en especifico que ya este dentro de una cadeana
verifica = cadena1.startswith("Ho")

#verifica si una cadena termina con un caracter en especifico que ya este dentro de una cadeana
verifica2 = cadena1.endswith("gO")

#remplaza un pedazo de una cadena por otra cadena existente
reemplazo = cadena1.replace("go", "guinho")

#separa cadenas con la cadena que le pasemos
cadena_nueva = cadena1.split("o")

print(minusculas)
print(mayusculas)
print(primeraLetraMayuscula)
print("la letra esta en la posicion: ", busqueda) #si no encuentra nada devuelve -1
print("la oracion tiene ", longitud, " caracteres")
print(verifica)
print(verifica2)
print(reemplazo)
print(cadena_nueva)