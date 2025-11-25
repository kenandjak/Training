def quick(lista):
    quicksort(lista,0,len(lista)-1)

def quicksort(lista,esquerda,direita):
    if esquerda < direita:
        pivot = lista[(esquerda+direita)//2]
        index = dividindo(lista,esquerda,direita,pivot)
        quicksort(lista,esquerda,index-1)
        quicksort(lista,index,direita)

def dividindo(lista,i,j,pivot):
    while i <= j:
        while lista[i] < pivot:
            i += 1
        while lista[j] > pivot:
            j -= 1
        if i <= j:
            lista[i],lista[j] = lista[j],lista[i]
            i += 1
            j -= 1
    return i 

#vetor = list(map(int,input().split(' ')))
vetor = [2,8,5,6,1,3]
print("Vetor original:",vetor)
quick(vetor)
print("Vetor ordenado:",vetor)
