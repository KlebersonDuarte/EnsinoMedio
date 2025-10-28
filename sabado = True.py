dia = input('Que dia é hoje?')
if dia == 'sabado' or 'domingo':
    print('Dia de descaço')
elif dia =='segunda' or 'terça' or 'quarta' or 'quinta' or 'sexta':
    print('Dia útil')
else:
    print('Dia inválido')