# **Questão 6**

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