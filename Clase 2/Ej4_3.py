horas = 23
minutos = 59
segundos = 59
print("La hora es: "+str(horas)+":"+str(minutos)+":"+str(segundos))
if horas<=23 and minutos<=59 and segundos<=59:
    segundos+=1
    if segundos==60:
        minutos+=1
        segundos=0
    if minutos==60:
        horas+=1
        minutos=0
    if horas==24:
        horas=0
    print("La hora un segundo después corresponde a: "+str(horas)+":"+str(minutos)+":"+str(segundos))
else:
    print("Ingrese una hora válida.")