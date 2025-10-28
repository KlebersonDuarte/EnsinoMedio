candidato=int(input('Digite seu voto: '))
match candidato:
    case 13:
        print('Nome do candidato: Lula ')
        print('nome do vice: Gustavo Lima')
        print('Partido:PT')
    case 22:
        print('Nome do candidato: Bolsonaro ')
        print('nome do vice: Felipe neto')
        print('Partido:Br')
    case 69:
        print('Nome do candidato: Alanzoka ')
        print('nome do vice: Caneta Azul')
        print('Partido:AG')
    case 00:
        print('Voto Branco')
    case _:
        print('Voto Nulo')