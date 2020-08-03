from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('Rosa', 6, 'Ford', 10)
carro_azul = Carro('Azul', 'Chevrolet', 40)
#print(caminhao_rosa)
#print(type(caminhao_rosa))
print('+=' *30)
print('Caminhão rosa')
print('Cor=>', caminhao_rosa.cor,'\nRodas=>', caminhao_rosa.cor,'\nMarca=>', caminhao_rosa.marca, '\nTanque=>', caminhao_rosa.tanque)
caminhao_rosa.abastecer(100)
print('+=' *30)
print('Carro azul')
print('Cor=>', carro_azul.cor, '\nRodas=>', carro_azul.rodas, '\nMarca=>', carro_azul.marca, '\nTanque=>', carro_azul.tanque)
carro_azul.abastecer(20)
print('Combustivel carro=>', carro_azul.tanque)
print('Combustivel caminhão', caminhao_rosa.tanque)
'''
crie um software de gerenciamento bancario
este softwate sera capaz de criar clientes e contas
cliente possui nome, cpf, idade
cada conta possui cliente e um limite negativo 
metodos sacar, depositar, consultar, saldo
'''