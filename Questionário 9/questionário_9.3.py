port_dic={
    'á':'a','é':'e','í':'i','ó':'o','ú':'u',
    'â':'a','ê':'e','ô':'o',
    'ã':'a','õ':'o',
    'à':'a', 'ç':'c',
    ' ':'','-':'',',':'','!':''
    }

trans_table = str.maketrans(port_dic)

def testa_palíndrome(str):
    print(str)
    pal = str.translate(trans_table).lower()
    if pal == pal[-1::-1]:
        print('Frase é palíndrome!')
    else:
        print('Frase não é palíndrome!')