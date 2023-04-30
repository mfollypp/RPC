# **Questão 3**

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