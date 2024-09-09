import math

# Preencha abaixo o valor da constante PI com 15 casas decimais
PI = 3.141592653589793

# Preencha abaixo o valor da constante E com 15 casas decimais
E = 2.718281828459045
I = 1j

# Os dois prints a seguir servem para verificar se você
# prencheu os valores corretos das constantes:
print('PI vale', PI)
print('E vale', E)

# O print a seguir é para informar o que será feito:
print('Verificando a identidade de Euler:')

# Complete o print abaixo como está na bibliografia
# Não use copiar e colar. Aproveite para treinar!
# Além disso, com copiar e colar você pode usar caracteres inválidos para Python
print("0 = {:.2f}".format(E**(PI*I) + 1))