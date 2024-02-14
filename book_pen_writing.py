class Caneta:
    def __init__(self,modelo,cor,ponta):
        self.modelo = modelo
        self.cor = cor
        self.ponta = ponta

    def rabiscar(self,tampa):
        if tampa == 'True':
            print("Caneta tampada.")
        else:
            acao = int(input("Escrever(1) ou Pintar(2)?: "))
            if acao == 1:
                rabisco = input("Escreva: ")
                print(f"Escreveu '{rabisco}' com a cor",self.cor)
            elif acao == 2:
                print("Pintou com a cor",self.cor)
                
print("~~~Minha caneta~~~")
m = input("Modelo: ")
c = input("Cor: ")
p = float(input("Ponta: "))
pen = Caneta(m,c,p)

# Se a caneta estiver tampada, como fazer se a pessoa quer escrever no livro?
class Livro:
    def __init__(self,autor,ano,tema,caneta):
        self.autor = autor
        self.ano = ano
        self.tema = tema
        self.caneta = caneta

    def ler(self,capa):
        if capa == 'fechado':
            print('Não é possível ler.')
        elif capa == 'aberto':
            pagina = int(input("Qual a página?: "))
            print(f"Livro aberto na página {pagina}")
    def escrever(self,folha):
        if folha == 'escrita':
            print("Não pode escrever aí!")
        elif folha == 'em branco':
            print("A caneta está com tampa?(True or False)")
            self.caneta.rabiscar(input())

print("~~~Meu livro~~~")
a = input("Autor: ")
y = int(input("Ano: "))
t = input("Tema: ")
book = Livro(a,y,t,pen)
print("O livro está aberto ou fechado?")
leitura = input().lower()
book.ler(leitura)
if leitura == 'aberto':
    print("A folha está...(escrita ou em branco?)")
    book.escrever(input().lower())
