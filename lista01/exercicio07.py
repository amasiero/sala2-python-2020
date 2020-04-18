valor_hora = float(input('Qual o seu valor hora? '))
horas_trabalhadas = int(input('Quantas horas você trabalhou neste mês? '))

salario = valor_hora * horas_trabalhadas
salario_arredondado = round(salario, 2)

print(f'O seu salário é de R$ {salario_arredondado}')