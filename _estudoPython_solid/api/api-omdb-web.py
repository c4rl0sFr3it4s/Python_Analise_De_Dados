'''api-request-web-json
um programinha que vai retornar os nomes dos
filmes, passar o nome do filme ele vai retornar
para o sistema o nome do filme, ano, nota.
API -aplication programing interfaces.
Interfaces que se comunica com outros programas vamos passar
para ele parametros, e está API vai te retornar com informações
Podemos encontrar milhares de API na web.
e conversar com outros programas através de parametros.
Para iste programa vamos utilizar o OMDB open moden data base
que é uma API sobre filmes, posemos requisitar por esta API e
obter resposta sobre filmes.
'''
import requests
import json

def requisitar(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=dd2ebb34&t='+ titulo+ '&type=movie')
        dict = json.loads(req.text)
        return imprimir(dict)
    except Exception as err:
        print('Erro', err)
        return None

def imprimir(dict):
    print('=+' *50)
    print('Titulo: ', dict['Title'])
    print('Ano: ', dict['Year'])
    print('Diretor: ', dict['Director'])
    print('Atores: ', dict['Actors'])
    print('Notas do público: ', dict['imdbRating'])
    print('Premios: ', dict['Awards'])
    print('Poster', dict['Poster'])
    print('=+' * 50)


rodar = True
while rodar:
    print('Digite...')
    op = input('para pesquisar um filme |FILME|\nou |SAIR| para encerrar o programa.')
    if op == 'SAIR':
        print('Saindo ...')
        sair = False
        exit()
    elif op == 'FILME':
        titulo = input('Entre com o titulo do filme.')
        requisitar(titulo)

