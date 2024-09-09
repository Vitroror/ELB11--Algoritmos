salario = float(input("Digite o valor do salário: "))

if salario <= 1000:
    percentual = 20
elif salario > 1000 and salario <= 2000:
    percentual = 18
elif salario > 2000 and salario <= 4000:
    percentual = 15
else:
    percentual = 10
    
percentual = percentual/100.0
aumento = percentual * salario
salarionovo = salario + aumento

print("Novo salário =", salarionovo)