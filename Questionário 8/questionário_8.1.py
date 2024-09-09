dic = {}
for x in range(ord('A'),ord('F')):
    dic[chr(x)] = x

print('dic =',dic)

print('chaves =',end=' ')
for j in dic.keys():
    print(j, end=' ')
print()

print('valores =',end=' ')
for l in dic.values():
    print(l, end=' ')
print()

print('itens =',end=' ')
for o,v in dic.items():
    print(o,v, end='   ')