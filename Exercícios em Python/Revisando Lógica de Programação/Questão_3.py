# Calcule o fatorial de um numero qualquer. O fatorial de um número n é n * (n-1) * (n-2) * ... * 1.
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)
print(f"O fatorial de 4 é {fatorial(4)}")