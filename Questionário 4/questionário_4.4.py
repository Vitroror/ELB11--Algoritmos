"""
Este programa pede para o usuário ir digitando números inteiros positivos
Números negativos são ignorados.
Zero é interpretado como fim da série - leva ao encerramento.
O programa conta quantos números válidos já foram digitados e seleciona o
maior.
Antes do encerramento o programa informa quantos números válidos foram
digitados e qual o maior.
Se nenhum número válido tiver sido digitado o programa emite uma
mensagem informando que nenhum número válido foi digitado.
"""
maior = 0
digitados = 0
while True:
    num = int(input('Digite um número inteiro positivo: '))
    if num == 0:
        print('Foi digitado 0, encerrando...')
        break
    if num < 0:
        print(num, 'é negativo. Será ignorado...')
        continue
    digitados += 1
    if num > maior:
        maior = num
if maior > 0:
    if digitados > 1:
        print('Foram digitados',digitados,'números válidos.')
    else:
        print('Foi digitado somente um número válido.')
    print('O maior número válido digitado foi',maior)
else:
    print('Nao foi digitado nenhum número válido')

