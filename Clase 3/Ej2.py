n = 10
x = 4
def vasos(n,x):
    total = 0
    while n>=x:
        reciclados = n//x
        sobran = n%x
        total+=reciclados
        n = reciclados + sobran
        print("Reciclados:",reciclados,"; Sobran:",sobran,"; Total de reciclados:",total,"; n:",n)
    return total
print (vasos(n,x))