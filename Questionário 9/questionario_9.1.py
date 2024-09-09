txt='Quem lê pela primeira vez a versão original de Viagens de Gulliver, tendo como pano de fundo uma vaga lembrança de adaptações infantis, espanta-se ao constatar que tem nas mãos um dos textos mais amargos do cânone ocidental. Como observa George Orwell no prefácio incluído nesta edição, o livro de Jonathan Swift, apesar de todo o seu ressentimento e misantropia, é uma obra deliciosa, que permite vários níveis de leitura. É primeiro um livro de viagens - ou melhor, uma sátira aos livros de viagens, tal como Dom Quixote é, entre outras coisas, uma sátira aos romances de cavalaria; para as crianças, é uma história de aventuras, cheia das criaturas fantásticas e do humor escatológico de que tanto gostam; e é um dos marcos iniciais da ficção científica.'
palavras = txt.split()
print(f'O texto tem {len(palavras)} palavras')

total = 0
for p in palavras:
    total += len(p.rstrip('.,;:'))
print(f'O texto tem {total} letras (excluídos espaços e pontuação)')
print(f'O comprimento médio das palavras é de {total/len(palavras):.2} letras')
frases=txt.split('. ')
print(f'O texto contém {len(frases)} frases') 