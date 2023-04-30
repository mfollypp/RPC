import rpyc
import sys
import os
import time

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

conn = rpyc.connect(server,18861)
conn._config['sync_request_timeout'] = 240 # Para evitar timeout enquanto está realizando as contas

v = []
start = time.time()

for i in range(10000):
    v.append(i)

print("The array sum is:", conn.root.array_sum(v))

end = time.time()
print(end - start)