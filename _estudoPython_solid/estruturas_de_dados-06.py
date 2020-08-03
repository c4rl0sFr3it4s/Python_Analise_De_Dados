'''
ESTRUTURAS DE DADOS
dicionarios - dict
tuplas - tuple
conjuntos - set
'''
minha_tupla = ('Carlos', 'João')
meu_dicionario = {'nome': 'Carlos', 'idade': 27}
meu_conjunto = {'Carlos', 'João'}
#iniciando estruturas de dados vazias
list = []
tupla = ()
dicionario = {}
conjunto = set() # iniciando conjunto
meu_conjunto.add('Maria')
meu_conjunto.add('Maria') #não vai ser adicionado porque o set não aceita repetidos
meu_conjunto.remove('Maria')
print(meu_conjunto)
#print(meu_conjunto[0]), dá pau porque o objeto set, não tem indice
if 'Maria' in meu_conjunto:
    print('Foi encontrado dentro do conjunto')
'''
Conjunto
É para busca rápida, não aceita repetido
Sempre utilizado em estrutura de decisão
Quando você pergunta assim se Maria está dentro do conjunto
o python percorre a lista inteira atrás da Maria, se a maria for o ultimo
ele vai percorrer a lista inteira atrás da Maria, fazendo milhões de comparações
lá dentro.
Já o conjunto é uma tabela hash, cada palavra lá dentro é transformado em um 
código e a busca dentro dela na memória é mais rápida.
A lista ela é ordenado 
Se o programa está lento ou estranho você pode estar usando alguma 
estrutura erronea
'''
'''
#dicionario
#sempre que refernciar a chave vem dentro do []
print(meu_dicionario['nome'])
#modificando pela chave o valor
meu_dicionario['nome'] = 'João'
#adicionando nova chave e valor
meu_dicionario['endereco'] = 'Av. Pedro Garcia Fernandes'
meu_dicionario['telefone'] = '(11) - 932732754'
print(len(meu_dicionario))

#verifica se o valor esta dentro do dict
if 'Carlos' in meu_dicionario.values():
    print('Carlos está no dicionário')
#printa somente os valores dentro do dict
for valores in meu_dicionario.values():
    print(valores)
#verificando as chaves
for keys in meu_dicionario.keys():
    print(keys)
#pegando o chave

Dicionário 
clear - limpar
update - atualizar
meu_dicionario.keys()
meu_dicionario.values(), procura se o valor esta lá dentro
clear() - limpa
pop() - retira 
update() - modifica o valor lá dentro
Muito utilizado em organizar dados, estruturar dados
utilizar em banco de dados, em busca ele é muito mais eficiente que tuplas 
e listas.
'''
'''
saida tupla
print(minha_tupla)
print(type(minha_tupla))
print(minha_tupla[0])
print(minha_tupla[1])

A tupla quando for modificada ela somente 
será modificada toda

minha_tupla = ('Vinicios', 'Alvaro')
print(minha_tupla)
for nome in minha_tupla:
    print(nome)
#pode fazer isto para qualquer uma das estruturas.
if 'Vinicios' in minha_tupla:
    print('Vinicios está na coleção')
'''
'''
Tuplas - tuple
Não é mutavel não tem append, remove, extend
So consigo pegar o valor, modificar, não consegue mudar
o tamanho, utilizar quando se precisa ter um valor limitado.
É utilizado em objeto mais estatico.
Dicionário - dict
Funciona mesma coisa como um dicionário comum que vemos
ele possui chave e valor.
O valor pode ser qualquer coisa, a chave ele pode ser hash, o dicionário me
descreve ele é parecido como objeto json, o hashMap do java, ou dict
Conjunto - set
Também é pareciodo como um dicionário, porém não tem a chave
não contém repetidos, é por isto chama conjunto como se fosse um
conjunto matemático, ele é dinâmico, pode adicionar, e pegar, remover.
Não é ordenado não tem indice.
'''