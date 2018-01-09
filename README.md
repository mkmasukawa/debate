# Calcula duplas 

Este programa foi feito para agilizar a contagem de pontos de uma competição de debate. Por enquanto ele no possui interface gráfica e 
precisa ser rodado no terminal.

## Como o programa funciona

### Como usar
1. Para rodar o programa, é necessário ter duas tabelas com o nome planilha1.csv e planilha2.csv na mesma pasta do programa contendo o nome das duplas e a pontuação em cada rodada.
As tabelas devem estar no formato .csv. As duas tabelas são iguais e devem ser preenchidas manualmente da mesma forma. A razão de existir 
duas tabelas é para evitar erros de digitação. Caso as tabelas sejam preenchidas de forma diferente, um aviso é dado no terminal.

Na primeira rodada, a tabela tem o formato (Não usar espaço entre os valores, apenas "," para separar os valores)

Nome 1,Nome 2
A,B
C,D
E,F
G,H
...

Ondee A, B, C, D, E, F, G, H são o nome dos competidores e (A,B), (C, D), (E, F), (G,H) são as duplas.

À medida que mais rodadas são adicionadas, a tabela tem o formato.

Nome 1,Nome 2
A,B,posiçãoA;posiçãoB;pontosA;pontosB
C,D,posiçãoC;posiçãoD;pontosC;pontosD
E,F,posiçãoE;posiçãoF;pontosE;pontosF
G,H,posiçãoG;posiçãoH;pontosG;pontosH
...

Onde a posição do indivíduo é a posição no debate 
* 1 = primeiro a falar (primeira defesa)
* 2 = segundo a falar (primeira oposição)
* 3 = terceiro a falar (segundo defesa)
* 4 = quarto a falar (segunda oposição)
* 5 = quinto a falar (whip)
* 6 = sexto a falar
* 7 = sétimo a falar
* 8 = oitavo a falar


2. O programa irá 

##
execute o arquivo no terminal.


## Como contribuir

## Crédito

## Licença
