from random import randint
def número_ausente(tabla,número):
    for i in range(len(tabla)):
        for j in range(len(tabla)):
            if tabla[i][j]==número:
                return False
            elif i==len(tabla)-1 and j==len(tabla)-1:
                return True
def llenarSecuencia(n):
    tabla = []
    num=1
    for i in range(n):
        tabla.append([])
        for j in range(n):
            tabla[i]+=[num]
            num+=1
    return tabla
def imprimir(tabla):
    for fila in tabla:
        print("[",end="")
        for columna in fila:
            print("%3s"%columna,end="")
        print("  ]")
def comprobarGanador(tabla,símbolo):
    cont1 = 0
    cont2 = 0
    cont3 = 0   
    for i in range(len(tabla)):
        if (tabla[i].count(símbolo)==3):
            return True
        for j in range(len(tabla)):
            if tabla[j][i]==símbolo:
                cont3+=1
                if i==j:
                    cont1+=1
                if i+j==len(tabla)-1:
                    cont2+=1                 
        if cont1==3 or cont2==3 or cont3==3:
            return True
        if cont3!=3:
            cont3=0
    return False
tabla2= llenarSecuencia(3)
if int(input("Seleccione una figura:\n1.-◯\n2.-X\n"))==1:
    fig_user="◯"
    fig_comp="X"
else:
    fig_user="X"
    fig_comp="◯"
empate=False
cont=0
while empate==False and comprobarGanador(tabla2,"X")==False and comprobarGanador(tabla2,"◯")==False:
    print("Escoja una posición:")
    imprimir(tabla2)
    pos_user = int(input())
    pos_comp = randint(1,9)
    if cont!=8:
        while pos_comp==pos_user or número_ausente(tabla2,pos_comp):
            pos_comp = randint(1,9)
    for i in range(len(tabla2)):
        for j in range(len(tabla2)):
            if tabla2[i][j]==pos_user:
                tabla2[i][j]=fig_user
                cont+=1
            if tabla2[i][j]==pos_comp:
                tabla2[i][j]=fig_comp
                cont+=1
    if comprobarGanador(tabla2,fig_user):
        imprimir(tabla2)
        print("¡Ganaste!")
    elif comprobarGanador(tabla2,fig_comp):
        imprimir(tabla2)
        print("Perdiste")
    elif cont>=9:
        imprimir(tabla2)
        print("Es un empate")
        empate=True


