# Imprima a seguintetabela usando fors encadeados:
# 1
# 2 4
# 3 6 9
# 4 8 12 16
# n n*2 n*3 .... n*n


def escada (n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i*j,end=' ')
        print()
escada(n=6)
