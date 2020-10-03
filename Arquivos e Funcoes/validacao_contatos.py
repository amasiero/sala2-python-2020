# encoding: utf-8
import re


def nome_valido(nome):
    return len(re.findall(r'^[a-zA-z]*\ [a-zA-z]*$', nome)) > 0


def email_valido(email):
    return len(re.findall(r'^[a-z0-9.]+@[a-z0-9]+\.[a-z]*', email)) > 0


def celular_valido(celular):
    localidade = ''
    if (len(re.findall(r'^\(\d{2}\) \d{4,5}-\d{4}$', celular)) > 0):
        localidade = 'Brasil'
    elif (len(re.findall(r'^\(\d{3}\)-\d{4,5}-\d{4}$', celular)) > 0):
        localidade = 'Estados Unidos'
    elif (len(re.findall(r'^\d{4}-\d{7}$', celular)) > 0):
        localidade = 'Alemanha'
    elif (len(re.findall(r'^\d{4}-\d{3}-\d{3,4}$', celular)) > 0):
        localidade = 'Reino Unido'
    return localidade


def telefone_valido(telefone):
    localidade = ''
    if (len(re.findall(r'^\(\d{2}\) \d{4,5}-\d{4}$', telefone)) > 0):
        localidade = 'Brasil'
    elif (len(re.findall(r'^\(\d{3}\)-\d{4,5}-\d{4}$', telefone)) > 0):
        localidade = 'Estados Unidos'
    elif (len(re.findall(r'^\d{4}-\d{7}$', telefone)) > 0):
        localidade = 'Alemanha'
    elif (len(re.findall(r'^\d{6}\ \d{5}$', telefone)) > 0):
        localidade = 'Reino Unido'
    return localidade


def ler_base_dados(base_dados):
    with open(base_dados, 'r') as arquivo:
        with open('relatorio.txt', 'w') as destino:
            arquivo.readline()
            for linha in arquivo:
                contato = linha.split(',')
                nome = nome_valido(contato[0])
                email = email_valido(contato[1])
                celular = celular_valido(contato[2])
                telefone = telefone_valido(contato[3])
                registro = {
                    "nome": "valido" if nome else "invalido",
                    "email": "valido" if email else "invalido",
                    "celular": "valido" if celular != '' else "invalido",
                    "telefone": "valido" if telefone != '' else "invalido",
                    "localidade": celular or telefone
                }
                destino.write(str(registro) + '\n')


ler_base_dados('database.csv')
