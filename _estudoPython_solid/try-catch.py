'''tratamento de erros
try - except
'''
try:
    num = 100 / 0
    print('')
except Exception as err:
    print('Erro ao dividir por { 0 }', err)

print('Fim da execusão.')