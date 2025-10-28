import random

semana={1:'domingo',
        2:'segunda',
        3:'terça',
        4:'quinta',
        6:'sexta',
        7:'sábado'}

treino={1:'peito',
        2:'costas',
        3:'glúteos',
        4:'perna',
        5:'posterior',
        6:'triceps',
        7:'biceps',
        8:'ombro',
        9:'trapézio',
        10:'antebraço'}

escolha = int(input('Que dia é hoje? '))
sorteio = random.randint(1,10)

print(f'Hoje é {semana[escolha]}, dia de treinar {treino[sorteio]}')