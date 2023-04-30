# **Questão 9**

## **Tarefa**:
> Faça uma tabela mostrando o tempo de execução do cliente e servidor executando em máquinas diferentes, com n ={100, 1000, 10000}.
---
## **Questão**:
> O que você observa em relação ao tempo de execução para os três valores de n?
---
## **Resposta**:

### Cliente
>| 100 | 1000 | 10000
>| ----------- | ----------- | -----------
>| 1.0020337104797363 | 11.132964372634888 | 108.86889910697937

### Servidor
>| 100 | 1000 | 10000
>| ----------- | ----------- | -----------
>| 0.974616289138794 | 11.07751727104187 | 108.8212022781372

> Observa-se que o tempo para os 3 valores de n são bem maiores como o esperado por estarem sendo executados em máquinas diferentes

### **OBS:** Foi utilizado o `sync_request_timeout` para modificar o valor padrão de 30s. O `sync_request_timeout` é responsável pelo tempo de timeout de espera por resultado, então se antes o default era 30s, se o tempo de espera por resposta do cliente com o servidor passasse de 30s, ele daria erro devido ao timeout.
```python
conn._config['sync_request_timeout'] = 360
```