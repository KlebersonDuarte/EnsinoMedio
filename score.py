renda = int (input('Informe a sua reda:'))
score = int(input('qual o seu score? '))
fiador = input('Você tem um fiador com score 700? (s/n)')

if renda >=2000 and (score >= 600 or fiador == 's'):
    print('Empréstimo liberado')
else:
    print('Tende outro banco')