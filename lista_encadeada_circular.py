'''Listas Circulares'''

class Item:
    def __init__(self,nome:str,nota:float):
        self.nome = nome
        self.nota = nota
        self.proximo = None
        self.anterior = None

class Lista:
    def __init__(self):
        self.cursor = None
    
    def listaVazia(self):
        if self.cursor == None:
            return True
        return False
    
    def mostrarLista(self):
        ponteiro = self.cursor

        if ponteiro != None:
            print(ponteiro.nome,':',ponteiro.nota)
            ponteiro = ponteiro.proximo

        while ponteiro != self.cursor:
            print(ponteiro.nome,':',ponteiro.nota)
            ponteiro = ponteiro.proximo

    def mostrarReverso(self):
        ponteiro = self.cursor.anterior
        if ponteiro != None:
            print(ponteiro.nome,':',ponteiro.nota)
            ponteiro = ponteiro.anterior

        while ponteiro != self.cursor.anterior:
            print(ponteiro.nome,':',ponteiro.nota)
            ponteiro = ponteiro.anterior

    def inserirInicio(self,nome:str,nota:float):
        bloco = Item(nome,nota)
        if self.cursor == None:
            bloco.proximo = bloco
            bloco.anterior = bloco
            self.cursor = bloco
        else:
            self.cursor.anterior.proximo = bloco
            bloco.anterior = self.cursor.anterior
            bloco.proximo = self.cursor
            self.cursor.anterior = bloco
            self.cursor = bloco

    def inserirFinal(self,nome:str,nota:float):
        bloco = Item(nome,nota)
        if self.cursor == None:
            bloco.proximo = bloco
            bloco.anterior = bloco
            self.cursor = bloco
        else:
            self.cursor.anterior.proximo = bloco
            bloco.anterior = self.cursor.anterior
            bloco.proximo = self.cursor
            self.cursor.anterior = bloco
    
    def buscaNome(self,nome:str):
        index = 0
        start = self.cursor
        ponteiro = self.cursor
        while ponteiro:
            if ponteiro.nome == nome:
                print(ponteiro.nome,':',ponteiro.nota)
                ponteiro = ponteiro.proximo
                index += 1
                if ponteiro == start:
                    break
            else:
                ponteiro = ponteiro.proximo
                if ponteiro == start:
                    break
        if index == 0:
             print('O nome',nome,'não está na lista.')

    def retiraNome(self,nome:str):
        index = 0
        ponteiro = self.cursor
        while ponteiro:
            # lista unitária
            if  ponteiro.nome == nome and self.cursor.proximo == self.cursor:
                self.cursor = None
                index += 1
                break
            if ponteiro == self.cursor and ponteiro.nome == nome:
                ponteiro.anterior.proximo = ponteiro.proximo
                ponteiro.proximo.anterior = ponteiro.anterior
                self.cursor = ponteiro.proximo
                ponteiro = ponteiro.proximo
                index += 1
            else:
                if ponteiro.nome == nome:
                    ponteiro.anterior.proximo = ponteiro.proximo
                    ponteiro.proximo.anterior = ponteiro.anterior
                    ponteiro = ponteiro.proximo
                    index += 1
                    if ponteiro == self.cursor:
                        break
                else:
                    ponteiro = ponteiro.proximo
                    if ponteiro == self.cursor:
                        break
        if index == 0:
            print('O nome',nome,'não está na lista.')

    def esvaziar(self):
        self.cursor = None
    
    # Lista encadeada em vetor
    def listaEncadeadaVetor(self):
        vetor = []
        ponteiro = self.cursor
        if ponteiro != None: 
            vetor.append(ponteiro)
            ponteiro = ponteiro.proximo

        while ponteiro != self.cursor:
            vetor.append(ponteiro)
            ponteiro = ponteiro.proximo
        return vetor

    # Elementos de um vetor numa lista encadeada
    def vetorListaEncadeada(self,vetor):
        tam = len(vetor)
        i = 0
        while i < tam:
            self.inserirInicio(vetor[i],vetor[i+1])
            i += 2
        
    # Retornar número de nós
    def numeroNos(self):
        vetor = self.listaEncadeadaVetor()
        return len(vetor)


l1 = Lista()
print('Lista vazia?',l1.listaVazia())
print()
print('Lista com elementos:')
l1.inserirInicio('Daniel',9.5)
l1.inserirInicio('Cecília',9.8)
l1.inserirInicio('Aline',10)
l1.inserirFinal('Rafael',8.75)
l1.inserirFinal('Sandra',7.7)
l1.inserirFinal('Rafael',5)
l1.inserirFinal('Aline',10)
l1.mostrarLista()
print()
print()
print('Lista Reversa:')
l1.mostrarReverso()
print()
print()
print('Lista vazia?:',l1.listaVazia())
print()
print()
print('Busca: Aline')
l1.buscaNome('Aline')
print()
print('Busca: Daniel')
l1.buscaNome('Daniel')
print()
print('Busca: Rafael')
l1.buscaNome('Rafael')
print()
print()
print('Remoção: Aline')
l1.retiraNome('Aline')
l1.mostrarLista()
print()
print('Remoção: Sandra')
l1.retiraNome('Sandra')
l1.mostrarLista()
print()
print('Remoção: Lara')
l1.retiraNome('Lara')
print()
print('Remoção: Rafael')
l1.retiraNome('Rafael')
l1.mostrarLista()
print()
print()
print('Esvaziar:')
l1.esvaziar()
l1.mostrarLista()
print('Lista vazia?:',l1.listaVazia())
print()
print("Número de Nós:")
print(l1.numeroNos())
print()
print("Lista encadeada em vetor:")
print(l1.listaEncadeadaVetor())

l2 = Lista()
vetor = ['Ana',10,'Beto',9,'Carol',8]
print()
print("Transformar vetor em lista encadeada")
l2.vetorListaEncadeada(vetor)
l2.mostrarLista()