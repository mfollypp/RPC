# **Questão 4**

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