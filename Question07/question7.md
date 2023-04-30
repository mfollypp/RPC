# **Questão 7**

## **Tarefa**:
> Execute o cliente e servidor na mesma máquina para um vetor de 10000 posições. Depois, execute o cliente e servidor em máquinas diferentes para um vetor de 10000 posições.

## **Questão**:
> Existe diferença nos tempos obtidos? Explique a razão de existir diferença ou de não existir diferença.

## **Resposta**:
> Existe diferença devido a latência da conexão entre as máquinas e pelo fato que o RPyC passa o vetor por referência, então para cada elemento no vetor o RPyC fica interagindo entre cliente e servidor, aumentando o tempo necessário para realizar a soma.