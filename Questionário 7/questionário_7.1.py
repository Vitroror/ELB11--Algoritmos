cols = len(M[0])
lins = len(M)
print(f'A matriz M tem {lins} linhas e {cols} colunas')
print()
for lin in range(lins):
    for col in range(cols):
        print(f'{M[lin][col]:3}', end="")
    print()