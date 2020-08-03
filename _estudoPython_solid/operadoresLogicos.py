'''
operadores lógicos
if - else
boolean sao dados que tem 2 formas true ou false
através destes dados o python vai tomar uma decisão
operadores relacionais: ==, >, <, >=, <=, !=
conectivos: and, or, not - não
aritméticos: +, -, *, / divisão, // divisão inteira, % modulo resto da divisão, ** exponenciasão
#################################################################################################
var_verdade = True
var_falso = False

if var_verdade == True:
    print('var_verdade é verdadeiro')

        tudo que estiver aqui dentro esta dentro da
        estrutura de decisão if.
        operadores relacional == retorna True ou False.

#saindo
print('Sai da estrutura de decisão.')
a = 20
b = 10
if (a > b) and ('abacaxi' == 'abacaxi'):
    print(a, 'é maior que', b)
else:
    print(b, 'é maior que', a)
print('Sai da estrutura de decisão')
#print('{}{}'.format(type(var_verdade), type(var_falso)))
'''
#menu
print('\t--Opções:\n1- Escreve Carlos\n2- Escreve Maria\n3- Escreve João')
op = input('Escolha uma opção: \n')
if op == '1':
    print('Carlos')
elif op == '2':
    print('Maria')
elif op == '3':
    print('João')
else:
    print('Opção invalida')
print('Encerrando o programa.....')