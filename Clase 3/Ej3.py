from random import randint
def ppt(op):
    if op==1:
        r="piedra"
    elif op==2:
        r="papel"
    else:
        r="tijera"
    return r
ganadas = 0
ganadasMáquina = 0
while ganadas<3 and ganadasMáquina<3:
    opUsuario = int(input("Ingrese una opción:\n1.-Piedra\n2.-Papel\n3.-Tijera\n"))
    if opUsuario>3 or opUsuario<1:
        print("Ingrese una opción válida")
        continue
    opMáquina = randint(1,3)
    print("El usuario eligió:",ppt(opUsuario))
    print("La máquina eligió:",ppt(opMáquina))
    if (opUsuario==1 and opMáquina==3) or (opUsuario==2 and opMáquina==1) or (opUsuario==3 and opMáquina==2):
        print("Gana el usuario")
        ganadas+=1
    elif opUsuario==opMáquina:
        print("Es un empate")
    else:
        print("Gana la máquina")
        ganadasMáquina+=1
    print("Ganadas del usuario:",ganadas)
    print("Ganadas de la Máquina:",ganadasMáquina,"\n")
