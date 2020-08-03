# comentario ctrl + /, ctrl + alt + r, auto identação, ctrl + shift + f10
frase = 'Oi, tudo bem?'
'''
strings
python trata a frase como se fosse uma lista, lista de letras.
letra começa do indice 0, 1, em diante.
'''
print(frase)
print(frase[0], frase[1], frase[2], frase[3], frase[4], frase[5], frase[6], frase[7], frase[8], frase[9], frase[10], frase[11], frase[12])
print(len(frase))
# conta todos os caracteres dentro de uma string, espaço em branco, caracteres especiais.
troca_bem = frase.replace('bem', 'ok')
troca_frase = frase.replace('Oi, tudo bem?', 'Olá, como você está')
print(troca_bem)
print(troca_frase)
# subistitui o caractere ou frase de uma string
print(troca_frase.count('o'))
print(troca_frase.count('m'))
# conta o numero de vezes que um caracter aparece na frase
print(frase.find('t'))
print(frase.find('?'))
# mostra a possição que o caractere apareçe na string
print(frase.split())
print(frase.split(','))
# separa uma string nos espaços parthen, escolhendo o token para ser separado ,
print(''.join(frase.split(',')))
print(frase.split('tudo'))
print('tudo'.join(frase.split('tudo')))
# junta a string, caso sendo separada por um split()
print(frase.upper())
# transformando string em caixa alta
print(frase.lower())
# transformando string em caixa baixa
print('lower com capitalize =>', frase.lower().capitalize())
print(frase.title())
# deixa as primeiras letras da string em maiusculas
print(frase.swapcase())
# troca maiusculos para minusculas, minusculas para maiusculas.
'''rodando testes nas strings'''
print('UPPER'.isupper())
# a string UPPER é superior - saida sempre em boolean - True - False
print('uPPER'.isupper())
# a string uPPER é superior - saida sempre em boolean - True - False
print('lower'.islower())
# a string lower é baixo - saida sempre em boolean - True - False
print('Lower'.islower())
# a string Lower é baixo - retorna em boolean - False
print('Este Titulo'.istitle())
# checando se é um titulo - os primeiros caracteres começa com letra Maiuscula
print('Este não é um titulo'.istitle())
# chacando se é um tirulo - os primeiros caracteres começa com letra Maiuscula
print('123Abc'.isalnum())
# checando se a string é alfanumérica - apenas letras e numeros não caracteres especiais
print('1@a'',abc'.isalnum())
# checando se a string é alfanumerica - apenas letras e numeros
print('abcdefghijklmnopqrstuvxwyz'.isalpha())
# checando se a string tem somente letras
print('0123456789'.isdigit())
# chegando se ela contém somente numeros
print(' '.isspace())
# checando se a string existe espaço
print('A string.'.ljust(15), 'contém espaço')
# adicionando 15 espaço a direita.
print('A string.'.rjust(15), 'contém espaco')
# adicionando 15 espaco a esquerda
print('A string'.center(15))
# centraliza uma string dentro do espaco
print('String'.ljust(15).strip())
# com strinp(), separa a string com o mesmo argumento em ambos os lados
print('String'.rjust(15).strip())
# com strip(), separa a string com o mesmo argumento em ambos os lados
