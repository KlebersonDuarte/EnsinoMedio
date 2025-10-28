quantidade=int(input('Quantos itens você comprou? '))
item=input('Ele entra em qual categoria? (tecnologia/vestuário)')

if item == 'tecnologia':
    if quantidade >2:
        print('Desconto de 10%')
    else:
        print('Sem desconto')
elif item == 'vestuário':
    if quantidade >3:
        print('Desconto de 20%')
    else:
        print('Sem desconto')
else:
    print('Produto não listado,tente de novo')
