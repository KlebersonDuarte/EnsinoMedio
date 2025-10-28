operacional= input('Demandará grande esforço da equipe? (s/n)').lower()
financeiro = input('A perda financeira é grande caso o problema se concretize? (s/n)').lower()
mercado = input('O mercado apresente incertezas? (s/n)').lower()

if operacional == 's' and financeiro == 's' and mercado == 's':
    print('Pense 1000x antes')
elif operacional == 's' and financeiro == 's':
    print('Investir em um setor mais seguro')
elif operacional == 's' and mercado == 's':
    print('Procure coisas mais importantes')
elif mercado == 's' and financeiro == 's':
    print('Compre pizza para equipe.Você vai precisar')
elif mercado == 's':
    print('Arrisca, que vai dar bom')
elif operacional == 's':
    print('Demite todo mundo e troca por estagiários')
elif financeiro == 's':
    print('Pega com Itaú Personalitte')
else:
    print('Tá perfeito')