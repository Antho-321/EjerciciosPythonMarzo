from random import randint
trueanswer=0
answer=0
aciertos=0
while (trueanswer==answer):
    num1 = randint(1,10)
    num2 = randint(1,10)
    num3 = randint(1,4)
    print("Ingrese la respuesta a la siguiente operación:")
    if num3==1:
        trueanswer = num1+num2
        print(num1,"+",num2,"=",end=" ")
        answer=float(input())
    elif num3==2:
        trueanswer = num1-num2
        print(num1,"-",num2,"=",end=" ")
        answer=float(input())
    elif num3==3:
        trueanswer = num1*num2
        print(num1,"*",num2,"=",end=" ")
        answer=float(input())
    else:
        trueanswer = num1/num2
        print(num1,"/",num2,"=",end=" ")
        answer=float(input())
    if trueanswer==answer:
        aciertos+=1
    print("Aciertos:",aciertos)