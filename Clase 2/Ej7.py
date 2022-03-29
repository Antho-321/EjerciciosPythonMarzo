altura = 5*2
for i in range (altura+1):
    if i%2!=0:
        for j in range(altura-i):
            print(" ",end="")  
        for k in range(i):
            print("* ",end="")        
        print("")