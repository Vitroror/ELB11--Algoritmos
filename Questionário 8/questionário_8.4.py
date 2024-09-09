total_votos = len(notas)

votos = [notas.count(x) for x in range(11)]

print('Foram consultados',total_votos,'usuários.\n')

print('A nota mais votada foi',votos.index(max(votos)))
print('A nota menos votada foi',votos.index(min(votos)))

print('\nParticipação porcentual de cada avaliação:\n')

for i in range(11):
    prc = votos[i]*100/total_votos
    print(f'Nota {i:2} obteve {prc:4.1f} % dos votos')