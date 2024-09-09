linhas=[1, 2, 3, 4, 5, 4, 3, 2, 1]
# Crie um loop externo que que percorra as linhas: 
for lin in linhas:                # percorre todas as 9 linhas da lista
# Crie um loop interno (encaixado) que imprima a quantidade de asteriscos por linha em cada coluna:
    for col in range(lin):        # percorre a quantidade de colunas de cada linha
        print('*',end=' ')        # imprimindo a quantidade de asteriscos daquela linha
    print()                     # print() sem argumentos só muda para a próxima linha