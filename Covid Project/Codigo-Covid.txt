import numpy as np


def calcula_media_movel(dados, janela=7):
    pesos = np.ones(janela)
    media_movel = np.convolve(dados, pesos, 'valid') / janela
    return media_movel


dados = []
dias = []
with open('owid-covid-data.csv', 'r') as arquivo:
    for linha in arquivo:
        registro = linha.strip().split(',')
        if registro[0] == 'BRA':
            dias.append(registro[3])
            dados.append(float(registro[5]))

media = np.mean(dados)
mediana = np.median(dados)
desvio_padrao = np.std(dados)
cv = desvio_padrao / media
media_movel_resultado = calcula_media_movel(dados)


with open('relatorio.txt', 'w') as arquivo:
    indice = 1
    for dia, casos, media_movel in zip(dias, dados, media_movel_resultado):
        arquivo.write('-' * 40 + '\n')
        arquivo.write(f'Data: {dia}\n')
        arquivo.write(f'Ocorreram {casos:.0f} casos novos.\n')
        arquivo.write(f'Total acumulado de {np.sum(dados[:indice]):.0f} casos.\n')
        arquivo.write(f'Media movel: {media_movel:.0f} casos.\n')
        indice += 1
    arquivo.write('-' * 40 + '\n')
    arquivo.write(f'Media Geral: {media:.0f}\n')
    arquivo.write(f'Mediana: {mediana:.0f}\n')
    arquivo.write(f'Desvio Padrao: {desvio_padrao:.0f}\n')
    arquivo.write(f'Coeficiente de Variacao: {cv:.5f}\n')
    arquivo.write('-' * 40 + '\n')
