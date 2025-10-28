sigla=input('Digite a sigla de um elemento: ')
sigla=sigla.upper()
match sigla:
    case 'FE':
        print('Elemento:Ferro')
        print('Massa:55')
        print('Número atómico:26')
    case 'AG':
        print('Elemento:Prata')
        print('Massa:107')
        print('Número atómico:47')
    case 'MG':
        print('Elemento:Magnézio')
        print('Massa:24')
        print('Número atómico:12')
    case _:
        print('Elemento não encontrado')