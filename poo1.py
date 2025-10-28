class Lampada:
    def __init__(self):
        self.estado=False #lampada apagada
    def interruptor(self):
        self.estado = not self.estado
        return 'Ligada' if self.estado else 'Desligada'
    
lampada_sala= Lampada() #cria o objeto de classe lampada
lampada_banheiro= Lampada() 
lampada_quarto= Lampada() 
print(lampada_sala.estado) #chama atributo sem parenteses
print(lampada_banheiro.interruptor()) #chama método com parenteses
print(lampada_banheiro.interruptor())