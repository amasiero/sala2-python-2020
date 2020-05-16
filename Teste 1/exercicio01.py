#receber o valor hora 
valor_hora = float(input('Digite seu valor hora: R$ '))
#receber quantidade de horas trabalhadas
horas_trabalhadas = int(input('Digite a quantidadede horas trabalhadas: '))
#calcular o salario bruto
salario_bruto = valor_hora * horas_trabalhadas
#calular IR
## até 900 - isento
ir = 0
percentual = 0
## até 1500 - 5%
if salario_bruto > 900 and salario_bruto <= 1500:
	ir = salario_bruto * 0.05
	percentual = 5
	## até 2500 - 10%
elif salario_bruto > 1500 and salario_bruto <= 2500:
	ir = salario_bruto * 0.1
	percentual = 10
	## acima 2500 - 20%
elif salario_bruto > 2500:
	ir = salario_bruto * 0.2
	percentual = 20
#calcular sindicato 3%
sindicato = salario_bruto * 0.03
#calcular inss 10%
inss = salario_bruto * 0.1
#calular FGTS 11% (sem descontar)
fgts = salario_bruto * 0.11
#salario liquido
descontos = (ir + sindicato + inss)
salario_liquido = salario_bruto - descontos
#exibir o demonstrativo de pagamento
print(f'\033[95mSalário Bruto\033[0m: ({valor_hora:.2f} * {horas_trabalhadas})\t: R$ {salario_bruto:.2f}')
print(f' \033[91m(-)\033[0m IR ({percentual}%)\t\t\t: R$ {ir:.2f}')
print(f' \033[91m(-)\033[0m INSS (10%)\t\t\t: R$ {inss:.2f}')
print(f' \033[91m(-)\033[0m Sindicato (3%)\t\t: R$ {sindicato:.2f}')
print(f'\033[92mFGTS\033[0m (11%)\t\t\t: R$ {fgts:.2f}')
print(f'Total de descontos\t\t: R$ {descontos:.2f}')
print(f'\033[92mSalário Líquido\033[0m\t\t\t: R$ {salario_liquido:.2f}')

#MAGENTA = '\033[95m'
#CYAN = '\033[96m'
#BLUE = '\033[94m'
#DARKCYAN = '\033[36m'
#GREEN = '\033[92m'
#YELLOW = '\033[93m'
#RED = '\033[91m'
#BOLD = '\033[1m'
#UNDERLINE = '\033[4m'
#END = '\033[0m'
#https://raccoon.ninja/pt/dev-pt/tabela-de-cores-ansi-python/