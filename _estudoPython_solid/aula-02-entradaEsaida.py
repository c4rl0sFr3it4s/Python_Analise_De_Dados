#uma funcao print(), so aceita string
'''
print('Hellow word')
print('Segundo print\nTerceiro print\tQuarto print')
#variaveis objeto
nome = 'Carlos'
idade = 27
altura = 1.78

o python voce pode jogar dentro de uma variavel, funcao, valores
vendo tipo, python adota tipo
print(type(nome))
tipo_nome = type(nome)
tipo_idade = type(idade)
tipo_altura = type(altura)

#automaticamente ele descobre o tipo de variavel que tem lá dentro
print('Nome {} Idade {} Altura {} '.format(nome, idade, altura))
print('tipo nome {}\ntipo idade {}\ntipo altura {}'.format(tipo_nome, tipo_idade, tipo_altura))

concatenando com + tem como colocar tudo dentro de uma variavel
frase = nome + 'tem' + idade + 'anos' + altura + 'de altura'
print(frase)
# o que é jogado dentro de uma função é chamada de argumentos

#entrada no sistema, retorna sempre uma string
nome = input('Escreve seu nome: ')
idade = input('Escreve sua idade:')
altura = input('Escreva sua altura: ')
print('Olá {} voçê tem {} anos e {:.4} de altura'.format(nome, idade, altura))
'''
#operacoes aritmeticas
numero1 = 10
numero2 = 53
numero3 = 74.3
resultado = (numero1 + numero2) / numero3
#pega a raizQ do numero1
raizQ = numero1 ** (1/2)
print('O resultado é: {:.3}'.format(resultado * 5))
print('A raizQ de 10 é {:.3}'.format(raizQ))