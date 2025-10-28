semana ={1:'dia do trabalhador',
         7:'dia da independência',
         12:'nossa senhora parecida',
         2:'finados',
         20:'conciência',
         25:'natal',
         9:'revolução constitucional',
         2008:'aniversário da cidade'}
numero = int(input('Que feriado você quer? '))
print(semana[numero])
semana[3] = 'ano novo'
print(semana [3])
del semana [7]
print(semana)