from conta import Conta

class Cliente(Conta):
    def __init__(self, nome, cpf, idade, saldo):
        Conta.__init__(self, numero='', tipo='')
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.saldo = saldo

    #depositar
    def depositar(self, valor):
        self.saldo += valor


    #sacar
    def sacar(self, valor):
        self.saldo -= valor


'''
    def status(self):
        print(self.numero)
        print(self.tipo)
'''

