'''Write your own book!!!!!!!!'''

class Caneta:
    def __init__(self,modelo,cor,ponta):
        self.modelo = modelo
        self.cor = cor
        self.ponta = ponta

    def rabiscar(self,tampa):
        if tampa == 'True':
            rabisco = ' '
            return "Caneta tampada. Página em branco."
        else:
            acao = int(input("Escrever(1) ou Pintar(2)?: "))
            if acao == 1:
                rabisco = input("Escreva: ")
            elif acao == 2:
                rabisco = f"Pintou com a cor {self.cor}"
        return rabisco
                

print("~~~Minha caneta~~~")
m = input("Modelo: ")
c = input("Cor: ")
p = float(input("Ponta: "))
pen = Caneta(m,c,p)


class Livro:
    def __init__(self,autor,ano,tema,caneta):
        self.autor = autor
        self.ano = ano
        self.tema = tema
        self.caneta = caneta
        self.capa = False
    
    def openn(self):
        if self.capa:
            print("O livro já está aberto.")
        else:
            self.capa = True
            print("Livro aberto!")

    def close(self):
        if self.capa == False:
            print("O livro já está fechado.")
        else:
            self.capa = False
            print("Fechando...")

    def escrever(self):
        if self.capa:
            print("A caneta está com tampa?(True or False)")
            return self.caneta.rabiscar(input())
        else:
            print('Não é possível escrever.')

    def ler(self):
        if self.capa:
            pagina = int(input("Qual a página?: "))
            pagina -= 1
            return pagina
        else:
            return "Não é possível ler."


print("~~~Meu livro~~~")
a = input("Autor: ")
y = int(input("Ano: "))
t = input("Tema: ")
book = Livro(a,y,t,pen)


print("Abrir o livro? (True or False)")
decisao = input()
if decisao == "False":
    book.close()
else:
    book.openn()
    escritos = []
    continua = True

    while True:
        escritos.append(book.escrever())
        print("Deseja continuar? (True or False)")
        continua = input()
        if continua == 'False':
            break

    print("Que tal fazer uma leitura? (True or False)")
    leitura = bool(input())
    if leitura == True:
        continua2 = True

        while True:
            try:
                print(escritos[book.ler()])
            except IndexError:
                print("Oops...página inválida.")

            print("Deseja continuar a leitura? (True or False)")
            continua2 = input()
            if continua2 == 'False':
                break

    print("Fechar o livro? (True or False)")
    decisao = input()
    if decisao == "True":
        book.close()
    else:
        book.openn()
