with open('owid-covid-data.csv', 'r') as arquivo:
    for linha in arquivo:
        colunas = linha.split(',')
        if colunas[0] == 'BRA':
            print(colunas)