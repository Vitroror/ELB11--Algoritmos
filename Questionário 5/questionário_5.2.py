"""
Tabela de raízes quadradas - questão 7 questionário 5
"""
import math

print(f"{'valor':^7}{'raiz do valor':^15}")
for i in range(1,11):
    print(f'{i:^7}{math.sqrt(i):^15.3f}')

