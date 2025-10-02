#Pídele al usuario que ingrese su nombre y apellido, pero pídele
#explícitamente que deje espacios al inicio y al final (ej. " Juan
#Pérez "). Usa el método strip() para eliminar esos espacios
#innecesarios y luego imprime la longitud de la cadena limpia para
#demostrar que los espacios fueron eliminados.

while True: 
    nombreCompleto = input("ingrese sun nombre completo (con espacios al principio y final): ")
    
    if nombreCompleto.startswith(" ") and nombreCompleto.endswith(" "):
        break
    else:
        print("con espacios al principio y final")

print("longitud original: ", len(nombreCompleto))

filtro = nombreCompleto.strip()
print("longitud con filtro: ", len(filtro))

print("nombre en limpio: ", filtro)