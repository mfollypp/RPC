# **Questão 2**

## **Tarefa**:
> Execute o servidor em uma máquina e execute o cliente em outra máquina. Para isso basta executar o programa python do servidor sem argumentos e o do cliente em outra máquina com o argumento "nome_da_maquina_servidor".
---
## **Questão**:
> Explique o que foi impresso no cliente.
---
## **Resposta**:
```python
<__main__.MyService object at 0x0000025762AFBD60>
42
43
```
> Foi impresso no cliente o atributo root que da conexão que da acesso ao serviço exposto pelo servidor, o retorno da função exposed e o valor da variável exposed do server.py que dentro do RPyC são elementos expostos.