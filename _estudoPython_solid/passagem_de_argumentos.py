'''passagem de argumentos pela linha de comando
Todas as funções padroes do python é build in
Passagem pelo usuário pelo input,
E a saida usando o terminal
modulo sys permite utilizar algumas coisas do sistema operacional
['c:/Users/Ticar/Desktop/_estudoPython/passagem_de_argumentos.py'] 
arg 0, é sempre o caminho do arquivo python sistema operacional
abrir o terminal e rodar o arquivo .py ele vai abrir no argumento 0, que é o nome do arquivo
agora colocando mais argumento ele vai passando do sistema operacional para nosso script.
Pela linha de comando passa argumento, scripts para rodar em modo texto para o cara poder 
executar rapidamente
'''
import sys
'''
 variável dentro da sys, arg1 metodo, arg2 vai ser n1, arg3 vai ser n2
 arg1 o metodo que o sistema vai ter que fazer
 arg2 operador
 arg3 operando
'''
argumentos = sys.argv

def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

if argumentos[1] == "soma":
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "sub":
    resp = sub(float(argumentos[2]), float(argumentos[3]))


print(resp)
