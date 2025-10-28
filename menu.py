equipes = []
def cadastrar():
    print('---CASDATRO DE EQUIPE---')
    devs=int(input('Quantos desenvolvedores'))
    designers=int(input('Quantos designers'))
    gerentes=int(input('Quantos gerentes'))
    orcamento=int(input('Qual orçamento'))

    equipe ={
        'Desenvolvedores': devs,
        'Designers': designers,
        'Gerentes de projeto': gerentes,
        'Orçamento': orcamento
    }

    equipes.append(equipe)
    print('Equipe cadastrada com sucesso!')

def consultar():
    print('---CONSULTA DE EQUIPE---')
    if len(equipes)==0:
        print('Nenhuma equipe cadastrada')
    else:
        for n,equipe in enumerate(equipes,start=1):#o enumerete permite rodar um vetor, e o satrt é onde começa,por padrão ele começa no 0, caso você quiera que comece no 0 nem precisa colocar o start
            print(f'Equipe {n}:')
            print(f'Desenvolvedores:{equipe['Desenvolvedores']}')
            print(f'Designers:{equipe['Designers']}')
            print(f'Gerentes de projeto:{equipe['Gerentes de projeto']}')
            print(f'Orçamneto:{equipe['Orçamento']}\n')

escolha =''
while escolha != '3':
    print('---MENU PRINCIPAL---')
    print('1. Cadastrar equipe')
    print('2. Consultar equipes')
    print('3. Sair do programa')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        cadastrar()
    elif escolha == '2':
        consultar()
    else:
        print('Programa encerrado')