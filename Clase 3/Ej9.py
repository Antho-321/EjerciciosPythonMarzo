from random import randint
contaux=0
lista2=[]
def llenarlista(n):
    lista = []
    for i in range(1,n+1):
        print("Nombre ",i,": ",end="")
        lista=lista+[input()]
    return lista
n=int(input("Ingrese el número de participantes: "))
lista1 = llenarlista(n)
while (len(lista2)!=n):
    participante1 = randint(0,n-1)
    participante2 = randint(0,n-1)   
    while lista1[participante1] in lista2:
        participante1 = randint(0,n-1)
    while (participante2==participante1) or (lista1[participante2] in lista2):
        participante2 = randint(0,n-1)
    lista2 = lista2 + [lista1[participante1]]+[lista1[participante2]]
for i in range(0,n-1,2):
    contaux+=1
    aux=i+1
    print("La pareja",contaux,"corresponde a:",lista2[i],"con",lista2[aux])
    