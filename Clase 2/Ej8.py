frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
cont = 0
for carac in frase:
    if carac == letra:
        cont+=1
if cont>0:
    print("La letra " + letra + " se encontró",cont,"veces")
else:
    print("No se encontró la letra \""+letra+"\".")