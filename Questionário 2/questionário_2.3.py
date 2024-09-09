import math

n = float(input('Entre com o número desejado: '))
if(n<0):
    print('Não existe raiz real de número negativo!')
    print('Encerrando o programa...')
    exit()
print('A raiz de', n, 'e',math.sqrt(n))