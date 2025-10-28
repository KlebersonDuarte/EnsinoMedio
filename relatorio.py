vendas = [('Produto A',10),('Produto B',20),('Produto C',15),('Produto D',25)]
total = {}
contagem = {}
#Processamento de dados
for produto,venda in vendas:
    if produto in total:
        total[produto] += venda
        contagem[produto] += 1
    else:
        total[produto] = venda
        contagem[produto] = 1

print('Relatório de vendas:')
for produto in total:
    media = total[produto]/contagem[produto]
    print(f'{produto}: Total vendido = {total[produto]}, Média diária = {media:.2f}')