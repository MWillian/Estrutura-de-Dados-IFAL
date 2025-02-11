# Escreva um programa que utiliza a função da questão [5] para alterar o valor de uma variável x. O programa deve parar
# quando x tiver o valor final de 1.
# Por exemplo, para x = 13,a saída será:
# 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
def comparacao(x):
    while x != 1:
        if x % 2 == 0:
            x = x = x / 2
        else:
            x = 3 * x + 1
        print(x)
comparacao(13)
