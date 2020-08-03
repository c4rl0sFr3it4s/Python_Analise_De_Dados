'''
muito importante para o python
permitem procurar por padrão dentro de texto.
Expressões regulares é um mini linguagem dentro
das linguagens de programações.
regular expression
search procura pela primeria incidencia
findall procurar por tudas as incidencias, quando se usa o findall
é retornado uma lista
string_de_teste = 'O gato ou a gata e os gatinhos e gatoes'
encontrado = re.search(r'(^.)+', string_de_teste)
 imprimir o texto usar o group()
if encontrado:
    print(encontrado.group())
else:
    print('Expressão não encontrada!')
'''
import re
import requests
requisicao = requests.get('https://zecoxinha.com.br/contato/')
encontrado = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text) # requiscao.text, isto é chamado de web crowling
if encontrado:
    for e in encontrado:
        print(e)
else:
    print('Não encontrado!')