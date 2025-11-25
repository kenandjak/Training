def recursivo(n):
    if n > 1:
        return n * recursivo(n-1)
    else:
        return 1

def iterativo(n):
    fatorial = 1
    if n > 1:
        fatorial = n
        i = 1
        while n > i:
            fatorial = fatorial * (n-i)
            i += 1
    return fatorial

print('Forma recursiva:',recursivo(4))
print('Forma iterativa:',iterativo(6))