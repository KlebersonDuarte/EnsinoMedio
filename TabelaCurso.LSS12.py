print('😎TABELA DE CURSOS😎')
curso=int(input('Digite o numero de acordo com o curso que deseja: \n1-Tecnologia\n2-Artes\n3-Ciências'))
if curso == 1:
    nivel=int(input('Agora digite o número de acordo com a dificuldade: \n1-Iniciante:Introdução à Programação\n2-Intermediário:Desenvolvimento Web\n3-Inteligência Artificial'))
    if nivel==1:
        print('Você escolheu o curso Introdução à Programação (Iniciante)')
    elif nivel == 2:
        print('Você escolheu o curso Desenvolvimento Web (Intermediário)')
    elif nivel==3:
        print('Você escolheu o curso Inteligência Artificial (Avançado)')
    else:
        print('Opção não encontrada')
elif curso == 2:
    nivel=int(input('Agora digite o número de acordo com a dificuldade: \n1-Iniciante:Fundamentos de Desenho\n2-Intermediário:Técnicas de Pintura\n3-História da Arte Moderna'))
    if nivel==1:
        print('Você escolheu o curso Fundamentos de Desenho (Iniciante)')
    elif nivel == 2:
        print('Você escolheu o curso Técnicas de Pintura (Intermediário)')
    elif nivel ==3:
        print('Você escolheu o curso História da Arte Moderna (Avançado)')
    else:
        print('Opção não encontrada')
elif curso ==3:
    nivel=int(input('Agora digite o número de acordo com a dificuldade: \n1-Iniciante:Ciência para Todos\n2-Intermediário:Química Experimental\n3-Fisíca Teórica'))
    if nivel==1:
        print('Você escolheu o curso Ciêcia para Todos (Iniciante)')
    elif nivel == 2:
        print('Você escolheu o curso Química Experimental (Intermediário)')
    elif nivel == 3:
        print('Você escolheu o curso Fisíca Teórica (Avançado)')
    else:
     print('Opção não encontrada')
else:
    print('Opção não encontrada')  