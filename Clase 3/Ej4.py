saldo = 0
op = 0
while (op!=3):
    print("Saldo actual:",saldo)
    op=int(input("Ingrese una opción:\n1.-Depósito\n2.-Retiro\n3.-Salir\n"))
    if op<0 or op>3:
        print("Opción no válida\n")
        continue
    if op==1:
        saldo+=float(input("Ingrese la cantidad a depositar: "))
    elif op==2:
        cant = float(input("Ingrese la cantidad a retirar: "))
        if cant>saldo:
            print("No se puede retirar esa cantidad\n")
        else:
            saldo-=cant
    else:
        print("Saliendo...")