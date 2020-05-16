print('Lojas Tabajara')
print('pressione Ctrl + C para finalizar o programa')
while True:
	produtos = []
	print('\nPróximo Cliente\n')
	while True:
		valor_produto = float(input('Digite o valor do produto: R$ '))
		if valor_produto == 0:
			break
		produtos.append(valor_produto)

	total_compra = 0
	print('\nListagem dos Produtos')
	for produto, numero in zip(produtos, range(len(produtos))):
		print(f'Produto {numero + 1}: R$ {produto:.2f}')
		total_compra += produto

	print(f'\nTotal: R$ {total_compra:.2f}')
	dinheiro = float(input('\nInforme o valor recebido: R$ '))
	print(f'Dinheiro: R$ {dinheiro:.2f}')
	print(f'Troco: R$ {(dinheiro - total_compra):.2f}')