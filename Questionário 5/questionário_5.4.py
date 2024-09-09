"""
Capítulo 4 - JAR - Exercício 4.10
Escreva uma função celsius(fahrenheit) que receba
um valor de uma temperatura Fahrenheit e devolva
seu equivalente em Celsius.
Escreva então outra função, que faça uso da primeira para
imprimir os valores equivalentes
das temperaturas Fahrenheit em Celsius entre 0 e 300,
com incrementos de 10.
A função usa esses valores como padrão, mas pode ser chamada
com qualquer valor inicial, final e passo se desejado.
"""
def celsius(fahrenheit):
    return (fahrenheit-32)*5/9

def imprime_tabela(início=0, fim=300, passo=10):
    print(f"{'fahrenheit':>12}{'celsius':>12}")
    for i in range(início, fim+1,passo):
        print(f'{i:>12}{celsius(i):>12.1f}')