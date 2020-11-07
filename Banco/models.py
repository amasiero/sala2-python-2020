class Conta:
    def __init__(self, cliente):
        self.__cliente = cliente
        self.__saldo = 0.0

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def saldo(self):
        return self.__saldo

    def deposita(self, valor):  # Função Early Return
        if self.__valor_negativo(valor):
            raise AttributeError('O valor deve ser positivo.')

        self.__saldo += valor

    def saca(self, valor):
        if self.__valor_negativo(valor):
            raise AttributeError('O valor deve ser positivo.')

        if not self.__saldo_disponivel(valor):
            raise AttributeError('Saldo insuficiente')

        self.__saldo -= valor

    def transfere(self, valor, conta):
        if not self.__valida_tipo_conta(conta):
            raise TypeError('O objeto informado não é uma conta.')
        self.saca(valor)
        conta.deposita(valor)

    def __valida_tipo_conta(self, conta):
        return (
            type(conta) is Conta or
            issubclass(conta.__class__, Conta)
        )

    def __valor_negativo(self, valor):
        return valor < 0

    def __saldo_disponivel(self, valor):
        return self.__saldo >= valor

    def __str__(self):
        return f'O cliente {self.__cliente} tem o saldo de R$ {self.__saldo:.2f}.'


class ContaPF(Conta):
    def __init__(self, cliente, cpf):
        super().__init__(cliente)
        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    def __valida_cpf(self, cpf):
        # TODO utilizar expressão regular para validação do CPF
        pass
