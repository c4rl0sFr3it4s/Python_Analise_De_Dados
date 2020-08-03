from veiculo import Veiculo
class Carro(Veiculo):
    '''especifica, (heranca)'''
    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque)
        '''toda vez que inicia o construtor carro ele cria um veiculo'''

    '''sobreescreve de veiculos'''
    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print('Erro de Tanque capacidade inferior.....')
        else:
            self.tanque += litros