op=0
def agregarEstudiante(dic, código, nombre):
    dic[código]=[]
    dic[código].append(nombre) #SE AGREGA UNA REFERENCIA A UN OBJETO STRING PARA EL NOMBRE
    dic[código].append([]) #SE AGREGA OTRA REFERENCIA A UN OBJETO DE LISTA (VACÍA) PARA LAS NOTAS
def agregarNota(dic,código,nota):
    dic[código][1] += [nota]
def prom(lista):
    suma=0
    for item in lista:
        suma+=item
    return suma/len(lista)
def imprimir(dic,código):
        print("Código:",código,"; Estudiante:",dic[código][0],"; Notas:",dic[código][1],"; Promedio:",prom(dic[código][1]))
dic={}
while op!=4:
    op=int(input("Escoja una opción:\n1.-Agregar un estudiante\n2.-Agregar una nota a un estudiante\n3.-Consular la información de un estudiante\n4.-Salir\n"))
    if op==1:
        agregarEstudiante(dic,input("Código del estudiante: "),input("Nombre del estudiante: "))
    elif op==2:
        código=input("Introduzca el código del estudiante: ")
        for i in range(int(input("Ingrese el número de notas a ingresar: "))):
            print("Nota",i+1,"= ",end="")
            agregarNota(dic,código,int(input()))
    elif op==3:
        imprimir(dic,input("Ingrese el código: "))
print(dic)