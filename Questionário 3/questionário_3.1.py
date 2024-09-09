numerofaltas = int(input("Digite a quantidade de faltas: "))

if numerofaltas > 5 and numerofaltas <= 20:
    print("Reprovado por faltas.")
    exit()

if numerofaltas < 0 or numerofaltas > 20:
    print("Quantidade de faltas inválida! Encerrando...")
    exit()

    
nota1 = float(input("Qual é a primeira nota? "))

if (nota1 > 10 or nota1 < 0):
    print("Nota inválida! Encerrando...")
    exit()

nota2 = float( input("E a segunda nota? "))

if (nota2 > 10 or nota2 < 0):
    print("Nota inválida! Encerrando...")
    exit()

media = (nota1 + nota2)/2

print ("A média é ", media)

if media < 6:
    print("Reprovado por nota :(.")
else:
    print("Aprovado.")
