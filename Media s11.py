media = int (input('Qual é usa média?')) 
exame = input('Passou no exame (s/n)?')
if media > 7:
    print('Passou de ano')
elif media >5 and exame == 's':
    print('Passou de ano')
else:
    print('Reprovado')