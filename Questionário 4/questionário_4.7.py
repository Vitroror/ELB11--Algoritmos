n=int(input('Digite o valor do lado do losango: '))

for i in range(1,n+1):
    print(f"{'*  '*n:>{n*3+i}}")
print()
for i in range(1,n+1):
    print(f"{'*  '*n:>{n*4-i}}")