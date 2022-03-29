aciertos = int(input("Ingrese el número de respuestas correctas: "))
desaciertos = int(input("Ingrese el número de respuestas incorrectas: "))
total = aciertos + desaciertos
pAciertos = (aciertos/total)*100
pDesaciertos = (desaciertos/total)*100
print("Su puntaje final fue: "+str(aciertos)+"/"+str(total))
print("Su porcentaje de aciertos corresponde a: %.2f . Mientras su porcentaje de desaciertos es: %.2f"%(pAciertos,pDesaciertos))