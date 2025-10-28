class Eletronicos:
    def __init__ (self,nome,marca,preco):
        self.nome = nome
        self.marca = marca
        self.preco = preco
    def informacoes(self):
        print(f'Nome:{self.nome}, Marca:{self.marca}, Preço:R${self.preco}')
class Celular(Eletronicos):
    def __init__(self,nome,marca,preco,armazenamento):
        super().__init__(nome,marca,preco)
        self.armazenamento = armazenamento
    def informacoes(self):
        super().informacoes()
        print(f'Capacidade de armazenamento:{self.armazenamento}GBqqqq')
class Notebook(Eletronicos):
    def __init__(self,nome,marca,preco,memoria):
        super().__init__(nome,marca,preco)
        self.memoria = memoria
    def informacoes(self):
        super().informacoes()
        print(f'Capacidade de memória Ram:{self.memoria}GB')

aparelho1 = Celular('Iphone','Apple',10000,'512')
aparelho1.informacoes()
aparelho2 = Celular('Galaxy S24','Samsung',3000,'256')
aparelho2.informacoes()
aparelho3 = Notebook('Chromebook','Google',1700,'4')
aparelho3.informacoes()