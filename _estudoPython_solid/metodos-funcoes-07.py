'''metodos-funções
print(), todas vez que tiver um parentese é uma função

print('Olá Mundo')
print(len('Olá Mundo'))
    função
    def soma(numero1, numero2):
        soma = numero1 + numero2
        return soma


    metodo
    def procedimento_soma(n1, n2):
        div = n1 / n2
        print('A divisão entre {} e {} é = {:.4}'.format(n1, n2, div))


    metodo
    def imprime_oi():
        print('Oi')


    def tem_sete_itens(argumento):
        if len(argumento) == 7:
            return True
        else:
            return False


    retorno da função
    resp = soma(75, 1289)
    procedimento com passagem de parametro
    procedimento_soma(10, 2)
    metodo
    imprime_oi()
    funcão_sete_letras, string, lista, pode passar qualquer conjunto
    #   if tem_sete_itens('abcdefg'):
    if tem_sete_itens([1, 2, 3, 4, 5, 6, 7]):
        print('Tem sete itens. ')

    saida
    print('A somar é = ', resp)    
'''
'''
Escreva uma função que recebe 1 objeto de colecao, lista, tupla, set, dicionário
e retorne o valor do maior numero dentro desta funcão.
Faça outra funcão que retorne o menor numero de uma coleção
'''
'''maior valor'''
def maior_valor_itens(lista):
    mai = 0
    valor = []
    for c in range(0, len(lista)):
        valor.append(int(lista[c]))
        if c == 0:
            mai = valor[c]    
        else:
            if valor[c] > mai:
                mai = valor[c]  

    return mai

'''menor valor'''
def menor_valor_itens(lista):
     men = 0
     valor = []
     for c in range(0, len(lista)):
         valor.append(int(lista[c]))
         if c == 0:
             men = valor[c]
         else:
             if valor[c] < men:
                 men = valor[c]
    
     return men



lista = ['1', '22', '333', '4444', '55555', '666666']
maior_valor = maior_valor_itens(lista)
menor_valor = menor_valor_itens(lista)
'''saida '''
# maior valor
print(f'O maior valor é {maior_valor}')
print(f'O menor valor é {menor_valor}')