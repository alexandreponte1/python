class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite


#metodos estaticos que são da classe
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}


# Atributo o que um objeto tem.
# Metodo o que uma objeto faz, o comportamento.


# Nesta aula, aprendemos:

#     Métodos de leitura dos atributos, os getters
#     Métodos de modifição dos atributos, os setters
#     Propriedades



# >>> from conta import Conta
# >>> conta = Conta(123, "Nico", 55.5, 1000.0)
# Construindo objeto ... <conta.Conta object at 0x7faf2aad4438>
# >>> conta.saca(10000)
# O valor 10000 passou o limite


# >>> from conta import Conta
# >>> Conta.codigo_banco()
# '001'
# >>> Conta.codigos_bancos()
# {'Caixa': '104', 'BB': '001', 'Bradesco': '237'}