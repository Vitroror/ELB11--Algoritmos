lista = [i for i in range(1,11)]
print('Lista original:',lista)
for i, item  in enumerate(lista):
    lista[i] = item*item
print('Lista modificada:',lista)
