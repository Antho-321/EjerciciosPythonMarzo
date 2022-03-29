def imprimir(tabla):
    for i in range(len(tabla)):
        print("[",end="")
        for j in range(len(tabla)):
            print("%3s"%tabla[i][j],end="")
        print(" ]")
def llenarSecuencia(n):
    tabla = []
    num=1
    for i in range(n):
        tabla.append([])
        for j in range(n):
            tabla[i]+=[num]
            num+=1
    return tabla
imprimir(llenarSecuencia(5))

