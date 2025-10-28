import random 

numero = random.randint(1,100)
tentativa=0
vida=10
resto= 1
print('-🤩-JOGO DA ADIVINHAÇÃO-🤩-')
print('Você tem 10 chances de acertar o numéro ')

while tentativa <10:
    palpite=int(input('Faça um chute de 1 até 100: '))
    tentativa+=1 #pode ser tentativa=tentaiva-1
    if palpite > numero:
        print('O numéro é menor')
        print(f'Vida restante= {vida-resto}')
    elif palpite < numero:
        print('O numéro é maior')
        print(f'Vida restante= {vida-resto}')
    else:
        print(f'Você acertou em {tentativas} tentativas')
        print(f'Vida restante= {vida-resto}')

        tentativas=11
print('FIM DE JOGO')