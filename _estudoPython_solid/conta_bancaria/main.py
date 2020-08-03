from conta import Conta
from cliente import Cliente

print('+=' *30)
print('Informações do cliente.')
conta_01 = Conta(1, 'Corrente')
cliente_01 = Cliente('Clodoaldo', '321.456.789.9', 19, 100)
print('Numero da Conta: ', conta_01.numero, '\nTipo da Conta: ', conta_01.tipo)
print('\nNome: ', cliente_01.nome,'\nCpf:', cliente_01.cpf,'\nIdade:', cliente_01.idade,'\nSaldo:', cliente_01.saldo)
cliente_01.depositar(10)
print(cliente_01.saldo)
print('+=' *30)