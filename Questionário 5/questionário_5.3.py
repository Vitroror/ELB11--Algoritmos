"""
Capítulo 4 - exercício 4.6 - imprimir árvore de natal
usando laços for
Como o capítulo é de funções, usaremos também funções
Será usado o mesmo desenho da bibliografia, mas
com uma base ========
"""
def imprime_galho(n, max=11, car='*'):
    print(f'{car*n:^{max}}')

imprime_galho(1,car='@')
for i in range(3,6,2):
    imprime_galho(i)
for i in range(3,10,2):
    imprime_galho(i)
for i in range(5,10,2):
    imprime_galho(i)
for i in range(7,12,2):
    imprime_galho(i)
for i in range(3,6,2):
    imprime_galho(i,11,'|')
imprime_galho(11,11,'=')

