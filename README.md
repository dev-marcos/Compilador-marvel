# Compilador para a Linguagem de Programação marvel

## 1.	Introdução

### 1.1	Propósito
O compilador desenvolvido descrito nesta especificação de requisitos de software elaborado para a linguagem Marvel é ser uma linguagem simples e de fácil entendimento e busca fazer alusões às personagens da franquia Marvel no funcionamento do programa com termos tais como “fury”, “drestranho”, “formiga” e etc.

### 1.2	Convenções do Documento
O documento foi escrito conforme os padrões da IEEE (Instituto de Engenharias Elétricas e Eletrônica), utilizando fonte Times New Roman tamanho 11, com alinhamento justificado e espaçamento 1.15 pt.

### 1.3	Público Alvo e Sugestões de Leitura
Este documento tem como objetivo atingir principalmente os programadores de linguagem de programação Marvel, e usuários do compilador em questão, a fim de se obter uma melhor compreensão é sugerido que o documento seja lido na ordem escrita.

### 1.4	Escopo da Linguagem
A linguagem de programação Marvel tem por seu objetivo utilizar elementos de várias linguagens, como C, JavaScript, Python e as transforma em algo mais lúdico com os elementos da franquia Marvel a fim de despertar o interesse dos usuários em programação.

### 1.5	E-BNF da Linguagem
```
(*Variavel*)
<inteiro> ::= 0|1|2|3|4|5|6|7|8|9
<caracteres> ::= “a”|”b”|”c”|”d”|”e”|”f”|”g”|”h”|”i”|”j”|”k”|”l”|”m”|”n”|”o”|”p”|”q”|”r”|”s”|”t”|”u”|”v”|”w”|”x”|”y”|”z”

<numero> ::= <inteiro><numero> | <inteiro>
<palavra> ::= <caracteres><palavra> | <caracteres>

(*Declaracao*)
<nome de funcao> ::= fury|hulk|visao|groot|rocket|venom|carnificina|madrox|golias|mistica|thanos|drestranho|dormamo|loki|formiga|america|stark|lince

(*Escopo do codigo*)
<encerrador> ::= avengers | rocket | shield | dormamo
<variavel> ::= <variavel>.<palavra> | <variavel>.<numero> | <palavra>
<finalizador> ::= <variavel>.<variavel> | <variavel>."<palavra>" | <encerrador> | <variavel>."<numero>" | <variavel>.<funcao>
<funcao> ::= <nome de funcao> -> <finalizador> | <nome de funcao> -> <funcao> | <nome de funcao> -> <variavel>.<funcao>
```

## 2.	Descrição Geral

### 2.1	Perspectiva de Produto
O software desenvolvido é um produto de autoria própria, e independente, desenvolvido por alunos de Engenharia de Computação da Universidade Tecnológica Federal do Paraná para a disciplina de Compiladores, as principais funções da linguagem de programação podem ser vistas nos tópicos a seguir.

### 2.2	Tabela de Símbolos
Abaixo pode ser vista a tabela de símbolos da linguagem de programação Marvel que explicita os símbolos, comandos e palavras reservadas da linguagem.

Tabela 1. Tabela de símbolos

| Símbolo	| Descrição |
| --- | --- |
| #	| Comentário |
| fury 	| Inicia o programa |
| hulk 	| Palavra reservada(variável) |
| visao	| Palavra reservada (p/ print) |
| groot	| Palavra reservada (p/ if) |
| rocket	| Palavra reservada (p/ endif) |
| venom 	| Palavra reservada (p/ soma) |
| carnificina	| Palavra reservada (p/subtração) |
| madrox	| Palavra reservada (p/ multiplicação) |
| golias 	| Palavra reservada (p/ maior) |
| mistica	| Palavra reservada (p/comparação) |
| thanos	| Palavra reservada (p/ divisão) |
| drestranho 	| Palavra reservada (p/laço de repetição) |
| dormamo 	| Palavra reservada (p/ end for) |
| formiga	| Palavra reservada (p/ menor que) |
| america	| Palavra reservada (p/ and) |
| stark	| Palavra reservada (p/ or) |
| shield	| Palavra reservada |
| avengers	| Palavra reservada |
| “”	| Constante literal |
| ->  	| Comando de atribuição |
| .	| Comando de atribuição |


### 2.3	Inicialização e encerramento do código
A inicialização e encerramento do código deve ser feito da seguinte forma:

```
#inicialização do programa
fury -> avengers

#encerramento do programa
fury -> shield
```

### 2.4	Declaração de variáveis
A declaração de variáveis deve ser feita da seguinte maneira:

```
# inicialização das variáveis
hulk -> var1.456 #variavel “var1” recebe o valor 456

hulk -> var2.”456” #variavel “var2” recebe o char 456
```


## 3.	Processos de compilação
Na Figura 1 podemos observar quais são as etapas realizadas por um compilador:

Figura 1 - Etapas de um compilador

![Etapas de um compilador](https://www.cadcobol.com.br/compiladores_wikipedia_autociencia.png) 


No entanto para o desenvolvimento da linguagem de programação Marvel foram utilizadas apenas a Análise Léxica, Análise Sintática, Análise Semântica e Gerador de Código Intermediário, foi utilizada a linguagem Python por se tratar de uma linguagem prática e eficiente. As etapas e o amadurecimento do desenvolvimento podem ser vistos nos tópicos a seguir:

### 3.1	Análise Léxica

A análise léxica é o primeiro processo realizado pelo compilador, e consiste em realizar uma varredura no código, removendo os espaçamentos e separando os tokens, alguns elementos da linguagem foram divididos em grupos para facilitar a análise, podemos observar os grupos na tabela abaixo:




As palavras reservadas como nomes de funções e nomes de variáveis são divididas neste grupo a fim de obter um fácil tratamento durante as análise, os literais são definidos como a parte digitada pelo usuário, normalmente entre aspas para simbolizar textos, os comandos de atribuição são símbolos que facilitam a identificação para posterior tratamento de chamadas de funções e atribuições de valores as variáveis  nas próximas etapas.
Abaixo podemos observar como o compilador efetua a análise léxica da linguagem:

```
#inicializador#
fur11y -> avengers

#atribuição de variaveis#
hulk -> var1."123"
hulk -> var2."456"

#atribuição e soma de variaveis#
hulk -> var3.venom -> var1.var2

#print de variaveis#
visao -> var3

#encerramento de laço#
fury -> shield
```

Para o código acima temos a seguinte resposta léxica:

```
Token = COMENTARIOS, Lexeme = '#', Row = 1, Column = 14
erro léxico, variável fur11y
Token = ID, Lexeme = 'fur11y', Row = 2, Column = 0
Token = CHAMADA_DE_FUNCAO, Lexeme = '->', Row = 2, Column = 7
Token = AVENGERS, Lexeme = 'avengers', Row = 2, Column = 10
Token = COMENTARIOS, Lexeme = '#', Row = 4, Column = 26
Token = HULK, Lexeme = 'hulk', Row = 5, Column = 0
Token = CHAMADA_DE_FUNCAO, Lexeme = '->', Row = 5, Column = 5
Token = ID, Lexeme = 'var1', Row = 5, Column = 8
Token = ATRIBUIR, Lexeme = '.', Row = 5, Column = 12
Token = INTEGER_CONST, Lexeme = '123', Row = 5, Column = 14
Token = HULK, Lexeme = 'hulk', Row = 6, Column = 0
Token = CHAMADA_DE_FUNCAO, Lexeme = '->', Row = 6, Column = 5
Token = ID, Lexeme = 'var2', Row = 6, Column = 8
Token = ATRIBUIR, Lexeme = '.', Row = 6, Column = 12
Token = INTEGER_CONST, Lexeme = '456', Row = 6, Column = 14
Token = COMENTARIOS, Lexeme = '#', Row = 8, Column = 33
Token = HULK, Lexeme = 'hulk', Row = 9, Column = 0
Token = CHAMADA_DE_FUNCAO, Lexeme = '->', Row = 9, Column = 5
Token = ID, Lexeme = 'var3', Row = 9, Column = 8
Token = ATRIBUIR, Lexeme = '.', Row = 9, Column = 12
Token = VENOM, Lexeme = 'venom', Row = 9, Column = 13
Token = CHAMADA_DE_FUNCAO, Lexeme = '->', Row = 9, Column = 19
Token = ID, Lexeme = 'var1', Row = 9, Column = 22
Token = ATRIBUIR, Lexeme = '.', Row = 9, Column = 26
Token = ID, Lexeme = 'var2', Row = 9, Column = 27
Token = COMENTARIOS, Lexeme = '#', Row = 11, Column = 19
Token = VISAO, Lexeme = 'visao', Row = 12, Column = 0
Token = CHAMADA_DE_FUNCAO, Lexeme = '->', Row = 12, Column = 6
Token = ID, Lexeme = 'var3', Row = 12, Column = 9
Token = COMENTARIOS, Lexeme = '#', Row = 14, Column = 22
Token = FURY, Lexeme = 'fury', Row = 15, Column = 0
Token = CHAMADA_DE_FUNCAO, Lexeme = '->', Row = 15, Column = 5
Token = SHIELD, Lexeme = 'shield', Row = 15, Column = 8

Recognize Tokens:  ['COMENTARIOS', 'ID', 'CHAMADA_DE_FUNCAO', 'AVENGERS', 'COMENTARIOS', 'HULK', 'CHAMADA_DE_FUNCAO', 'ID', 'ATRIBUIR', 'INTEGER_CONST', 'HULK', 'CHAMADA_DE_FUNCAO', 'ID', 'ATRIBUIR', 'INTEGER_CONST', 'COMENTARIOS', 'HULK', 'CHAMADA_DE_FUNCAO', 'ID', 'ATRIBUIR', 'VENOM', 'CHAMADA_DE_FUNCAO', 'ID', 'ATRIBUIR', 'ID', 'COMENTARIOS', 'VISAO', 'CHAMADA_DE_FUNCAO', 'ID', 'COMENTARIOS', 'FURY', 'CHAMADA_DE_FUNCAO', 'SHIELD']
```
Através da resposta do compilador podemos observar (na parte grifada) que caso exista algum erro no código fonte digitado pelo usuário, o analisador léxico o alerta, identificando a linha em que ocorre o erro e continua o processo de leitura, após isso o compilador segue para o processo de análise sintática.

### 3.2	Análise Sintática
O analisador sintático ou parser é a segunda etapa realizada pelo compilador e determina se o código inserido pelo usuário (após passar pelo analisador léxico) possui a estrutura e a sentença válidas para a linguagem Marvel. Normalmente para a análise sintática são criadas gramáticas livres de contexto e a validação da parte sintática depende da derivação da gramática, dessa maneira, caso uma entrada finalize em um terminal a mesma está correta, caso contrário ela é incorreta.

### 3.3	Análise Semântica
A análise semântica tem como objetivo verificar aspectos das instruções dadas ao compilador, nessa etapa é realizada a verificação da compatibilidade dos tipos na atribuição, duplas declarações, entre outros. Podemos pensar que a análise semântica realiza o tratamento que as etapas anteriores não executaram. Nessa etapa pode-se visualizar melhor como a linguagem desenvolvida se comporta através de grafos que podem ser visualizados no Apêndice A.      

### 3.4	Geração de código intermediário
A geração do código intermediário converte as expressões validadas anteriormente pelos analisadores para o código de três endereços, que simboliza uma sequência de instruções. O código intermediário possibilita a otimização do código intermediário, de modo a obter o código final mais eficiente, e simplificar a implementação do compilador e resolver a passagem do do código fonte para o objeto (alto-nível para baixo-nível) e possibilita a tradução de código intermediário para diversas máquinas.
Na Figura abaixo podemos entender como funciona o gerador de código intermediário:
