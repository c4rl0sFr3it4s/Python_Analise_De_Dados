import requests
import json
from googletrans import Translator

'''
A máxima está em fahrenheit
273.15 para celsius
'''
cidade = str(input('Digite a cidade: '))
key = '2846992e8e77ad1ce03b041c5f566cfc'
try:
    requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ cidade+ '&APPID='+ key)
    tempo = json.loads(requisicao.content)
    print(tempo)
# escolher a chave do objeto dicionario
# atencao aos dados na saida como saiu como uma lista pefar o indice da lista
# neste caso só tem um indice na lista
# novamente se tornou uma lista
# cada api funciona de uma maneira tem que ir decifrando
    print('>>>PREVISÃO DO TEMPO<<<')
    estado = tempo['weather'][0]['main']
    traducao = Translator()
    print('Condição de tempo: ', traducao.translate(estado, dest='pt', src='auto'))
# temperatura
    print('Temperatura em CELSIUS: ', round(float(tempo['main']['temp']) - 273.15))
except Exception as erro:
    print('Erro!', erro)
