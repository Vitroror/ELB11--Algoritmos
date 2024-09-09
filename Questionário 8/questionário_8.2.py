estados = {
    'acre':                'AC', 'alagoas':             'AL',
    'amapá':               'AP', 'amazonas':            'AM',
    'bahia':               'BA', 'ceará':               'CE',
    'espírito santo':      'ES', 'goiás':               'GO',
    'maranhão':            'MA', 'mato grosso':         'MT',
    'mato grosso do sul':  'MS', 'minas Gerais':        'MG',
    'pará':                'PA', 'paraíba':             'PB',
    'paraná':              'PR', 'pernambuco':          'PE',
    'piauí':               'PI', 'rio de janeiro':      'RJ',
    'rio grande do norte': 'RN', 'rio grande do sul':   'RS',
    'rondônia':            'RO', 'roraima':             'RR',
    'santa catarina':      'SC', 'são paulo':           'SP',
    'sergipe':             'SE', 'tocantins':           'TO',
}

regiões = {
    'AC':'Norte',        'AL':'Nordeste',     'AP':'Norte',
    'AM':'Norte',        'BA':'Nordeste',     'CE':'Nordeste',
    'ES':'Sudeste',      'GO':'Centro-Oeste', 'MA':'Nordeste',
    'MT':'Centro-Oeste', 'MS':'Centro-Oeste', 'MG':'Sudeste',
    'PA':'Norte',        'PB':'Nordeste',     'PR':'Sul',
    'PE':'Nordeste',     'PI':'Nordeste',     'RJ':'Sudeste',
    'RN':'Nordeste',     'RS':'Sul',          'RO':'Norte',
    'RR':'Norte',        'SC':'Sul',          'SP':'Sudeste',
    'SE':'Nordeste',     'TO':'Norte',
}

est = input('Digite o nome de um estado: ')
try:
    sigla = estados[est.lower()]       
    reg = regiões[sigla]               
     
    print(f'\n{est} ({sigla}) fica na região {reg}')

    print()                            

    list_regiões=list(regiões.values()) 
    qtde = list_regiões.count(reg)    

    print(f'A região {reg} tem {qtde} estados')
except KeyError:
    print('Nome inválido!')
    print('Encerrando...')