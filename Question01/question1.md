# **Questão 1**

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