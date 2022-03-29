dic={}
menu = True
while menu:
    op = int(input("Elija una opción:\n1.-Agregar\n2.Salir\n"))
    if op==1:
        índice = input("Ingrese el índice: ")
        valor = input("Ingrese el valor: ")
        dic[índice]=valor
        print(dic)
    elif op==2:
        menu=False
    else:
        print("Ingrese una opción válida")