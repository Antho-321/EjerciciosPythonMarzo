A = [2,3,2,6,7,2,8]
for i in range((len(A)-1),-1,-1):
    #print("A = "+str(A)+"; i: "+str(i)+"; A[i] = "+str(A[i])+"; A[:i] = "+str(A[:i]))
    if A[i] in A[:i]:
        del(A[i])
print(A)