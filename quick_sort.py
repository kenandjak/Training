def quick(v):
    if len(v) <= 1:
        return v
    else:
        pivot = v[len(v)//2]
        esq = [x for x in v if x < pivot]
        mid = [x for x in v if x == pivot]
        dir = [x for x in v if x > pivot]
        return quick(esq) + mid + quick(dir)
    
vetor = list(map(int,input().split(" ")))
print("Vetor ordenado:",quick(vetor))