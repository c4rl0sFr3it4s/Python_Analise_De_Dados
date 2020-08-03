'''
big query uma biblioteca para dados do google driver
recurso é objeto dos dados em uma coleção
coleção é um conjunto de dados de recursos
.load(), para arquivo, de somente reandable, leitura, no formato coleção
.loads(), como o nome já diz é para Strings
'''
import requests
import json

'''pesquisa por titulo e paginação'''
def pesquisar(titulo, pagina):
    try:
        resposta = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=dd2ebb34&s='+ titulo+ '&page=', pagina)
        # json.loads() transformou a string JSON em um objeto Python
        dados = json.loads(resposta.content)
        # print(dados['Search'])
        for d in dados['Search']:
            imprimir(d)
    except Exception as err:
        print('Erro....', err)

'''imprime o dicionari'''
def imprimir(d):
    print('+=' *30)
    print('RESULTADO DA PESQUISA')
    print('+=' * 30)
    print('Tipo =>', d['Type'])
    print('Titulo => ', d['Title'])
    print('Ano =>', d['Year'])
    # print('+=' * 30)

while True:
    print('Sistema de pesquisa de FILME.\n')
    op = input('Digite "F" para filme ou "S" para sair.').upper()[0]
    if op in 'FS':
        if op == 'F':
            titulo = input('Entre com o titulo: ')
            pagina = int(input('Número de páginas'))
            pesquisar(titulo, pagina)
        elif op == 'S':
            print('Saindo....')
            exit()
print('Fim da operação!')