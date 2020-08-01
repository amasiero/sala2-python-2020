import numpy as np

dados = []

with open('owid-covid-data.csv', 'r') as arquivo:
    for linha in arquivo:
        registro = linha.strip().split(',')
        if registro[0] == 'BRA':
            dados.append(float(registro[5]))

media = np.mean(dados)
print(f'{media:.0f}')

mediana = np.median(dados)
print(f'{mediana:.0f}')

desvio_padrao = np.std(dados)
print(f'{desvio_padrao:.0f}')

cv = desvio_padrao / media
print(f'{cv:.5f}')


def calcula_media_movel(dados, janela=7):
    pesos = np.ones(janela)
    media_movel = np.convolve(dados, pesos, 'valid') / janela
    return media_movel


media_movel_resultado = calcula_media_movel(dados)
print(media_movel_resultado)
