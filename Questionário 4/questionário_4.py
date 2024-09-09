n = int(input('Qual o número final? '))

if n < 0:
    print("Use números positivos!")
    exit()

print("A soma dos quadrados de 1 a",n-1,"=",sum([i*i for i in range(1,n)]))
print("Verificação: soma =", sum([i*i for i in range(1,n)]))
