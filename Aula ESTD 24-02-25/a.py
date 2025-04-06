def ehPerfeito(n,div,soma):
    if div == 0:
       return n == soma
    else:
        if n % div == 0:
            return ehPerfeito(n,div-1,soma+div)
        else:
            return ehPerfeito(n,div-1,soma)
        
def somaperfeito(a,b,soma0,soma1):
    if a == b:
        return soma1
    else:
        if ehPerfeito(a,a-1,0):
            return somaperfeito(a+1,b,soma0,soma1)
        else:
            return somaperfeito(a+1,b,soma0,soma1)
valor1 = 10
valor2 = 20
print(somaperfeito(valor1,valor2,0,0))
