horas = int(input("quantidade de horas na semana:\n"))
dias = int(input("dias trabalhados na semana:\n"))
valor = int(input("valor que recebe por hora:\n"))
salario = horas * dias * valor * 4.5 * 0.93
print(f"seu salário é de R$ {salario:.2f} ")