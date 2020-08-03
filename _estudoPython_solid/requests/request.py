'''requests
biblioteca beaultiful solp para páginas web.
'''
from builtins import print

import requests

'''compartilhando o cabeçario http, vem junto com requesição
cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://google.com.br'}
meus_cookies = {'Ultima-visita': '10-10-2020'}
meus_dados = {'Username': 'Guigui',
         'Password': '12345'}
         headers=cabecalho, cookies=meus_cookies, data=meus_dados
         '''
try:
    '''passar estes dados somente via post'''
    requisicao = requests.post('http://uniesp.edu.br/sites/maua/')
    status = requisicao.status_code
    text = requisicao.text
except Exception as err:
    print('Erro', err)
print('+=' *30)
print('Status:', status)
print('+=' *30)
print(text)
