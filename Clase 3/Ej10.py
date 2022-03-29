A = [80,34,80,23,70]
k=150
k2=0
num=1
for i in range (len(A)-1): 
    for j in range (i+1,len(A)):       
        if (A[i]+A[j])<=k:
            print("Pareja "+str(num)+": Persona de "+str(A[i])+" kg con persona de "+str(A[j])+" kg")
            num+=1
            if k2<A[i]+A[j]:
                k2=A[i]+A[j]
print("La suma más grande posible corresponde a:",k2,"kg")
        