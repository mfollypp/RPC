import rpyc
import sys
import os
import time

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

conn = rpyc.connect(server,18861)

#----------------------------QUESTION 1 -----------------------------
print(conn.root)
print(conn.root.get_answer())
print(conn.root.the_real_answer_though)

# Foi impresso no cliente o retorno da funcao exposed e o valor da variavel exposed do server
#----------------------------QUESTION 1 -----------------------------

#----------------------------QUESTION 4 -----------------------------
n = int(input("Enter the array size: "))
v = []
#for i in range(n):
#    v.append(int(input("Enter the element of the array: ")))
start = time.time()
for i in range(n):
    v.append(i)

print("The array sum is:", conn.root.array_sum(v))
#----------------------------QUESTION 4 -----------------------------

#----------------------------QUESTION 5 -----------------------------
end = time.time()
print(end - start)
# 0.8626573085784912 no cliente e 0.8606574535369873 no servidor
#----------------------------QUESTION 5 -----------------------------