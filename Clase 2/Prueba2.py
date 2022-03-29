límite = int(input("Ingrese el valor del límite: "))
for i in range(1,límite+1):
    if i%3==0:
        print(i,"Fizz",end="")
        if i%5==0:
            print("Buzz",end="")
        print("")
    else:
        if i%5==0:
            print(i,"Buzz")
