def entrada_de_numero_pelo_usuario(mensagem):
    return int(input(mensagem))


def operacao_aritmetica(n1, n2, op='+'):
    if op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        return n1 + n2


def exibe_o_resultado_para_usuario(valor):
    print(valor)


def operacao(n1, n2, funcao):
    return funcao(n1, n2)

