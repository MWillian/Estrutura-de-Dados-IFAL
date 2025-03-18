def soma_divisores(num,div,soma):
    if div != 0:
        if num % div == 0:
            soma += div
        return soma_divisores(num,div-1,soma)
    else:
        return soma
    
dividendo = 6
divisor = 6
valor_Somar = 0
print(soma_divisores(dividendo,divisor-1,valor_Somar))