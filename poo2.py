class Usuario:
    def __init__ (self,nome,senha):
        self.nome = nome #self fica com atributo,sem self é parametro
        self.senha = senha

    def get_senha (self):
        return self.senha
    
    def set_senha (self,nova_senha):
        self.senha = nova_senha 
        return 'senha altera com sucesso'
    
user1 = Usuario('João Dirty','senha125')
print(user1.get_senha())
print(user1.set_senha('novasenha521'))
print(user1.get_senha())