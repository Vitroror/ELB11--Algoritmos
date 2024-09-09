a = int(input("Valor do primeiro lado: "))
b = int(input("Valor do segundo lado: "))
c = int(input("Valor do terceiro lado: "))

if a + b <= c or a + c <= b or b+c <= a:
    print("Não é um triângulo")
elif a == b == c:
    print("O triângulo é equilátero")
elif a == b or a == c or b == c:
    print("O triângulo é isóceles")
else:
    print("O triângulo é escaleno")