numerofaltas = int(input("Digite a quantidade de faltas: "))

nota1 = float(input("Qual é a primeira nota? "))

nota2 = float( input("E a segunda nota? "))

media = (nota1 + nota2)/2

print ("A média é ", media)

if numerofaltas > 20 or numerofaltas < 0:
    print("Número de faltas inválido! Encerrando...")
    exit()
    
if nota1 > 10 or nota1 < 0
    print("Nota inválida! Encerrando...")
    exit()
    
if numerofaltas > 5:
    print("Reprovado por faltas.")
elif media < 6:
    print("Reprovado por nota :(.")
else:
    print("Aprovado!")