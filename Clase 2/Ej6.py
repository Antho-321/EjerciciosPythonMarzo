def Bisiesto(año):
    if año%4==0:
        if año%100==0:
            return año%400==0
        else:
            return True
    else:
        return False
añoInicio = 1500
añoFin = 2022
r = "Los años bisiestos entre "+str(añoInicio)+" y "+str(añoFin)+" y múltiplos de 10 corresponden a:"
for i in range(añoInicio,añoFin+1):
    if Bisiesto(i) and i%10==0:
        r+= str(i)+", "
print(r)