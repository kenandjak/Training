class Caneta:
    def __init__(self,modelo,cor,ponta):
        self.modelo = modelo
        self.cor = cor
        self.ponta = ponta

    def rabiscar(self,tampa):
        if tampa == True:
            print(False)
        else:
            acao = int(input("Escrever(1) ou Pintar(2)?: "))
            if acao == 1:
                print("Escreveu com a cor",self.cor)
            elif acao == 2:
                print("Pintou com a cor",self.cor)

pen = Caneta('Bic','vermelha',0.7)
pen.rabiscar(False)