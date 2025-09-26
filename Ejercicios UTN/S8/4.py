#Pídele al usuario que ingrese una acción. Utiliza un if sencillo para
#verificar si la acción es "SALIR". Si no lo es, usa una f-string para
#confirmar la acción. Si el usuario no ingresa nada (deja la cadena
#vacía), el programa no debería intentar procesar la acción.


accion = int(input("ingrese una accion (1 salir - 2 quedarse): "))

if accion == 1:
    print("saliendo UwU")
elif accion == 2:
    print("elegiste quedarte :)")
else:
    print("decidite capo")