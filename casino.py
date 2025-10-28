import random
animais = ['🐔','🐮','🐷','🦊','🐴','🦁','🦭']
saldo = 50
print('=====🎰 BEM VINDO AO JOGO DO BIXO 🎰=====')
print('-'*40)

while saldo>0:
    print(f'Saldo atual: ${saldo}')
    aposta = float(input('O quanto quer apostar? (Digite 0 para sair) '))
    if aposta == 0:
        print(f'Tchau! Você saiu do jogo com ${saldo}')
        break
    saldo = saldo - aposta
    sorteio = [random.choice(animais) for _ in range (3)]
    print('Resultado:',' / '.join(sorteio))
    if sorteio[0]==sorteio[1]==sorteio[2]:
        print(f'3 animais iguais! Você ganhou {aposta*5}')
        saldo = saldo + aposta*5
    elif sorteio[0]==sorteio[1] or sorteio[1]==sorteio[2]:
        print(f'2 animais iguais! Você ganhou {aposta*2}')
        saldo = saldo + aposta*2
    else:
        print('Não ganho nada kkkkkk😄')
print('-'*40)
if saldo <=0:
    print('Seu dinheiro acabou')