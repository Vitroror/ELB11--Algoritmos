'''Função para imprimir uma linha n vezes.'''
def print_line(line, n=1):       # n padrão é 1
    for i in range(n):           # repete n vezes
        for x in line:           # imprime os caracteres
            print(chr(x),end='') # da linha em questão
        print()                  # muda de linha no fim
# w é a largura do quadrado sem as bordas
# é também o dobro da altura sem as bordas
# w precisa ser ímpar para garantir a forma
w=15                                    

topo =[0x2554]+[0x2550]*w+[0x2557]      # topo do quadrado
lado =[0x2551]+[0x20]*w+[0x2551]        # lado do quadrado
meio =[0x2551]+[0x20]*(w//2)+\
      [0x263a]+[0x20]*(w//2)+[0x2551]   # lado com smile
base =[0x255a]+[0x2550]*w+[0x255d]      # base do quadrado

# definição do quadrado: lista de tuplas contendo linha e n
# n é o número de vezes que a linha deve ser impressa
quadrado=[
    (topo,1),     # 1 lina do topo do quadrado
    (lado,w//4),  # 2 linhas de lados do quadrado
    (meio,1),     # 1 linha do meio do quadrado
    (lado,w//4),  # 2 linhas de lados do quadrado
    (base,1),     # 1 linha da base do quadrado
    ]
# agora acessa cada tupla de linha e manda imprimir:
for x in quadrado:
    print_line(*x) # desempacota cada tupla e imprime
    
# agora a definição das linhas da grade:    
topog = [0x2554]+[0x2550]*(w//2)+[0x2566]+\
        [0x2550]*(w//2)+[0x2557]
ladog = [0x2551]+[0x20]*(w//2)+[0x2551]+\
        [0x20]*(w//2)+[0x2551]
meiog = [0x2560]+[0x2550]*(w//2)+[0x256c]+\
        [0x2550]*(w//2)+[0x2563]
baseg = [0x255a]+[0x2550]*(w//2)+[0x2569]+\
        [0x2550]*(w//2)+[0x255d]
# definição da lista de tuplas da grade:
grade = [
    (topog,1),    
    (ladog,w//4), 
    (meiog,1),   
    (ladog,w//4), 
    (baseg,1) 
    ]
# agora acessa cada tupla de linha da grade e imprime:
for x in grade:
    print_line(*x)