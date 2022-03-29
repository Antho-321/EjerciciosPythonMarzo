días = int(input("Ingrese el número de días: "))
años = días//365
meses = (días%365)//30
semanas = ((días%365)%30)//7
días2 = ((días%365)%30)%7
print(días,"días equivalen a:",años,"años,",meses,"meses,",semanas,"semanas y",días2,"días")