import re
'''
from timeit import timeit
setup = """import re """
time = timeit("""re.match(r'\d{4}', '1234')""", setup)
print(time)
'''
'''match restringe a busca pela string no inicio(padrão, string)'''
result = re.match(r'Av', 'Av Paulista 1680')
print('match =>', result.group(0))
print('inicio match', result.start())
print('fim match', result.end())
'''search nao restringe a busca'''
result_search = re.search(r'Paulista', 'Av Paulista 1680')
print('search =>', result_search.group(0))

'''findall busca padroes e retorna em uma lista
quando printado somente como variável ele mostra uma lista
printado com o indice ele retorna uma string'''
result_findall = re.findall(r'Av', 'Av Paulista 1680')
print('findall =>', result_findall)
'''split ajuda a dividir a string pela ocorrência do padrão dado'''
result_split = re.split(r'i', 'Av Paulista 1680')
print('split =>', result_split)
'''split tem uma função maxsplit que delimita o numero de divisão'''
result_split_maxsplit = re.split(r'i', 'Av Paulista 1680 perto da igreja', maxsplit=1)
print('maxsplit => ', result_split_maxsplit)
'''sub o padrao não for encontrado reescreve o padrão achado e substitui pelo sub'''
result_sub = re.sub(r'da India', 'do Mundo!', 'Av é a maior comunidade de Analytics da India')
print('sub =>', result_sub)
'''compile combina expressões regulares com objetos de padrões'''
pattern = re.compile('hoje') # hoje é objeto de padrão
av = pattern.findall('Av Paulista hoje está vazia.') 
print('compile =>', av)
'''expressão mais comumente usado
.   => corresponde qualquer caractere único exeto a nova linha
?   => corresponde a 0 ou uma ocorrências do padrão, encontra-se a esquerda
+   => corresponde a 1 ou mais ocorrência do padrão, encontra-se a esquerda
*   => corresponde a 0 ou mais ocorrência do padrão, encontra-se a esquerda
\w  => corresponde a 1 caractere alfanúmerico
\W  => corresponde a 1 caractere não alfanúmerico

'''



