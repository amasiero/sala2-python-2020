# tabela de preco
print(f'\t\tAté 5 kg\t\tAcima de 5 kg')
print(u"\u2022", f'Morango\tR$ 2,50 por kg\t\tR$ 2,20 por kg')
print(u"\u2022", f'Maça\t\tR$ 1,80 por kg\t\tR$ 1,50 por kg\n')
# receber quantidade de morangos
quilos_morangos = float(input('Digite a quantidade de morango (kg):'))
# receber quantidade de maças
quilos_maca = float(input('Digite a quantidade de maças (kg):'))
# calcular total de peso
total_quilos = quilos_morangos + quilos_maca
# calcular valor para macas
if quilos_maca > 5:
	valor_maca = quilos_maca * 1.5
else:
	valor_maca = quilos_maca * 1.8
# calcular valor para morangos
if quilos_morangos > 5:
	valor_morangos = quilos_morangos * 2.2
else:
	valor_morangos = quilos_morangos * 2.5
# calcular valor
valor_total = valor_morangos + valor_maca
# calcular o desconto
desconto = 0
if valor_total > 25 or total_quilos > 8:
	desconto = valor_total * 0.1
# calcular o pagamento
pagamento = valor_total - desconto
# exibir o resultado
print(f'\nTotal de frutas {total_quilos:.2f} kg')
print(f'Valor sem desconto R$ {valor_total:.2f}')
print(f'Valor do desconto R$ {desconto:.2f}')
print(f'Valor a pagar R$ {pagamento:.2f}')
