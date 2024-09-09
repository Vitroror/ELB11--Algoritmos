lista = []
y = 1

x = int(input("Digite o número: (0 para terminar) "))

if x < 0:
    print("Use números positivos!")

elif x > 0:
    lista.append(x)

else:
    print("A média dos ", len(lista), "números digitados vale", sum(lista)/len(lista))
    exit()
    
while y == 1 :
    x = int(input("Digite o número (0 para terminar) "))
    
    if x < 0:
        print("Use números positivos!")

    elif x > 0:
        lista.append(x)
        
    else:
        print("A média dos ", len(lista), "números digitados vale", sum(lista)/len(lista))
        exit()
