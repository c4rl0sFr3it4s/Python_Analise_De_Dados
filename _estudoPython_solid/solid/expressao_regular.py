'''
expressões regulares são muito poderosas permitem que padrões sejam achados ou casados.
com alguma parte da string, e alguma substituição pode ser feita se a expressão regular
casar com alguma parte da string.
'''
import re
frase = 'This is for testing regular expressions in python'
'''search - procure
conbine o resultado periodo 0, 4
'''
result_search = re.search('This', frase)
result_match = re.match('(.{20})(regular)', frase)
print(result_search)
print(result_match.group(0))
print(result_match.group(1))
print(result_match.group(2))
'''saindo resultado do padrao com group
com padrão simples
'''
result = re.match ('(.{10,20})(regular)', frase)
print(result.group(0))
'''usando intervalo
range neste caso 10 a quandidade de index que ele deve contar, 20 em uma escala de 20 caracteres
'''
another_test = 'a cat, a dog, a goat, a person'
'''fazendo uma escala range de intervalo'''
result_another = re.match('(.{5,20})(,)', another_test)
print(result_another.group(1))
'''mostra um comportamento indesejado 
fizemos o regex, padrão com intervalo do 5 indice da string até o 20 indice
ele nos trouxe todos sem o inicio do intervalo
'''
'''pegando somente a cat'''
result_anotherTest = re.match('(.{5,20}?)(,)', another_test)
print(result_anotherTest.group(1))
'''utilizando um ponto de interrogação
faz com que a função ache a menor quantidade possivel de caractere.
'''
