def imprimir(dic):
    for índice in dic:
        print("Producto:",índice,"Precio:",dic[índice])
dic={}
menu = True
while menu:
    op = int(input("Elija una opción:\n1.-Agregar producto\n2.-Facturar\n3.-Salir\n"))
    if op==1:
        índice = input("Ingrese el índice: ")
        valor = float(input("Ingrese el valor: "))
        dic[índice]=valor
        print(dic)
    if op==2:
        total=0
        factura=True
        while factura:
            imprimir(dic)
            print("Elija una opción:\n1.-Agregar a factura\n2.-Finalizar")
            opf=int(input())
            if opf==1:
                índice = input("Ingrese el producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                if dic.get(índice) is None:
                    print("Producto no encontrado")
                else:
                    total += float(dic[índice])*cantidad
                    print("El total es:",total)
            else:
                factura=False
                total=0
    elif op==3:
        menu=False
