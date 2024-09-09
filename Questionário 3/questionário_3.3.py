ano = int(input('Digite um ano: '))

if ano <= 1582 or ano > 2100:
    print("Data inválida")
    exit()
    
if ano % 4 != 0:
    print("Ano não é bissexto")
elif ano % 100 != 0:
    print("Ano é bissexto")
elif ano % 400 == 0:
    print("Ano é bissexto")
else:
    print("Ano não é bissexto")