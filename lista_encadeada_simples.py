class Item:
    def __init__(self,nome:str,nota:float):
        self.nome = nome
        self.nota = nota
        self.proximo = None

class Lista:
    def __init__(self):
        self.inicio = None

    def mostrarLista(self):
        ponteiro = self.inicio
        while ponteiro != None:
            print(ponteiro.nome,':',ponteiro.nota)
            ponteiro = ponteiro.proximo
    
    def listaVazia(self):
        if self.inicio == None:
            return 'True'
        return 'False'

    def inserirInicio(self,nome:str,nota:float):
        bloco = Item(nome,nota)
        bloco.proximo = self.inicio
        self.inicio = bloco

    def inserirFinal(self,nome:str,nota:float):
        bloco = Item(nome,nota)
        ponteiro = self.inicio
        ultimo = None
        while True:
            if ponteiro == None:
                break
            else:
                ultimo = ponteiro
                ponteiro = ponteiro.proximo
        ultimo.proximo = bloco

    # Procura pelo nome - digita o nome e revela a nota
    def buscaNome(self,nome:str):
        index = 0
        ponteiro = self.inicio
        while ponteiro:
            if ponteiro.nome == nome:
                print(ponteiro.nome,':',ponteiro.nota)
                ponteiro = ponteiro.proximo
                index += 1
            else:
                ponteiro = ponteiro.proximo
        if index == 0:
            print('O nome',nome,'não está na lista.')
    
    def retiraNome(self,nome:str):
        index = 0
        ponteiro = self.inicio
        while ponteiro:
            if self.inicio.nome == nome:
                self.inicio = self.inicio.proximo
                index += 1
            if ponteiro.proximo and ponteiro.proximo.nome == nome:
                ponteiro.proximo = ponteiro.proximo.proximo
                index += 1
            else:
                ponteiro = ponteiro.proximo
        if index == 0:
            print('O nome',nome,'não está na lista.')
    
    def esvaziar(self):
        self.inicio = None

lista = Lista()

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