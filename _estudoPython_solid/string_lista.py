'''
string grupo de caracteres, trata a frase como uma LISTA
de caracteres.
para imprimir a primeira letra frase[0]
lista é assim 1 caractere 0, 2 caractere 1, 3 caractere 2 etc
[0,1,2,3,4,5,6,7,8,9,10] -> indice
 O,i, ,t,u,d,o, ,b,e,m
LISTA é uma estrutura de dados coleção que pode guardar varios tipos de dados dentro
separado por virgula, para o python é mesma coisa que uma string cada letra é um nome.
['João', 'Maria', 'Carlos', 'Francine']
    0,     1,       2,         3       -> indice
impresso
['João', 'Maria', 'Carlos', 'Francine', 10, 10.2]
'''
#string
frase = 'Oi, tudo bem?'
#operacoes com string
frase_separada = frase.split(',')

#lista
lista_nomes = ['João', 'Maria', 'Carlos', 'Francine', 10, 10.2]

#operações com LISTAS
print('Lista -> \'', lista_nomes[0:2], '\'')
lista_nomes.append('Geralda')
lista_nomes.append('Lorena')
lista_nomes.remove('Geralda')
#lista_nomes.clear()
lista_nomes.insert(5, 'Creuza')
lista_nomes[0] = 'Robervania'
contador_carlos = lista_nomes.count('Maria')

#saida lista
print(lista_nomes)
print('Contando João \"', contador_carlos, '\"')
print('Tamanho da Coleção \"', len(lista_nomes), '\"')
print('Função de pilha Pop\"', lista_nomes.pop(), '\"')
print(lista_nomes)
'''
lista_nomes, imprime tudo
lista_nomes[0:2], imprime do indice 0 ate 1, não incluiso o 2
lista_nome[-1], de trás para frente
append adiciona no ultimo lugar da lista
remove remove da lista
clear limpa toda a lista
insert insere no indice que escolher
lista_nome[0] = 'Robervania', adicionando no indice escolhido
count('Maria') contagem quantas vezes contém na Coleção
len(lista_nomes) traz o tamanho da coleção
pop(), funcao de pilha o primeiro que entra é o ultimo que sai, e retira da lista
LISTA é mutável, e ordenada do jeito que é inserido  
'''
#saida com string
print('Frase -> \'', frase[0:5:1], '\'')
print('Frase em caixa baixa -> \"', frase.lower(), '\"')
print('Frase separada com split() \"', frase_separada, '\"')
print('Acessando o indice da coleção do split() \"', frase_separada[0], '\"')
'''
pegando do indice 0 ate o 5 frase[0:5], dando um step passos frase[0:5:1], 1 e de quantos em quantos vai pular
passando somente o passo ele retorna ao contrario frase[::-1]
[inicio:dividir:passo]
lower(), traz tudo para caixa baixa
split(), transforma a frase em uma lista, indicando aode você quer
'''
