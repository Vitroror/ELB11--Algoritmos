p_f_até_2 = 12.5 # fator até 2 anos cão pequeno
m_f_até_2 = 10.5 # fator até 2 anos cão médio
g_f_até_2 =  9.0 # fator até 2 anos cão grande

p_f_mais_2 = 5.2 # fator mais que 2 anos cão pequeno
m_f_mais_2 = 5.7 # fator mais que 2 anos cão médio
g_f_mais_2 = 7.8 # fator mais que 2 anos cão grande

peso = float(input("Digite a peso do seu cão: "))
idade = float(input("Digite a idade do seu cão: "))

if 0 <= peso < 10.0:
    print("Classificação: Pequeno")
    if idade < 2:
        idade_humana = idade*p_f_até_2
    else:
        saldo = idade - 2
        idade_humana = 2*p_f_até_2 + saldo * p_f_mais_2
elif 10 <= peso < 23:
    print("Classificação: Médio")
    if idade < 2:
        idade_humana = idade * m_f_até_2
    else:
        saldo = idade - 2
        idade_humana = 2 * m_f_até_2 + saldo * m_f_mais_2
else:
    print("Classificação: Grande")
    if idade < 2:
        idade_humana = idade * g_f_até_2
    else:
        saldo= idade - 2
        idade_humana = 2 * g_f_até_2 + saldo * g_f_mais_2
print("Idade humana = ", idade_humana)