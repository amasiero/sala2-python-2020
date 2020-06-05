lista = ['a', 'b', 'c']
print(lista)
lista[1] = 'd'
print(lista)

tupla = (0, 1, 2)
print(tupla)

tupla = (3, 4 ,) + tupla[0:]
print(tupla)

tupla = 0, 1, 2
print(tupla)

email = 'andrey.masiero@germinare.org.br'
splitE = email.split('e')
print(splitE)

usuario, dominio = email.split('@')
print(usuario)
print(dominio)

print(zip(lista, tupla))
print(list(zip(lista, tupla)))

pessoas = ['Manzolli', 'PH',    'Lucas',    'Calvin', 'Paula', 'Henrique', 'Vinicius', 'João',     'Rafa']
frutas  = ('Morango',  'Cacau', 'Melancia', 'Banana', 'Coco',  'Manga',    'Maçã',     'Mixirica', 'Uva')

for pessoa, fruta in zip(pessoas, frutas):
	print(pessoa, 'gosta de', fruta)