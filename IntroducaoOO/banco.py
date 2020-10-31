# -*- coding: UTF-8 -*-
class Conta:
    def __init__(self, cliente='', saldo=0.0, limite=100):
        self.__cliente = cliente
        self.__saldo = saldo
        self.__limite = limite

    def get_cliente(self):
        return self.__cliente

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def get_saldo(self):
        return self.__saldo

    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        if (self.__saldo + self.__limite) >= valor:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente')


if __name__ == '__main__':
    conta = Conta('Thayná', 15000.0)
    print(conta.get_cliente())
    print(conta.get_saldo())

    conta.deposito(500)
    print(conta.get_saldo())

    conta.saque(15000)
    print(conta.get_saldo())

    conta.saque(600)
    print(conta.get_saldo())

    conta.saque(100)
    conta.saldo = 15000.0
    print(conta.saldo)
    print(conta.get_saldo())

    conta.set_cliente('Jesus')
    print(conta.get_cliente())
