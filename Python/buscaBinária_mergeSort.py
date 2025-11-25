'''Implementação de algoritmo para ordenar um vetor
e buscar o valor solicitado pelo usuário'''

def merge(v):
    if len(v) > 1:
        meio = len(v)//2
        m_esq = v[:meio]
        m_dir = v[meio:]

        merge(m_esq)
        merge(m_dir)

        i=j=k=0
        while i<len(m_esq) and j<len(m_dir):
            if m_esq[i] < m_dir[j]:
                v[k] = m_esq[i]
                i += 1
            else:
                v[k] = m_dir[j]
                j += 1
            k += 1
        while i < len(m_esq):
            v[k] = m_esq[i]
            i += 1
            k += 1
        while j < len(m_dir):
            v[k] = m_dir[j]
            j += 1
            k += 1
    return v

def buscaBinária(n,v):
    t = len(v)
    inicio = 0
    final = t - 1
    indice = -1
    b = True
    while b and inicio <= final:
        ind = (inicio+final)//2
        meio = v[ind]
        if n == meio:
            indice = ind
            b = False
        else:
            if n < meio:
                print("Número:",meio,"Índice:",ind)
                final = ind - 1
            else:
                print("Número:",meio,"Índice:",ind)
                inicio = ind + 1

    return indice

numero = float(input())
vetor = [27,-5.02,999,2,18.5,-3,45,10,0,21]

print("Vetor original:",vetor)
print("Vetor ordenado:",merge(vetor))
print("Valor do índice buscado:",buscaBinária(numero,vetor))