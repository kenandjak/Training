# Item tem 2 atributos
class Item:
    def __init__(self,dado:str):
        self.dado = dado
        self.proximo = None

class Lista:
    def __init__(self):
        self.inicio = None

    def mostrarLista(self):
        print("INICIO")
        # 1 - atual aponta para Aracomp
        atual = self.inicio
        while atual != None:
            print(atual.dado)
            atual = atual.proximo
            # Atual recebe o próximo, que é UFAL
        print("FIM")
    
    def adicionarInicio(self,texto:str):
        # 1 - Instanciar o item
        item = Item(texto)
        # 2 - Próximo
        item.proximo = self.inicio
        self.inicio = item
    
l1 = Lista()
l1.adicionarInicio('UFAL')
l1.adicionarInicio("Aracomp")
l1.mostrarLista()

