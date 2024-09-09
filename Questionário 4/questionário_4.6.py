n = int(input('Digite a quantidade de asteriscos por lado: '))
for lin in range(n):
    print('*',end=' ')
print()
for lin in range(1,n-1):
    print('*',end=' ')
    for col in range(1,n-1):
        print(' ',end=' ')
    print('*')
for lin in range(n):
    print('*',end=' ')