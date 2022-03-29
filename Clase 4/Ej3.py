from random import randint
def imprimir(tabla):
    for i in range(len(tabla)):
        print("[",end="")
        for j in range(len(tabla[i])):
            print("%3s"%tabla[i][j],end="")
        print(" ]")
def imprimir2(tabla):
    for fila in tabla:
        print("[",end="")
        for columna in fila:
            print("%3s"%columna,end="")
        print(" ]")
def llenarAleatorio(n):
    tabla = []
    for i in range(n):
        tabla.append([])
        columnas=randint(1,10)
        for j in range(columnas):
            tabla[i]+=[randint(1,10)]
    return tabla
tabla=llenarAleatorio(5)
imprimir(tabla)
