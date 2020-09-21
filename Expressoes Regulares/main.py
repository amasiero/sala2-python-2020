import re

email = input('Informe seu email: ')
padrao = r'[a-z0-9.]+@[a-z0-9]+\.[a-z]*'

resultado = re.findall(padrao, email)

if resultado is not None and len(resultado) > 0:
    print(resultado)
else:
    print('\033[91mPadrao não validado\033[0m')


telefone = input('Informe seu telefone: ')
padrao = r'\(\d{2}\) \d{4,5}-\d{4}|\d{4,5}-\d{4}|\d{2} \d{4,5}-\d{4}'

resultado = re.findall(padrao, telefone)

if resultado is not None and len(resultado) > 0:
    print(re.sub('[()-]|\s', '', telefone))
else:
    print('\033[91mPadrao não validado\033[0m')

cpf = input('Digite seu cpf: ')
padrao = r'\d{3}\.\d{3}\.\d{3}-\d{2}|^\d{11}$|\d{3}\s\d{3}\s\d{3}-\d{2}|\d{3}\.\d{3}\.\d{3}\/\d{2}'

resultado = re.findall(padrao, cpf)
print(resultado)

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