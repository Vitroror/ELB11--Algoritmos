### Q1
O código define as constantes matemáticas 𝜋 (PI) e 𝑒 (E) com 15 casas decimais e usa o número imaginário 𝑖. Ele verifica a identidade de Euler (𝑒^𝜋𝑖 + 1 = 0) e exibe o resultado formatado para duas casas decimais.

### Q2.1
Este código calcula a média de duas notas inseridas pelo usuário e avalia a aprovação ou reprovação com base na média e no número de faltas. Se o número de faltas for inválido ou se uma das notas estiver fora do intervalo válido (0-10), o programa encerra. O aluno é reprovado se tiver mais de 5 faltas ou se a média for menor que 6.

### Q2.2
O código recebe um número em ponto flutuante e realiza várias aproximações usando funções da biblioteca `math`. Ele calcula a aproximação para cima, para baixo, para o valor mais próximo e em direção a zero, tanto para o número positivo quanto para seu negativo.

### Q2.3
O código calcula a raiz quadrada de um número fornecido pelo usuário. Ele verifica se o número é negativo e, se for, exibe uma mensagem de erro e encerra o programa, pois não é possível calcular a raiz real de um número negativo.

### Q2.4
Este código calcula a área de um triângulo com base e altura fornecidas pelo usuário.

### Q3.1
Este código solicita ao usuário a quantidade de faltas e duas notas. Ele verifica se os valores são válidos (quantidade de faltas entre 0 e 20 e notas entre 0 e 10). Dependendo do número de faltas e da média das notas, o aluno é classificado como "Reprovado por faltas", "Reprovado por nota" ou "Aprovado".

### Q3.2
O código verifica se um número fornecido pelo usuário é divisível por 3, 5 e/ou 7. Ele imprime mensagens diferentes dependendo das combinações de divisibilidade, ou se não for divisível por nenhum dos três números.

### Q3.3
**Descrição:** Este código determina se um ano fornecido pelo usuário é bissexto. O programa verifica se o ano está no intervalo permitido (1582 a 2100) e, em seguida, aplica as regras para identificar anos bissextos.  
**Lógica:** Um ano é bissexto se for divisível por 4 e não por 100, a menos que também seja divisível por 400.

### Q3.4
**Descrição:** O código calcula o novo salário de um funcionário com base em um percentual de aumento, que depende do valor atual do salário. Ele utiliza diferentes percentuais dependendo da faixa salarial.  
**Faixas de aumento:** 20% para salários até 1000, 18% para salários entre 1000 e 2000, 15% para salários entre 2000 e 4000, e 10% para salários acima de 4000.

### Q3.5
**Descrição:** Este código verifica se três valores fornecidos pelo usuário podem formar um triângulo e, em caso afirmativo, identifica o tipo de triângulo: equilátero, isósceles ou escaleno.  
**Lógica:** Um triângulo é válido se a soma de quaisquer dois lados for maior que o terceiro.

### Q3.6
**Descrição:** Este código classifica uma pessoa com base na idade fornecida pelo usuário. Ele verifica se a idade é válida (entre 0 e 120) e imprime a classificação correspondente (bebê, criança, pré-adolescente, adolescente, jovem, meia-idade ou idoso).  
**Intervalos de classificação:** Variam de "Bebê" para idades de 0 a 3 anos até "Idoso" para idades acima de 65 anos.

### Q3.7
**Descrição:** O código converte a idade de um cão em "idade humana" com base em seu peso (classificando-o como pequeno, médio ou grande) e idade. A conversão utiliza diferentes fatores para cães com menos de 2 anos e para cães com 2 anos ou mais.  
**Cálculos:** Aplica fatores de conversão específicos para cães pequenos, médios e grandes, levando em consideração se o cão tem menos ou mais de 2 anos.

### Q4.1
**Descrição:** O programa calcula a soma dos quadrados dos números inteiros de 1 até um número fornecido pelo usuário (não incluído). Se o número fornecido for negativo, o programa encerra.  
**Lógica:** Utiliza uma lista de compreensão para calcular os quadrados e a função `sum()` para encontrar a soma total.

### Q4.2
**Descrição:** Este código calcula a média de números positivos fornecidos pelo usuário. O programa continua pedindo números até que o usuário insira 0, momento em que calcula e imprime a média dos números digitados. Números negativos são ignorados.  
**Lógica:** Os números válidos são armazenados em uma lista, e a média é calculada ao encerrar a entrada com 0.

### Q4.3
**Descrição:** Converte temperaturas de Celsius para Fahrenheit em intervalos de 10 graus, começando de 0 até 100 graus Celsius.  
**Lógica:** Utiliza um loop `while` para calcular e exibir a temperatura equivalente em Fahrenheit para cada valor de Celsius.

### Q4.4
**Descrição:** Este programa permite ao usuário inserir números inteiros positivos e calcula o maior número inserido, além de contar quantos números válidos foram digitados. Números negativos são ignorados, e o programa encerra quando 0 é digitado.  
**Lógica:** Utiliza um loop `while True` para receber os números e atualizar as variáveis de contagem e o maior valor, encerrando quando 0 é inserido.

### Q4.5
**Descrição:** O código imprime uma forma piramidal de asteriscos em nove linhas. A quantidade de asteriscos por linha segue a sequência: 1, 2, 3, 4, 5, 4, 3, 2, 1.  
**Lógica:** Um loop externo percorre a lista de números de asteriscos para cada linha, enquanto um loop interno imprime o número de asteriscos correspondente.

### Q4.6
**Descrição:** Este código desenha um quadrado de asteriscos com um lado especificado pelo usuário. As bordas do quadrado são compostas por asteriscos, e o interior é preenchido com espaços.  
**Lógica:** Utiliza três loops para imprimir as bordas superior, inferior e laterais do quadrado.

### Q4.7
**Descrição:** O programa desenha um losango usando asteriscos. O tamanho do losango é baseado no valor fornecido pelo usuário. Ele é dividido em duas partes: a parte superior crescente e a parte inferior decrescente.  
**Lógica:** Utiliza dois loops `for` para imprimir as duas metades do losango, ajustando o espaçamento para criar a forma correta.

### Q5.1
**Descrição:** Calcula o volume de um cilindro dado seu diâmetro e altura.

### Q5.2
**Descrição:** Gera uma tabela com as raízes quadradas dos números de 1 a 10.

### Q5.3
**Descrição:** Imprime uma árvore de Natal em formato de texto usando loops `for` e uma função para desenhar os galhos e a base.

### Q5.4
**Descrição:** Define uma função para converter temperaturas de Fahrenheit para Celsius e outra para imprimir uma tabela de conversão de 0 a 300 graus Fahrenheit, com incrementos de 10.

### Q6.1
**Descrição:** Gera uma lista de números de 1 a 10, eleva cada elemento ao quadrado e exibe a lista original e a lista modificada.

### Q6.2
**Descrição:** Gera uma lista de números de 0 a 50 e cria outra lista contendo apenas múltiplos de 7 que não são múltiplos de 3.

### Q6.3
**Descrição:** Cria um padrão de asteriscos em formato de losango, usando loops e listas para armazenar e imprimir os padrões.

### Q6.4
**Descrição:** Manipula uma lista de números primos, inserindo novos elementos em posições específicas.

### Q6.5
**Descrição:** Simula o funcionamento de uma fila com operações de chegada e saída de elementos, usando métodos de lista como `append()`, `extend()` e `pop()`.

### Q7.1
**Descrição:** Imprime uma matriz representada por uma lista de listas e exibe o número de linhas e colunas da matriz.

### Q8.1
**Descrição:** Cria um dicionário com letras de 'A' a 'E' como chaves e seus respectivos valores em ASCII. Depois, exibe as chaves, os valores e os itens (pares chave-valor) do dicionário.

### Q8.2
**Descrição:** Contém dois dicionários: um com estados brasileiros e suas siglas, e outro com siglas e suas regiões. Recebe do usuário o nome de um estado e exibe sua sigla e a região correspondente, contando quantos estados existem nessa região. Caso o estado não seja encontrado, informa que o nome é inválido.

### Q8.3
**Descrição:** Usa dois dicionários: um para os meses e outro para armazenar nomes de pessoas com suas datas de nascimento. Cria uma lista de tuplas a partir do dicionário e exibe os dados das pessoas usando os dicionários e as tuplas.

### Q8.4
**Descrição:** Calcula a quantidade de votos em uma lista de notas e determina a nota mais e menos votada. Em seguida, calcula e imprime a porcentagem de votos para cada nota em um total de votos.

### Q9.1
**Descrição:** Processa um texto para contar o número de palavras, o número total de letras (excluindo espaços e pontuações) e a média de comprimento das palavras. Também conta o número de frases no texto.

### Q9.2
**Descrição:** Define uma função que recebe um nome completo e o formata em um padrão: último sobrenome em primeiro lugar, seguido do primeiro nome e abreviações dos nomes intermediários.

### Q9.3
**Descrição:** Define uma função que verifica se uma frase é um palíndromo (lida da mesma forma de trás para frente). Remove acentos, espaços e pontuações da frase antes da verificação.

### Q9.4
**Descrição:** Define uma função para imprimir um quadrado e uma grade, usando caracteres especiais da tabela ASCII. O quadrado inclui bordas e um smiley no centro, e a grade é uma matriz com bordas e divisões internas.

### Q9.5
**Descrição:** Gera uma sequência de bytes de 0x80 a 0xFF, decodifica-os usando a codificação 'cp850', e imprime os caracteres resultantes em um formato organizado.
