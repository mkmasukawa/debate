# Calcula próxima rodada 

## Objetivo do programa

Este programa foi feito para agilizar a contagem de pontos e sorteio de duplas e competiçes de debate. O programa minimiza a repetição de duplas e funções.

Na primeira rodada, as duplas são selecionadas aleatoriamente. A partir da segunda rodada, as duplas são classificadas por pontuação e agrupadas. O programa verifica qual a função desempenhada (abertura, whip, etc.) pela dupla e evita repetições.

No momento, o programa não possui interface gráfica e precisa ser rodado no terminal. Veja como rodar um programa .py [aqui](https://stackoverflow.com/questions/1522564/how-do-i-run-a-python-program).

## O que o programa faz

O programa lê uma tabela onde são salvos dados de cada rodada do debate. A tabela precisa ser preenchida manualmente a cada tabela e salva em um formato específico. Na primeira rodada, o programa sorteia grupos aleatórios para debater. Após a primeira rodada, o programa faz grupos de duplas com pontuaçes semelhantes. O programa também determina a função de cada dupla, evitando funções que já foram cumpridas em rodadas anteriores.

**Atenção!** O programa só funciona quando o número de duplas é múltiplo de 4.

## Como o programa funciona

### Como usar
1. Para rodar o programa, é necessário ter duas tabelas com o nome planilha1.csv e planilha2.csv na mesma pasta do programa contendo o nome das duplas e a pontuação em cada rodada.

As tabelas devem estar no formato .csv. As duas tabelas são iguais e devem ser preenchidas manualmente da mesma forma. A razão para duas tabelas é evitar erros de digitação. Caso as tabelas sejam preenchidas de forma diferente ou de forma incorreta, um aviso é dado no terminal.

Na primeira rodada, a tabela tem o seguinte formato (Não usar espaço entre os valores, apenas "," para separar os valores):

>Nome 1,Nome   
A,B  
C,D  
E,F  
G,H

Ondee A, B, C, D, E, F, G, H são o nome dos competidores e (A,B), (C, D), (E, F), (G,H) são as duplas.

À medida que mais rodadas são adicionadas, a tabela tem o formato:

>Nome 1,Nome 2, Rodada 1  
A,B,posiçãoA;posiçãoB;pontosA;pontosB  
C,D,posiçãoC;posiçãoD;pontosC;pontosD  
E,F,posiçãoE;posiçãoF;pontosE;pontosF  
G,H,posiçãoG;posiçãoH;pontosG;pontosH


Onde a posição do indivíduo é a posição no debate 
* 1 = primeiro a falar (abertura)
* 2 = segundo a falar (abertura)
* 3 = terceiro a falar (segundo primeira defesa)
* 4 = quarto a falar (segundo primeira oposição)
* 5 = quinto a falar (segundo segunda defesa)
* 6 = sexto a falar (segunda oposição)
* 7 = sétimo a falar (whip defesa)
* 8 = oitavo a falar (whip oposição)

E a pontuação é a pontuação individual, sendo a pontuação da dupla a média da pontuação de cada componente na rodada.

Exemplo de tabela com um grupo de debate e uma rodada:

>Nome 1,Nome 2,Rodada 1  
Alan,Bruna,1;3;70;90  
Carlos,Diego,2;4;60;50  
Ernesto,Fernanda,5;7;40;80  
Gabriela,Hector,6;8;90;90

_Nesta rodada, por exemplo, Ernesto foi o quinto a falar (segundo da segunda defesa) e fez 40 pontos. Fernanda, sua dupla, foi a sétima a falar (whip defesa) e fez 80 pontos, logo, como dupla fizeram (40+80)/2 = 60 pontos._

Exemplo de tabela com dois grupos de debate já com duas rodadas:

>Nome 1,Nome 2,Rodada 1, Rodada 2  
Alan,Bruna,1;3;70;90,2;4;60;50  
Carlos,Diego,2;4;60;50,5;7;40;80  
Ernesto,Fernanda,5;7;40;80,6;8;90;90  
Gabriela,Hector,6;8;90;90,6;8;90;90  
Ivan,João,1;3;70;90,2;4;60;50  
Kelvin,Leandro,2;4;60;50,5;7;40;80  
Manuela,Neide,5;7;40;80,6;8;90;90  
Oparin,Pepe,6;8;90;90,6;8;90;90  

2. O programa irá retornar o nome das duplas, a pontuação de cada indivíduo e a pontuação geral. As duplas aparecem em ordem crescente de pontuação.

Em seguida, o programa imprime no terminal os grupos selecionados e a função de cada um.

Note que podem existir várias possibilidades que não tem repetição de função, nestes caso, a reexecução do programa pode sugerir uma distribuição diferente de duplas. Para que a competição seja mais justa, deve-se sempre utilizar o resultado da primeira execução do programa, ao menos que as tabelas de pontuação contenham erros.

Exemplo de output do programa:

>Pontuação geral:  
('Carlos', 100, 'Diego', 130, 115)  
('Kelvin', 100, 'Leandro', 130, 115)  
('Alan', 130, 'Bruna', 140, 135)  
('Ivan', 130, 'Jo\xc3\xa3o', 140, 135)  
('Ernesto', 130, 'Fernanda', 170, 150)  
('Manuela', 130, 'Neide', 170, 150)  
('Gabriela', 180, 'Hector', 180, 180)  
('Oparin', 180, 'Pepe', 180, 180)    

>Grupo 1  
Dupla Carlos e Diego são 3 a falar  
Dupla Kelvin e Leandro são 2 a falar  
Dupla Alan e Bruna são 1 a falar  
Dupla Ivan e João são 4 a falar  

>Grupo 2  
Dupla Ernesto e Fernanda são 2 a falar  
Dupla Manuela e Neide são 1 a falar  
Dupla Gabriela e Hector são 4 a falar  
Dupla Oparin e Pepe são 3 a falar  

## Como executar
Para executar o programa, é necessário que as planilhas estejam na mesma pasta do programa .py. Python versão 2.7 é recomendada. Python 3 pode ser utilizado com pequenas modificações no código. 

**Após cada rodada é necessário atualizar as planilhas manualmente utilizando um editor de texto. **

## Como contribuir
Uma interface gráfica facilitaria o uso do programa. Talvez a estrutura do código não seja a melhor para ser implementada com uma interface para usuários, mas o algoritmo é eficiente para tornar mais justo a competição de debates. Sinta-se livre para usar este código ou partes dele.

## Crédito
Este programa foi originalmente feito por Marcos Masukawa.

## Licença
Este programa é de uso livre atribuindo cŕedito.
