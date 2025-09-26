password = "123t"
nuevaPass = "123t"


if nuevaPass == password:
    print("podes pasar")
else:
    print("incorrecto") 
    
    
#IF ANIDADO ---------------------------
saldo = 700000
gasto_menusual = 700000


if saldo < 500000:
    print("sos pobre amigo :C")
elif saldo >= 500000 & saldo <= 1000000:
    if saldo - gasto_menusual < 0:
        print("amigo, no sabes manejar la plata")
    elif gasto_menusual - saldo > 30000 :
        print("podes vivir bien")
    else:
        print("llegas con lo justo")
else:
    print("estas cheto bien")
    
    