notas = []

while True:
	nota = float(input('Digite uma nota: '))
	if nota >= 0:
		notas.append(nota)
	else:
		break

print('Foram registrados', len(notas), 'notas')

print('-----------------------------------')
for nota in notas:
	print(nota, end='\t')

print('\n-----------------------------------')
for nota in notas[::-1]:
	print(nota)

print('-----------------------------------')
soma = 0
for nota in notas:
	soma += nota
print('A soma total das notas eh', soma, 'pontos')

print('-----------------------------------')
media = soma / len(notas)
print('A media eh', media, 'pontos')

print('-----------------------------------')
valores_acima = []
qtde_acima = 0
for nota in notas:
	if(nota > media):
		qtde_acima += 1
		valores_acima.append(nota)

print(f'Foram encontrados {qtde_acima} notas acima da média.')
print(f'Confira a lista de valores: {valores_acima}')

print('-----------------------------------')
valores_abaixo_sete = []
qtde_abaixo_sete = 0
for nota in notas:
	if(nota < 7):
		qtde_abaixo_sete += 1
		valores_abaixo_sete.append(nota)

print(f'Foram encontrados {qtde_abaixo_sete} notas abaixo de sete.')
print(f'Confira a lista de valores: {valores_abaixo_sete}')

print('-----------------------------------')
print('Fim do Programa')