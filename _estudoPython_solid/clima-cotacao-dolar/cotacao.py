import requests
import json
import datetime
import time

# imprime cotacao
def imprime(usd, usdt, cad, eur, gbp, ars, btc,
            ltc, jpy, chf, aud, cny, ils, eth,
            xrp):
    print('+=' * 20)
    print('>>>COTAÇÃO<<<', datetime.datetime.now())
    print('Dólar comercial Alta =('+ usd+ ')')
    print('Dólar turismo Alta =('+ usdt+ ')')
    print('Dólar canadense Alta =('+ cad+ ')')
    print('Euro Alta =('+ eur+ ')')
    print('Libra Estrelina Alta =('+ gbp+ ')')
    print('Peso Argentino Alta =('+ ars+ ')')
    print('Bitcoin Alta =('+ btc+ ')')
    print('Litecoin Alta =('+ ltc+ ')')
    print('Iene Japonês Alta =('+ jpy+ ')')
    print('Franco Suíço Alta =('+ chf+ ')')
    print('Dólar Australiano Alta =('+ aud+ ')')
    print('Yuan Chinês Alta =('+ cny+ ')')
    print('Novo Shekel Israelense Alta =('+ ils+ ')')
    print('Ethereum Alta =('+ eth+ ')')
    print('Ripple Alta =('+ xrp+ ')')
    # for k, v in usd.items():
       # print(k, ' = (', v, ')')
    time.sleep(5)

# cotacao de dolar comercial
try:
    while True:
        requisicao = requests.get('https://economia.awesomeapi.com.br/all/')
        cotacao = json.loads(requisicao.content)
        # print(cotacao)
        imprime(cotacao['USD']['high'], cotacao['USDT']['high'], cotacao['CAD']['high'],
                cotacao['EUR']['high'], cotacao['GBP']['high'], cotacao['ARS']['high'],
                cotacao['BTC']['high'], cotacao['LTC']['high'], cotacao['JPY']['high'],
                cotacao['CHF']['high'], cotacao['AUD']['high'], cotacao['CNY']['high'],
                cotacao['ILS']['high'], cotacao['ETH']['high'], cotacao['XRP']['high'])
except Exception as err:
    print('Erro!', err)