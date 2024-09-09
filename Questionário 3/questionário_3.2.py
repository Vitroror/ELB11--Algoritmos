str_input = 'Digite o valor do número: '
str_3_5_7 = 'é divisível por 3, 5 e 7'
str_5_7 = 'é divisível só por 5 e 7'
str_3_7 = 'é divisível só por 3 e 7'
str_3_5 = 'é divisível só por 3 e 5'
str_7 = 'é divisível só por 7'
str_5 = 'é divisível só por 5'
str_3 = 'é divisível só por 3'
str_nada = 'não é divisível por 3 nem por 5 nem por 7'

n = int(input(str_input))

if (n%3==0) and (n%5==0) and (n%7==0):
    print(n, str_3_5_7)
elif (n%3!=0) and (n%5==0) and (n%7==0):
    print(n, str_5_7)
elif (n%3==0) and (n%5!=0) and (n%7==0):
    print(n, str_3_7)
elif (n%3==0) and (n%5==0) and (n%7!=0):
    print(n, str_3_5)
elif (n%3!=0) and (n%5!=0) and (n%7==0):
    print(n, str_7)
elif (n%3!=0) and (n%5==0) and (n%7!=0):
    print(n, str_5)
elif (n%3==0) and (n%5!=0) and (n%7!=0):
    print(n, str_3)
else:
    print(n, str_nada)