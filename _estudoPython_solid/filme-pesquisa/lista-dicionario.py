galera = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Digite o nome: '))
    pessoas['idade'] = int(input('Digite a idade: '))
    soma += pessoas['idade']
    while True:
        pessoas['sexo'] = str(input('Digite o sexo [M|F]: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Erro!, Digite M ou F.')
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar [S|N]:')).upper()[0]
        if resp in 'SN':
            break
        print('Erro!, Resposta é apenas "S" ou "N".')
    if resp == 'N':
        break
print('+=' *30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) a média de idade é de {media:5.2f} anos.')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera: # para cada na lista galera
    if p['idade'] >= media: # um item na lista
        print('   ', end='')
        for k, v in p.items(): # dicionario key, value
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRANDO>>')
