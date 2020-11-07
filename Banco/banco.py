from models import Conta, ContaPF
import sys

if __name__ == '__main__':
    try:
        conta = Conta('Andrey')
        conta.deposita(1400)

        conta.transfere(1000, 20)

        print(conta)
        conta.cliente = 'Giroto'
        print(conta)

        conta_pf = ContaPF('Cayo', '123456789-00')
        conta_pf.deposita(15000)
        print(conta_pf)

        conta.transfere(400, conta_pf)
        print(conta)
        print(conta_pf)
        conta.deposita(-100)

    except AttributeError as error:
        print(error)
    except TypeError as error:
        error_type, error_instance, traceback = sys.exc_info()
        print(error_type, error_instance, traceback)
    except:
        print('Deu ruim')
