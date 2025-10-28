msg= input('Você está conectado? (s/n) ')
amigo=input('O destinatário é seu amigo? (s/n) ')
if msg and amigo == 's':
    print("Mensagem enviada")
else:
    print('Mensagem não enviada')