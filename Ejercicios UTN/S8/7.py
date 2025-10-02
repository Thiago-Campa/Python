#Pídele al usuario una oración y una palabra que desee reemplazar. Luego,
#usa el método replace() para sustituir todas las apariciones de esa
#palabra por la palabra "***CENSURADO***". Imprime la oración resultante.

palabra = input("ingrese una oracion: ")

reemplazar = palabra.lower().replace("boca", "*CENSUARADO*")

print(reemplazar)