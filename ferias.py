def ferias (tempo,mes):
    temporada = ['novembro','dezembro','janeiro']
    autorizado = False

    #funcionários com mais de 3 anos podem tirar férias
    #quando quiser. Abaixo disso apenas fora de temporada

    if tempo >= 3:
        autorizado = True

    elif tempo <3 and mes.lower() not in temporada:
        autorizado = True

    return autorizado

tempo = int(input('Há quanto você trabalha nessa empresa? '))
mes = input('Qual mês você deseja tirar férias? ')

if ferias(tempo,mes):
    print("Pedido de férias aprovado")

else:
    print('Não pode tirar férias')