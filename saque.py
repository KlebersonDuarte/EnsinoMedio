saque=int(input('Que valor deseja sacar? '))
nota50=saque // 50
print(f'{nota50} notas de R$50')
saque = saque % 50

nota20=saque // 20
print(f'{nota20} notas de R$20')
saque = saque % 20

nota10=saque // 10
print(f'{nota10} notas de R$10')
saque = saque % 10

nota5=saque // 5
print(f'{nota5} notas de R$5')
saque = saque % 5

nota2=saque // 2
print(f'{nota2} notas de R$2')
saque = saque % 2

print(f'{saque} moedas de R$1')
