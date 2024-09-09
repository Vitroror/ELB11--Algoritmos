meses = {
     1:'Janeiro',    2:'Fevereiro',    3:'Março',
     4:'Abril',      5:'Maio',         6:'Junho',
     7:'Julho',      8:'Agosto',       9:'Setembro',
    10:'Outubro',   11:'Novembro',    12:'Dezembro'}


dic_pess = {
    'Marcelo':(3,4,1980),
    'João':   (4,5,1986),
    'Maria':  (24,8,1990),
    'Pedro':  (12,12,1996)}

lis_pess = []               
for k,v in dic_pess.items():  
    tup = k, v[0], v[1], v[2]  
    lis_pess.append(tup)       
    
tupl_pess = tuple(lis_pess)   

print('Listando a partir do dicionário:\n')
for k,v in dic_pess.items():
    print(f'{k:7}: nascido em {v[0]:2} de {meses[v[1]]:8} de {v[2]}')

print('\nListando a partir da tupla de tuplas:\n')
for t in tupl_pess:
    print(f'{t[0]:7}: nascido em {t[1]:2} de {meses[t[2]]:8} de {t[3]}')