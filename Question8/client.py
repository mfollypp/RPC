import rpyc
import sys
import os
import time

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

conn = rpyc.connect(server,18861)

v = []
start = time.time()
for i in range(100):
    v.append(i)
print("The array sum of array 100 is:", conn.root.array_sum(v))
end = time.time()
print(end - start)

v.clear()

start = time.time()
for i in range(1000):
    v.append(i)
print("The array sum of array 1000 is:", conn.root.array_sum(v))
end = time.time()
print(end - start)

v.clear()

start = time.time()
for i in range(10000):
    v.append(i)
print("The array sum of array 10000 is:", conn.root.array_sum(v))
end = time.time()
print(end - start)