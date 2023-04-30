# **Questão 10**

## **Tarefa**:
> Faça uma tabela mostrando o tempo de execução do cliente e servidor executando em uma mesma máquina, com n ={100, 1000, 10000}. Depois, faça uma tabela mostrando o tempo de execução do cliente e servidor executando em máquinas diferentes, com n ={100, 1000, 10000}.
---
## **Questão**:
> Compare as duas tabelas, indique se existem diferenças nos tempos de execução, e explique a existência ou não existência de diferenças.
---
## **Resposta**:

## **Mesma máquina:**
### Cliente
>| 100 | 1000 | 10000
>| ----------- | ----------- | -----------
>| 0.009998798370361328 | 0.08600020408630371 | 0.7691152095794678

### Servidor
>| 100 | 1000 | 10000
>| ----------- | ----------- | -----------
>| 0.00899648666381836 | 0.08600020408630371 | 0.7681152820587158

## **Máquinas diferentes:**
### Cliente
>| 100 | 1000 | 10000
>| ----------- | ----------- | -----------
>| 1.0020337104797363 | 11.132964372634888 | 108.86889910697937

### Servidor
>| 100 | 1000 | 10000
>| ----------- | ----------- | -----------
>| 0.974616289138794 | 11.07751727104187 | 108.8212022781372

> Como foi analisado na questão 7, existe diferença devido a latência da conexão entre as máquinas e pelo fato que o RPyC passa o vetor por referência, então para cada elemento no vetor o RPyC fica interagindo entre cliente e servidor, aumentando o tempo necessário para realizar a soma.