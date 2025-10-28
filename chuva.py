chuva=input('Está chovendo? (s/n) ')
gb=input('Você tem guarda  chuva? (s/n) ')
if chuva == 'n':
    print('Tá de boa')
elif chuva == 's':
    if gb == 's':
        print('Quase que você fica molhadinho')
    else:
        print('Vai ficar molhadinho')
else:
    print('Resposta inválida (responda apenas com "s" ou  "n")')