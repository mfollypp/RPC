import rpyc
import sys
import os
import time

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

conn = rpyc.connect(server,18861)

n = int(input("Enter the array size: "))
v = []
for i in range(n):
    v.append(int(input("Enter the element of the array: ")))

print("The array sum is:", conn.root.array_sum(v))