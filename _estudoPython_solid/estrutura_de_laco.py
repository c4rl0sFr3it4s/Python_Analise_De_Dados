'''
estrutura de laço
As listas são essenciais para intender a estrutura de laço
com esta estrutura e que vamos percorrer estas listas, cada uma de uma vez
while
for
'''
lista_nomes = ['Carlos', 'Marcelo', 'João', 'Julia']
#cont = range(0, 20, 2)
'''
range(comecar, ate, step)
'''
print('Comecei a processar!')
for nomes in lista_nomes:
    print(nomes)
for itens in range(0, 10, 2):
    print(itens)
for itens in range(len(lista_nomes)):
    print(lista_nomes[itens])

lista_nomes.append('OI')
print(lista_nomes)
print('Acabei de processar...')
#while, sempre true
i = 0
print('Entrei no while ;)')
while i < 10:
    print('i é menor que 10', i)
    if i == 8:
        print('Cheguei à', i, 'preciso sair....')
        break
    i += 1
print('Sai do while ;(')
qtd_pessoas = []
qtd = int(input('Entre com a quantidade de pessoas para a festa: '))
i = 0
while i < qtd:
    print(i, 'º Pessoa\n')
    nome = input('Nome:')
    qtd_pessoas.append(nome)
    i += 1
print('Pessoas relacionadas: ', qtd_pessoas)

'''
para cada nome dentro de lista_nomes
    mostre nomes
1 verifica cada nomes dentro de lista_nomes
  me mostra 1 nome.
1 em cada linha 
python não existe i++
'''