# Relatório sobre o trabalho de RPC

## A ideia principal do trabalho é implementar uma chamada remota a procedimento usando a biblioteca RPyC de Python.

## Grupo:
- Matheus Folly
- Juan Pablo
- Thiago Laet

---

# [**Questão 1**](Question01/question1.md)

## **Tarefa**:
> Execute o servidor em uma máquina e execute o cliente na mesma máquina. Para isso basta executar o programa python do servidor sem argumentos e o do cliente com o argumento "localhost".

## **Questão**:
> Explique o que foi impresso no cliente.

## **Resposta**:
```python
<__main__.MyService object at 0x0000025762AFBD60>
42
43
```
> Foi impresso no cliente o atributo root que da conexão que da acesso ao serviço exposto pelo servidor, o retorno da função exposed e o valor da variável exposed do server.py que dentro do RPyC são elementos expostos.

---

# [**Questão 2**](Question02/question2.md)

## **Tarefa**:
> Execute o servidor em uma máquina e execute o cliente em outra máquina. Para isso basta executar o programa python do servidor sem argumentos e o do cliente em outra máquina com o argumento "nome_da_maquina_servidor".

## **Questão**:
> Explique o que foi impresso no cliente.

## **Resposta**:
```python
<__main__.MyService object at 0x0000025762AFBD60>
42
43
```
> Foi impresso no cliente o atributo root que da acesso ao serviço exposto pelo servidor, o retorno da função exposed e o valor da variável exposed do server.py que são elementos expostos.

---

# [**Questão 3**](Question03/question3.md)

## **Tarefa**:
> Execute o programa cliente abaixo na mesma máquina.
```python
import rpyc
import sys
import os

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]
conn = rpyc.connect(server,18861)

print(c.get_question)
```

## **Questão**:
> Explique o que ocorreu.

## **Resposta**:
```python
AttributeError: cannot access 'get_question'
```
> O cliente não consegue acessar a função pois ela não está exposed no servidor, então toma o erro acima.

---

# [**Questão 4**](Question04/question4.md)

## **Tarefa**:
> Escreva um programa cliente que cria um vetor de n posições, onde n é definido pelo usuário, com elementos variando de 0 a n-1. Este procedimento chama um procedimento no servidor que soma os elementos do vetor e retorna o resultado da soma. O programa cliente deve imprimir o valor de soma.

## **Questão**:
> Mostre o código do cliente e do servidor.

## **Resposta**:
### No server.py foi adicionado
```python
def exposed_array_sum(self, array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum
```
### No client.py foi adicionado
```python
n = int(input("Enter the array size: "))
v = []
for i in range(n):
    v.append(int(input("Enter the element of the array: ")))

print("The array sum is:", conn.root.array_sum(v))
```
> Enter the array size: 3
>
> Enter the element of the array: 2
>
> Enter the element of the array: 3
>
> Enter the element of the array: 5
>
> The array sum is: 10

---

# [**Questão 5**](Question05/question5.md)

## **Tarefa**:
> Inclua no seu código do cliente e do servidor as instruções abaixo para medir o tempo de execução:
```python
start = time.time()
instruções
end = time.time()
print(end-start)
```
> Execute o cliente e servidor na mesma máquina para um vetor de 10000 posições.

## **Questão**:
> Indique o tempo de execução para obter o resultado no cliente e o tempo para executar o procedimento no servidor.

## **Resposta**:

> **Tempo no cliente para obter o resultado:** 0.8626573085784912
>
> **Tempo para executar o procedimento no servidor:** 0.8606574535369873

---

# [**Questão 6**](Question06/question6.md)

## **Tarefa**:
> Inclua no seu código do cliente e do servidor as instruções abaixo para medir o tempo de execução:
```python
start = time.time()
instruções
end = time.time()
print(end-start)
```
> Execute o cliente e servidor em máquinas diferentes para um vetor de 10000 posições.

## **Questão**:
> Indique o tempo de execução para obter o resultado no cliente e o tempo para executar o procedimento no servidor.

## **Resposta**:

> **Tempo no cliente para obter o resultado:** 100.28835463523865
>
> **Tempo para executar o procedimento no servidor:** 100.2725841999054

### **OBS:** Foi utilizado o `sync_request_timeout` para modificar o valor padrão de 30s. O `sync_request_timeout` é responsável pelo tempo de timeout de espera por resultado, então se antes o default era 30s, se o tempo de espera por resposta do cliente com o servidor passasse de 30s, ele daria erro devido ao timeout.
```python
conn._config['sync_request_timeout'] = 240
```

---

# [**Questão 7**](Question07/question7.md)

## **Tarefa**:
> Execute o cliente e servidor na mesma máquina para um vetor de 10000 posições. Depois, execute o cliente e servidor em máquinas diferentes para um vetor de 10000 posições.

## **Questão**:
> Existe diferença nos tempos obtidos? Explique a razão de existir diferença ou de não existir diferença.

## **Resposta**:
> Existe diferença devido a latência da conexão entre as máquinas e pelo fato que o RPyC passa o vetor por referência, então para cada elemento no vetor o RPyC fica interagindo entre cliente e servidor, aumentando o tempo necessário para realizar a soma.

---

# [**Questão 8**](Question08/question8.md)

## **Tarefa**:
> Faça uma tabela mostrando o tempo de execução do cliente e servidor executando em uma mesma máquina, com n ={100, 1000, 10000}.

## **Questão**:
> O que você observa em relação ao tempo de execução para os três valores de n?

## **Resposta**:

### Cliente
>| 100 | 1000 | 10000
>| ----- | ----- | -----
>| 0.009998798370361328 | 0.08600020408630371 | 0.7691152095794678

### Servidor
>| 100 | 1000 | 10000
>| ----- | ----- | -----
>| 0.00899648666381836 | 0.08600020408630371 | 0.7681152820587158

> Observa-se que o tempo para os 3 valores de n são bem próximos como o esperado por estarem sendo executados na mesma máquina

---

# [**Questão 9**](Question09/question9.md)

## **Tarefa**:
> Faça uma tabela mostrando o tempo de execução do cliente e servidor executando em máquinas diferentes, com n ={100, 1000, 10000}.

## **Questão**:
> O que você observa em relação ao tempo de execução para os três valores de n?

## **Resposta**:

### Cliente
>| 100 | 1000 | 10000
>| ----- | ----- | -----
>| 1.0020337104797363 | 11.132964372634888 | 108.86889910697937

### Servidor
>| 100 | 1000 | 10000
>| ----- | ----- | -----
>| 0.974616289138794 | 11.07751727104187 | 108.8212022781372

> Observa-se que o tempo para os 3 valores de n são bem maiores como o esperado por estarem sendo executados em máquinas diferentes

### **OBS:** Foi utilizado o `sync_request_timeout` para modificar o valor padrão de 30s. O `sync_request_timeout` é responsável pelo tempo de timeout de espera por resultado, então se antes o default era 30s, se o tempo de espera por resposta do cliente com o servidor passasse de 30s, ele daria erro devido ao timeout.
```python
conn._config['sync_request_timeout'] = 360
```

---

# [**Questão 10**](Question10/question10.md)

## **Tarefa**:
> Faça uma tabela mostrando o tempo de execução do cliente e servidor executando em uma mesma máquina, com n ={100, 1000, 10000}. Depois, faça uma tabela mostrando o tempo de execução do cliente e servidor executando em máquinas diferentes, com n ={100, 1000, 10000}.

## **Questão**:
> Compare as duas tabelas, indique se existem diferenças nos tempos de execução, e explique a existência ou não existência de diferenças.

## **Resposta**:

## **Mesma máquina:**
### Cliente
>| 100 | 1000 | 10000
>| ----- | ----- | -----
>| 0.009998798370361328 | 0.08600020408630371 | 0.7691152095794678

### Servidor
>| 100 | 1000 | 10000
>| ----- | ----- | -----
>| 0.00899648666381836 | 0.08600020408630371 | 0.7681152820587158

## **Máquinas diferentes:**
### Cliente
>| 100 | 1000 | 10000
>| ----- | ----- | -----
>| 1.0020337104797363 | 11.132964372634888 | 108.86889910697937

### Servidor
>| 100 | 1000 | 10000
>| ----- | ----- | -----
>| 0.974616289138794 | 11.07751727104187 | 108.8212022781372

> Como foi analisado na questão 7, existe diferença devido a latência da conexão entre as máquinas e pelo fato que o RPyC passa o vetor por referência, então para cada elemento no vetor o RPyC fica interagindo entre cliente e servidor, aumentando o tempo necessário para realizar a soma.