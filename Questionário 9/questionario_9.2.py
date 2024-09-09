def formata_nome(nome):
    l_nome = nome.split()      # separa em uma lista
    abrev = []                 # lista de abreviaturas vazia
    for n in l_nome[1:-1]:     # coleta do segundo ao penúltimo
        abrev.append(n[0]+'.') # coloca na lista (se tiver)
    s_abr = ' '.join(abrev)    # junta abreviaturras
    print(f'{l_nome[-1]}, {l_nome[0]} {s_abr}')