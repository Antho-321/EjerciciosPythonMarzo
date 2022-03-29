num = 20
r="El número "+str(num)+" es divisible para: "
for i in range(1,num//2+1):
    if num%i==0:
        r += str(i)+", "
r += str(num)
print(r)
