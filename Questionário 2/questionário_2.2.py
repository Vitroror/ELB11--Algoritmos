import math

n = float(input("Digite um número em ponto flutuante: "))
print()
print(n, "aproximado para cima =", math.ceil(n))
print(n, "aproximado para baixo =", math.floor(n))
print(n, "aproximado para mais próximo =", round(n))
if n > 0:
    print(n, "aproximado em direção a zero =", math.floor(n))
elif n < 0:
    print(n, "aproximado em direção a zero =", math.ceil(n))
print()
print(-n, "aproximado para cima =",-math.floor(n))
print(-n, "aproximado para baixo =",-math.ceil(n))
print(-n, "aproximado para mais próximo =",-round(n))
if n > 0:
    print(-n, "aproximado em direção a zero =", -math.floor(n))
elif n < 0:
    print(-n, "aproximado em direção a zero =", -math.ceil(n))
    