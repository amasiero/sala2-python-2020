respostas = []

resposta = input('Telefonou para a vítima? ')
respostas.append(resposta)

resposta = input('Esteve no local do crime? ')
respostas.append(resposta)

resposta = input('Mora perto da vítima? ')
respostas.append(resposta)

resposta = input('Devia para a vítima? ')
respostas.append(resposta)

resposta = input('Já trabalhou com a vítima? ')
respostas.append(resposta)

respostas_positivas = 0

for resposta in respostas:
	if resposta == 'sim':
		respostas_positivas += 1

if respostas_positivas == 2:
	print('Suspeita')
elif respostas_positivas == 3 or respostas_positivas == 4:
	print('Cumplice')
elif respostas_positivas == 5:
	print('Assassina')
else:
	print('Inocente')