from random import randint
zonaUsuario = int(input("¿En qué zona quiere disparar?: "));
zonaPortero = randint(1,6)
print("La zona cubierta por el portero es:",zonaPortero)
if zonaUsuario==zonaPortero:
    print("No ha sido un gol")
else:
    print("¡Gooool!")