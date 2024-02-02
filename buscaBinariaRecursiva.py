def busca(n,v,i=0,f=None):
    indice = -1
    if f is None:
        f = len(v) - 1
    if i > f:
        return indice
    else:
        ind = (i+f)//2
        meio = v[ind]
        if n > meio:
            return busca(n,v,(ind+1),f)
        elif n < meio:
            return busca(n,v,i,(ind-1))
        else:
            indice = ind
            return indice

n = int(input())
vetor = [1,2,3,5,12,14,15,21,24,45,46,47,53,86,90,98]
print(busca(n,vetor))