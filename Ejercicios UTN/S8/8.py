#Define una variable email con una dirección de correo electrónico de
#ejemplo. Escribe dos expresiones que impriman True o False dependiendo
#si la cadena cumple con: Contiene el carácter "@" y termina con ".com".

correo = input("ingres su correo: ")

print("contiene arroba '@'? : " , "@" in correo)
print("termina con '.com'? :",correo.endswith(".com"))