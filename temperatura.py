hr=input('Está de dia? (s/n)')
if hr == 's':
    temperatura=int(input('Qual é a temperatura? '))
    if temperatura > 25:
        print('Ar-condicionado ligado')
    elif temperatura < 15:
        print('Aquecedor ligado')
    else:
        print('Nada acontece')
else:
    print('Nada acontece')