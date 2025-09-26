#Pídele al usuario que introduzca su edad. Luego, usa una f-string para
#imprimir un mensaje que incorpore la edad y realice un cálculo sencillo,
#por ejemplo: "Tienes {edad} años, y dentro de 5 años tendrás {edad + 5}
#años.

edad = input("ingrese su edad: ")
suma = int(edad) + 5

print(f'ahora tenes {edad} años y dentro de 5 añoas tu edad será de {suma}')