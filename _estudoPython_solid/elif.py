chave = 7
numero = input('Digite um Numero: \n')
valor = int(numero)
if (chave == valor):
    print('Voçê acertou!')
elif (valor > chave):
    print('Voçê errou! O seu chute foi maior que o numero secreto!')
elif (valor < chave):
    print('Voçê errou! O seu chute foi menor que o numero secreto!')
