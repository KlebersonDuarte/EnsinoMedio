numero=int(input('Digite um numéro: '))
if numero > 0:
    if numero % 2== 0:
        print('Positivo e par')
    else:
        print('Positivo e  ímpar')
elif numero <0:
    if numero % 2 == 0:
         print('Negativo e par')
    else:
        print('Negativo e  ímpar')
else:
    print('Zero')
