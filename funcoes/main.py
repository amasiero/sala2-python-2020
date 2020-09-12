import funcoes as f

# PROGRAMA 1
a = f.entrada_de_numero_pelo_usuario("Digite um número: ")
b = f.entrada_de_numero_pelo_usuario("Digite outro número: ")

resultado = f.operacao_aritmetica(n2=a, n1=b, op='-')
f.exibe_o_resultado_para_usuario(resultado)

# PROGRAMA 2
c = f.entrada_de_numero_pelo_usuario("Digite um número: ")
d = f.entrada_de_numero_pelo_usuario("Digite outro número: ")

resultado = f.operacao_aritmetica(c, d)
f.exibe_o_resultado_para_usuario(resultado)


def soma(x, y):
    return x + y


e = 2
h = 4
print(f.operacao(e, h, lambda x, y: x + y))
print(f.operacao(e, h, lambda x, y: x - y))
print(f.operacao(e, h, lambda x, y: x * y))
print(f.operacao(e, h, lambda x, y: x / y))
