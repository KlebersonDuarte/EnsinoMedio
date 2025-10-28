notas= []
for i in range (1,5):
    nota = float(input(f'Digite nota do {i}° bimestre '))
    notas.append(nota)

print('===BOLETIM ANUAL===')
media= sum(notas)/len(notas)
print(f'A média do aluno foi {media}')
if media >=5:
    print("Aprovado")
else:
    print('Reprovado')