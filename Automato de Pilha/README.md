### Instruções para o Arquivo do Programa
#### Linha 1:
Alfabeto de entrada. Ex: "a b"
#### Linha 2:
Alfabeto Auxiliar. Ex: "X Z"
#### Linha 3:
Símbolo para representar o vazio (epsilon). Por padrão é "B" ou "e p s i l o n"
#### Linha 4:
Símbolo inicial da pilha. Por padrão é utilizado o símbolo "Z"
#### Linha 5:
Conjunto de Estados. Ex: "q0 q1 q2 q3 q4"
#### Linha 6:
Estado Inicial. Ex: "q0"
#### Linha 7:
Conjunto de Estados de Aceitação. Ex "qf"
#### Transições:
Por útimo vem as regras de transição. O formato é: 

"estado atual símbolo lido da palavra  símbolo do topo da pilha próximo estado símbolos a serem empilhados" 
(topo da pilha|base da pilha)
